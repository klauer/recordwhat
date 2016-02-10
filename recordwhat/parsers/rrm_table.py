""" Quick and imperfect script to parse the epics RRM (record reference manual)
for all of the table information on fields. Dumps to text files
"""

from __future__ import print_function
import os
from bs4 import BeautifulSoup


def get_record_names(fn='rrm_index.htm'):
    html = open(fn, 'rt').read()
    soup = BeautifulSoup(html)
    ret = {'RRM_3-14_Common.htm': 'common'}
    for tag in soup.findAll('a'):
        if '/RRM_3-14_' in tag['href']:
            s = tag.string.strip()
            filename = tag['href'].split('/')[-1]
            filename += '.htm'
            if '-' in s:
                rtyp = s.split(' ')[0]
                # print(filename, rtyp)
                ret[filename] = rtyp
    return ret

file_to_rtype = get_record_names()


def run(fn, output_path='output'):
    html = open(fn, 'rt').read()
    soup = BeautifulSoup(html)
    try:
        rtyp = file_to_rtype[os.path.split(fn)[1]]
    except KeyError:
        print('Not used', fn)
    else:
        print('--- %s ---' % (fn))
        print('Record type is', rtyp)

    records = []
    required_cols = [u'Field', u'Summary', u'Type', u'DCT',
                     u'Initial', u'Access', u'Modify', u'Rec Proc Monitor']
    new_header = None
    for table in soup.findAll("table"):
        cols = [c.string.strip() if c.string is not None
                else u''
                for c in table.findAll('th')]
        if not cols:
            continue
        print('--', cols)
        missing_cols = set(required_cols) - set(cols)
        if len(missing_cols) > 0:
            print('Missing columns', missing_cols)
            continue

        if new_header is None:

            new_cols = set(cols) - set(required_cols)
            if new_cols:
                print('new cols', new_cols)

            index_map = [(cols.index(col), required_cols.index(col))
                         for col in cols
                         if col in required_cols and col.strip()]

            new_header = list(required_cols)
            i = len(index_map)
            for j, col in enumerate(new_cols):
                if col:
                    index_map.append((cols.index(col), i))
                    i += 1
                    new_header.append(col)

            print('new header is', new_header)
        else:
            new_cols = set(cols) - set(new_header)
            try:
                new_cols.remove(u'')
            except:
                pass
            if new_cols:
                print('new columns introduced -- skipping table', new_cols)
                continue

        index_map = dict(index_map)
        for row in table.findAll('tr'):
            cols = row.findAll('td')
            strings = [c.string.strip() if c.string is not None
                       else u''
                       for c in cols]
            print(strings)
            records.append([strings[index_map[i]]
                           for i in range(len(new_header))])

    if new_header is None:
        print('-- empty file')
        return

    try:
        os.mkdir(output_path)
    except:
        pass

    with open(os.path.join(output_path, '%s.txt' % rtyp), 'wt') as f:
        print('\t'.join(new_header), file=f)
        for record in records:
            print('\t'.join(record), file=f)


RRM_PATH = 'rrm_html'
for fn in os.listdir(RRM_PATH):
    fn = os.path.join(RRM_PATH, fn)
    if fn.endswith('.htm'):
        run(fn)
        # break
