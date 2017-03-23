import subprocess
import re
import os.path

default_grep_path = '/cf-update/*.dbl'


def grep_pvs(expr, *, path=None, grep_tool='/bin/grep',
             ignore_exceptions=True, switches='-he'):
    '''Grep a path of dbl listings for a specific regex

    Parameters
    ----------
    expr: str
        Grep expression
    path : str, optional
        Path to search (defaults to util.default_grep_path)
    grep_tool : str, optional
        Grep binary to use (/bin/bash)
    switches : str, optional
        Grep tool switches (-he)
    ignore_exceptions : bool, optional
        Ignore permission errors and such when the grep tool is used
    '''
    if path is None:
        path = default_grep_path

    command = ('{grep_tool} {switches} "{expr}" {path}'
               ''.format(**locals()))

    try:
        stdout = subprocess.check_output(command, stderr=subprocess.DEVNULL,
                                         shell=True)
    except subprocess.CalledProcessError as ex:
        # some permissions errors in /cf-update
        if not ignore_exceptions:
            raise
        stdout = ex.output

    stdout = stdout.decode('ascii')
    for match in stdout.split('\n'):
        match = match.strip()
        if match:
            yield match


def find_file(fn, path):
    path = ['.'] + path.split(':')
    for s_path in path:
        test_fn = os.path.join(s_path, fn)
        if os.path.exists(test_fn):
            return test_fn
    return None


def fix_includes(text, path):
    offset = 0
    while True:
        m = re.search('^(\s*include\s*"(.*)".*)$', text[offset:],
                      flags=re.MULTILINE)
        if m is None:
            break
        offset += m.start()
        full_line = m.groups()[0]
        include_file = m.groups()[1]
        fn = find_file(include_file, path)
        if fn is None:
            offset += (m.end() - m.start())
            continue
        with open(fn, 'rt') as fin:
            insert_text = fin.read()
        text = text.replace(full_line, insert_text)
    return text


def read_file(fn, path=''):
    l_dir = os.path.dirname(fn)
    if l_dir:
        path = ':'.join((l_dir, path))
    with open(fn, 'rt') as fin:
        return fix_includes(fin.read(), path)
