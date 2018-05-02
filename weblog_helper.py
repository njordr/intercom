#!/usr/bin/env python3

import click
import ipaddress
import logging
import sys

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
@click.option('--ip', help='IP address to check')
@click.option('--log_file', help='Log File to parse')
def main(ip, log_file):
    """Main function to parse web log file"""
    ip_to_check = None
    try:
        ip_to_check = ipaddress.ip_address(ip)
    except ValueError:
        pass
    except Exception as e:
        logger.error('Cannot parse {} as ip address. Error {}'.format(ip, e))
        sys.exit(1)

    if ip_to_check is None:
        try:
            ip_to_check = ipaddress.ip_network(ip)
        except ValueError:
            logger.error('IP {} is not a valid ip or subnet address'.format(ip))
            sys.exit(1)
        except Exception as e:
            logger.error('Cannot parse {} as subnet address. Error {}'.format(ip, e))
            sys.exit(1)

    try:
        with open(log_file, 'r') as f:
            pass
    except Exception as e:
        logger.error('Cannot open file {}. Error: {}'.format(log_file, e))


if __name__ == '__main__':
    main()
