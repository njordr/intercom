#!/usr/bin/env python3

import click
import ipaddress
import logging
import sys

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
@click.option('--log_file', help='Log File to parse', default=None)
@click.option('--top', help='"n" Top IP', default=0)
def main(ip, log_file, top):
    """Main function to parse web log file"""
    lp = LogParser(ip, log_file, top)
    try:
        lp.parse()
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    main()
