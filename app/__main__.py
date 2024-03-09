# pylint: disable=invalid-name
"""
Usage:
  app [ -j=<path> -c=<path> | -h ]

Options:
    -h                      Show this help
    -j --jobs_file=<path>           Specify directory with jobs descriptions
    -c --cv_dir=<path>            Specify file with employee cv
"""

import os
from docopt import docopt
from __init__ import __version__
import main

DEFAULT_ARG = {
    '--jobs_file': os.getcwd() + '/data/rtu/jobs',
    '--cv_dir': os.getcwd() + '/data/rtu/cv_dir/',
}

if __name__ == '__main__':
    args = docopt(__doc__, version=__version__)
    if not args['--jobs_file']:
        args['--jobs_file'] = DEFAULT_ARG['--jobs_file']
    if not args['--cv_dir']:
        args['--cv_dir'] = DEFAULT_ARG['--cv_dir']
    main.main(args['--jobs_file'], args['--cv_dir'])



