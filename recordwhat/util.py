import subprocess


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
