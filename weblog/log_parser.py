import re
import ipaddress
import logging

from collections import Counter

logger = logging.getLogger(__name__)


class LogParser:
    """Class to parse a log file and search for a specific ip/subnet address"""
    def __init__(self, ip, log_file, top):
        """ __init_
        Args:
            ip (str): ip to searching for
            log_file (str): log file name to parser
            top (int): number of records to include in the top list
        """
        self._ip_to_check = ip
        self._log_file = log_file
        self._top = top
        self._ip = None
        self._log_regex = re.compile(
            r'^(?P<ip_addr>^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[.*\] "(?P<method>[A-Z]{3,4}).*" (?P<status>[0-9]{3}).*'
        ).match
        self._matches = {
            'requested_ip': [],
        }
        self._top_ip = []
        self._output = []

    def _check_params(self):
        """ Check parameters for errors
        Raises:
            RuntimeError if an error occurs
        """
        if self._ip_to_check is None:
            raise RuntimeError('Please specify an ip/subnet for filtering')
        if self._log_file is None:
            raise RuntimeError('Please specify a log file')

        try:
            self._ip = ipaddress.ip_address(self._ip_to_check)
        except ValueError:
            pass
        except Exception as e:
            logger.error('Cannot parse {} as ip address. Error {}'.format(self._ip_to_check, e))
            raise RuntimeError

        if self._ip is None:
            try:
                self._ip = ipaddress.ip_network(self._ip_to_check)
            except ValueError:
                logger.error('IP {} is not a valid ip or subnet address'.format(self._ip_to_check))
                raise RuntimeError
            except Exception as e:
                logger.error('Cannot parse {} as subnet address. Error {}'.format(self._ip_to_check, e))
                raise RuntimeError

        try:
            with open(self._log_file, 'r') as f:
                pass
        except Exception as e:
            raise RuntimeError(e)

    def _filter_ip(self, matched_ip):
        """Check if the regex matched ip is equal to the ip address searched or if it's contained inside the subnet searched
        Args:
            matched_ip (str): IP address matched by log line regex

        Returns:
            True if equal/contained, False otherwise
        """
        try:
            log_ip = ipaddress.ip_address(matched_ip.strip())
        except Exception:
            logger.warning('Matched IP {} cannot be converted to IPv4Address class. Error: {}'.format(matched_ip, e))
            return False

        if isinstance(self._ip, ipaddress.IPv4Address):
            if self._ip == log_ip:
                return True
        else:
            if log_ip in self._ip:
                return True

        return False

    def _parse_line(self, line):
        """Apply filter to the current log line
        Args:
            line (str): current line of the log file
        """
        match = self._log_regex(line)
        if match is None:
            return

        try:
            matched_ip = match.group('ip_addr')
            if self._filter_ip(matched_ip):
                self._matches['requested_ip'].append(line)
            if self._top > 0:
                self._top_ip.append(matched_ip)
        except Exception:
            logger.debug('Cannot get ip address from log liune')

    def print_output(self, matched_lines, top=None):
        """Print matched lines and top ip if requested
        Args:
            matched_lines (list): list of lines that match the search pattern
            top (list): list of tuples for top ip
        """
        for k, v in self._matches.items():
            self._output.extend(v)

        for line in self._output:
            print(line.strip())

        if self._top > 0:
            print('\n--------- Top {} IP ---------'.format(self._top))
            for ip in Counter(self._top_ip).most_common(self._top):
                print('{}\t\t{}'.format(ip[0], ip[1]))

    def parse(self):
        """Main function to start log parsing
        Raises:
            RuntimeError if any error occurs during execution
        """
        try:
            self._check_params()
        except Exception as e:
            raise RuntimeError(e)

        with open(self._log_file, 'r') as f:
            for line in f:
                self._parse_line(line)

        if self._top > 0:
            return self._matches, Counter(self._top_ip).most_common(self._top)
        else:
            return self._matches

