# pylint: disable=invalid-name
"""
Usage:
  app [ -j=<path> -c=<path> | -h ]

Options:
    -h                      Show this help
    -j --jobs_dir=<path>           Specify directory with jobs descriptions
    -c --cv_file=<path>            Specify file with employee cv
"""

import os
from docopt import docopt
from __init__ import __version__
import main

DEFAULT_ARG = {
    '--jobs_dir': os.getcwd() + '/data/text_data/jobs/',
    '--cv_file': os.getcwd() + '/data/text_data/cv/cv_000001',
}

if __name__ == '__main__':
    args = docopt(__doc__, version=__version__)
    if not args['--jobs_dir']:
        args['--jobs_dir'] = DEFAULT_ARG['--jobs_dir']
    if not args['--cv_file']:
        args['--cv_file'] = DEFAULT_ARG['--cv_file']
    main.main(args['--jobs_dir'], args['--cv_file'])



