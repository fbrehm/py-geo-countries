#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2015 by Frank Brehm, Berlin
@license: GPL3
@summary: unit tests for geo_countries.py
"""

import os
import sys
import logging
import argparse

try:
    import unittest2 as unittest
except ImportError:
    import unittest

# Own modules
_has_colored_logger = False
try:
    from pb_logging.colored import ColoredFormatter
    _has_colored_logger = True
except ImportError:
    pass

libdir = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))
sys.path.insert(0, libdir)


# =============================================================================

log = logging.getLogger('test_country')


# =============================================================================
def get_arg_verbose():

    arg_parser = argparse.ArgumentParser()

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-v", "--verbose", action="count",
        dest='verbose', help='Increase the verbosity level')
    args = arg_parser.parse_args()

    return args.verbose


# =============================================================================
def init_root_logger(verbose=0):

    root_log = logging.getLogger()
    root_log.setLevel(logging.WARNING)
    if verbose > 1:
        root_log.setLevel(logging.DEBUG)
    elif verbose:
        root_log.setLevel(logging.INFO)

    appname = os.path.basename(sys.argv[0])
    format_str = appname + ': '
    if verbose:
        if verbose > 1:
            format_str += '%(name)s(%(lineno)d) %(funcName)s() '
        else:
            format_str += '%(name)s '
    format_str += '%(levelname)s - %(message)s'
    formatter = None
    if _has_colored_logger:
        formatter = ColoredFormatter(format_str)
    else:
        formatter = logging.Formatter(format_str)

    # create log handler for console output
    lh_console = logging.StreamHandler(sys.stderr)
    if verbose:
        lh_console.setLevel(logging.DEBUG)
    else:
        lh_console.setLevel(logging.INFO)
    lh_console.setFormatter(formatter)

    root_log.addHandler(lh_console)


# =============================================================================
class CountryTestcase(unittest.TestCase):

    # -------------------------------------------------------------------------
    def __init__(self, methodName='runTest', verbose=0):

        self._verbose = int(verbose)

        super(CountryTestcase, self).__init__(methodName)

    # -------------------------------------------------------------------------
    @property
    def verbose(self):
        """The verbosity level."""
        return getattr(self, '_verbose', 0)

    # -------------------------------------------------------------------------
    def setUp(self):

        pass

    # -------------------------------------------------------------------------
    def tearDown(self):

        pass

    # -------------------------------------------------------------------------
    def test_import(self):

        log.info("Testing import of geo_countries ...")
        import geo_countries                                            # noqa



# =============================================================================

if __name__ == '__main__':

    verbose = get_arg_verbose()
    if verbose is None:
        verbose = 0
    init_root_logger(verbose)

    log.info("Starting tests ...")

    suite = unittest.TestSuite()

    suite.addTest(CountryTestcase('test_import', verbose))

    runner = unittest.TextTestRunner(verbosity=verbose)

    result = runner.run(suite)


# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
