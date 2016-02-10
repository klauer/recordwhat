import logging
from . import get_record_by_name
from .record_info import link_types

import graphviz as gv

logger = logging.getLogger(__name__)


def get_all_record_links(rec):
    type_attrs = rec.attrs_of_type(link_types)
    return {attr: getattr(rec, attr).get(as_string=True)
            for attr in type_attrs}


def get_link_str(link_str):
    if ' ' in link_str:
        # strip off PP/MS/etc (TODO might be useful later)
        link_str = link_str.split(' ')[0]
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

    return link_str


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

    checked = []
    records_to_check = [get_record_by_name(rec) for rec in starting_records]

    while records_to_check:
        rec = records_to_check.pop()
        checked.append(rec.prefix)

        for attr, link_str in get_all_record_links(rec).items():
            try:
                link_str = get_link_str(link_str)
            except ValueError:
                continue

            inlink = (attr in list(rec.attrs_of_type('DBF_INLINK')))

            logger.debug('attr %s link str %s', attr, link_str)
            if '.' in link_str:
                link_rec, link_field = link_str.split('.')
            else:
                link_rec, link_field = link_str, 'VAL'

            link_rec = get_record_by_name(link_rec)
            if link_rec.prefix not in checked:
                records_to_check.append(link_rec)

            for _rec in [rec, link_rec]:
                if _rec.prefix not in nodes:
                    node_id += 1
                    nodes[_rec.prefix] = str(node_id)
                    graph.node(nodes[_rec.prefix], label=_rec.prefix)
                    logger.debug('created node %s (%s)', _rec.prefix,
                                 nodes[_rec.prefix])

            link_attr = link_rec.field_to_attr(link_field)
            logger.debug('edge %s -> %s', rec.prefix, link_rec.prefix)

            src, dest = nodes[rec.prefix], nodes[link_rec.prefix]
            srcl, destl = attr, link_attr

            if inlink:
                src, dest = dest, src
                srcl, destl = destl, srcl

            graph.edge(src, dest, label='{}/{}'.format(srcl, destl))

    return graph


def port_graph(ad_ports, *, graph=None):
    '''Create a graphviz graph from an areadetector port dictionary

    Parameters
    ----------
    ad_ports : dict
        Dictionary of port name to areaDetector plugin instance
    graph : graphviz.Graph, optional
        Graph instance to use. New one created if not specified.

    Returns
    -------
    graph : graphviz.Graph
    '''


    if graph is None:
        graph = gv.Digraph(format='svg')

    for port, plugin in ad_ports.items():
        graph.node(port, label='{}\n{}'.format(plugin.prefix, port))

    for dest_port, plugin in ad_ports.items():
        source_port = plugin.nd_array_port.get()
        graph.edge(source_port, dest_port)

    return graph
