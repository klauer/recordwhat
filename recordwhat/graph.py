from collections import namedtuple
import logging

from . import (get_record_by_name, RecordBase)
from .record_info import link_types
from ophyd import EpicsSignalRO

import graphviz as gv

logger = logging.getLogger(__name__)


def links_from_record(rec):
    type_attrs = rec.attrs_of_type(link_types)
    return {attr: getattr(rec, attr).get(as_string=True)
            for attr in type_attrs}


def get_link_str(link_str):
    if ' ' in link_str:
        # strip off PP/MS/etc (TODO might be useful later)
        link_str, additional_info = link_str.split(' ', 1)
    else:
        additional_info = ''

    if link_str.startswith('@'):
        # TODO asyn/device links
        raise ValueError('asyn link')
    if not link_str:
        raise ValueError('empty link')

    try:
        int(link_str)
    except Exception:
        pass
    else:
        # 0 or 1 usually and not a string
        raise ValueError('integral link')

    try:
        float(link_str)
    except Exception:
        pass
    else:
        raise ValueError('float link')

    return link_str, tuple(additional_info.split(' '))


def graph_links(*starting_records, graph=None):
    '''Create a graphviz digraph of record links

    All starting records will be included, along with any other records that
    are linked to from there.

    Parameters
    ----------
    *starting_records : str
        Record names
    graph : graphviz.Graph, optional
        Graph instance to use. New one created if not specified.

    Returns
    -------
    graph : graphviz.Graph
    '''
    node_id = 0
    nodes = {}

    if graph is None:
        graph = gv.Digraph(format='svg')

    for li in find_record_links(*starting_records):
        for rec in [li.record1, li.record2]:
            if rec.prefix not in nodes:
                node_id += 1
                nodes[rec.prefix] = str(node_id)
                graph.node(nodes[rec.prefix], label=rec.prefix)
                logger.debug('Created node %s (%s)', rec.prefix,
                             nodes[rec.prefix])

        src, dest = nodes[li.record1.prefix], nodes[li.record2.prefix]
        srcl, destl = li.attr1, li.attr2

        if li.type_ == 'DBF_INLINK':
            src, dest = dest, src
            srcl, destl = destl, srcl
            logger.debug('New edge %s -> %s', li.record2.prefix,
                         li.record1.prefix)
        else:
            logger.debug('New edge %s -> %s', li.record1.prefix,
                         li.record2.prefix)

        graph.edge(src, dest, taillabel=srcl, label=destl)

    return graph


LinkInfo = namedtuple('LinkInfo',
                      'record1 attr1 record2 attr2 type_ link_info')


def find_record_links(*starting_records):
    '''Get all related record links from a set of starting records

    All starting records will be included, along with any other records that
    are linked to from there.

    Parameters
    ----------
    *starting_records : str
        Record names

    Yields
    -------
    link_info : LinkInfo
        Link info
    '''
    checked = []
    records_to_check = list(starting_records)

    while records_to_check:
        to_check = records_to_check.pop()
        if not isinstance(to_check, RecordBase):
            rec1 = get_record_by_name(to_check, read_attrs=[])
        else:
            rec1 = to_check

        checked.append(rec1.prefix)

        logger.debug('--- record %s ---', rec1.prefix)

        for attr1, link_str in links_from_record(rec1).items():
            try:
                link_str, link_info = get_link_str(link_str)
            except ValueError:
                continue

            try:
                type_ = getattr(rec1, attr1).metadata.type
            except AttributeError:
                type_ = 'unknown'

            logger.debug('checking attribute %s (link = %s)', attr1, link_str)
            if '.' in link_str:
                rec2, field2 = link_str.split('.')
            elif attr1 == 'forward_link':
                rec2, field2 = link_str, 'PROC'
            else:
                rec2, field2 = link_str, 'VAL'

            if (rec2 not in checked and rec2 not in records_to_check):
                records_to_check.append(rec2)

            rec2 = get_record_by_name(rec2, read_attrs=[])
            attr2 = rec2.field_to_attr(field2)
            if attr2 is None:
                attr2 = field2

            li = LinkInfo(record1=rec1, attr1=attr1,
                          record2=rec2, attr2=attr2,
                          type_=type_, link_info=link_info)

            logger.debug('Link %s', li)
            yield li


def graph_links_with_subgraphs(*starting_records, graph=None, engine='dot',
                               subgraph_attrs=None):
    '''Create a graphviz digraph of record links

    All starting records will be included, along with any other records that
    are linked to from there.

    Subgraphs are created for each record, with nodes corresponding to
    fields (attributes) of those records.

    Note: layout engine 'neato' does not support subgraphs (dot and fdp at
    least do)

    Parameters
    ----------
    *starting_records : str
        Record names
    graph : graphviz.Graph, optional
        Graph instance to use. New one created if not specified.
    engine : str, optional
        Defaults to dot (see note above)
    subgraph_attrs : dict, optional
        Subgraph keyword attributes

    Returns
    -------
    graph : graphviz.Graph
    '''
    node_id = 0
    graphs = {}
    edges = []
    all_nodes = {}

    if graph is None:
        graph = gv.Digraph(format='svg')
        # graph.graph_attr['rankdir'] = 'TB'
        # graph.graph_attr['rank'] = 'same'

    graph.graph_attr['compound'] = 'true'

    if engine is not None:
        graph.engine = engine

    if subgraph_attrs is None:
        subgraph_attrs = {'graph': {'rankdir': 'TB',
                                    'rank': 'same',
                                    'style': 'bold',
                                    },
                          'node': {'shape': 'record',
                                   'style': 'filled'},
                          'edge': {},
                          }

    for li in find_record_links(*starting_records):
        for (rec, attr) in ((li.record1, li.attr1),
                            (li.record2, li.attr2)):
            if rec.prefix not in graphs:
                cluster_id = len(graphs) + 1
                sgraph = gv.Digraph(name='cluster_{}'.format(cluster_id))

                for key, attrs in subgraph_attrs.items():
                    sgraph.attr(key, **attrs)
                sgraph.graph_attr['label'] = '\n'.join((rec.prefix,
                                                        rec.record_type.get()))

                graphs[rec.prefix] = {'graph': sgraph,
                                      'nodes': {}
                                      }

            sgraph = graphs[rec.prefix]['graph']
            nodes = graphs[rec.prefix]['nodes']

            if attr not in nodes:
                node_id += 1
                nodes[attr] = str(node_id)
                sgraph.node(nodes[attr], label=attr)

                fully_qualified_name = '{}.{}'.format(rec.prefix, attr)
                all_nodes[fully_qualified_name] = str(node_id)

                logger.debug('Created node %s.%s (%s)', rec.prefix, attr,
                             nodes[attr])

        full1 = '{}.{}'.format(li.record1.prefix, li.attr1)
        full2 = '{}.{}'.format(li.record2.prefix, li.attr2)
        src, dest = all_nodes[full1], all_nodes[full2]
        src_attr, dest_attr = li.attr1, li.attr2

        if li.type_ == 'DBF_INLINK':
            src, dest = dest, src
            src_attr, dest_attr = dest_attr, src_attr
            logger.debug('New edge %s -> %s', li.record2.prefix,
                         li.record1.prefix)
        else:
            logger.debug('New edge %s -> %s', li.record1.prefix,
                         li.record2.prefix)

        edge_kw = {}

        process_passive = (('PP' in li.link_info) or
                           ('CPP' in li.link_info) or
                           ('CP' in li.link_info))
        if process_passive:
            edge_kw['style'] = 'bold'

        maximize_severity = (('MS' in li.link_info) or
                             ('MSS' in li.link_info) or
                             ('MSI' in li.link_info))
        if maximize_severity:
            edge_kw['color'] = 'red'

        edges.append((src, dest, edge_kw))

    # add the subgraphs to the main graph
    for sgraph_info in graphs.values():
        graph.subgraph(sgraph_info['graph'])

        # create invisible subgraph nodes to organize fields inside clusters
        nodes = [node for attr, node in
                 sorted(sgraph_info['nodes'].items())]
        for n1, n2 in zip(nodes, nodes[1:]):
            graph.edge(n1, n2, style='invis', weight='100')
        # weight=100 ensures they're aligned nicely

    # add all of the edges between graphs
    for src, dest, options in edges:
        graph.edge(src, dest, **options)

    return graph


def port_graph(ad_ports, *, graph=None, enabled_kw=None, disabled_kw=None):
    '''Create a graphviz graph from an areadetector port dictionary

    Parameters
    ----------
    ad_ports : dict
        Dictionary of port name to areaDetector plugin instance
    graph : graphviz.Graph, optional
        Graph instance to use. New one created if not specified.
    enabled_kw : dict, optional
        graph.edge keywords for an enabled link
    enabled_kw : dict, optional
        graph.edge keywords for a disabled link

    Returns
    -------
    graph : graphviz.Graph
    '''

    if graph is None:
        graph = gv.Digraph(format='svg')

    if disabled_kw is None:
        disabled_kw = dict(color='red')

    if enabled_kw is None:
        enabled_kw = dict(color='green')

    for port, plugin in ad_ports.items():
        graph.node(port, label='{}\n{}'.format(plugin.prefix, port))

    for dest_port, plugin in ad_ports.items():
        source_port = plugin.nd_array_port.get()
        plugin_enabled = plugin.enable.get()

        if plugin_enabled:
            kw = enabled_kw
        else:
            kw = disabled_kw

        graph.edge(source_port, dest_port, **kw)

    return graph
