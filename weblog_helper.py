#!/usr/bin/env python3

import click
import ipaddress
import logging
import sys
import unittest
import os

from weblog.log_parser import LogParser


handler_console = logging.StreamHandler()
formatter_base = logging.Formatter('%(asctime)s|%(levelname)s|%(name)s|%(module)s|%(lineno)s|%(message)s')
handler_console.setFormatter(formatter_base)
logger = logging.getLogger()
level = logging.INFO
logger.setLevel(level)
logger.addHandler(handler_console)


def parse_log(log_line):
    pass


@click.command()
@click.option('--ip', help='IP address to check', default=None)
@click.option('--log-file', help='Log File to parse', default=None)
@click.option('--top', help='Number of records to include in the top list', default=0)
@click.option('--tests/--no-tests', help='Run tests', default=False)
def main(ip, log_file, top, tests):
    """Main function to parse web log file"""
    if tests:
        suite = unittest.TestLoader().discover(os.path.dirname(__file__)+'/tests')
        # Run
        unittest.TextTestRunner(verbosity=2).run(suite)
        sys.exit()

    lp = LogParser(ip, log_file, top)
    matched_lines = None
    top_lines = None
    try:
        if top > 0:
            matched_lines, top_lines = lp.parse()
        else:
            matched_lines = lp.parse()
    except Exception as e:
        logger.error(e)

    if top > 0:
        if matched_lines is not None and top_lines is not None:
            lp.print_output(matched_lines, top_lines)
    else:
        if matched_lines is not None:
            lp.print_output(matched_lines)

if __name__ == '__main__':
    main()
