import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from weblog.log_parser import LogParser
from unittest import TestCase
from pprint import pprint


class LogParserParametersTest(TestCase):
    def test_no_ip_addr(self):
        lp = LogParser(None, None, 0)
        self.assertRaises(RuntimeError, lp.parse)

    def test_wrong_ip_addr(self):
        lp = LogParser('ewrwerwrw', None, 0)
        self.assertRaises(RuntimeError, lp.parse)

    def test_no_log_file_name(self):
        lp = LogParser('127.0.0.1', None, 0)
        self.assertRaises(RuntimeError, lp.parse)

    def test_wrong_log_file_name(self):
        lp = LogParser('127.0.0.1', 'dummy.log', 0)
        self.assertRaises(RuntimeError, lp.parse)


class LogParserTest(TestCase):
    def test_found_ip_addr(self):
        lp = LogParser('180.76.15.135', 'tests/public_access.log', 0)
        matched_lines = lp.parse()
        self.assertEqual(2, len(matched_lines['requested_ip']))

    def test_no_found_ip_addr(self):
        lp = LogParser('180.76.15.175', 'tests/public_access.log', 0)
        matched_lines = lp.parse()
        self.assertEqual(0, len(matched_lines['requested_ip']))

    def test_found_subnet_addr(self):
        lp = LogParser('180.76.15.0/24', 'tests/public_access.log', 0)
        matched_lines = lp.parse()
        self.assertEqual(37, len(matched_lines['requested_ip']))

    def test_no_found_subnet_addr(self):
        lp = LogParser('180.76.16.0/24', 'tests/public_access.log', 0)
        matched_lines = lp.parse()
        self.assertEqual(0, len(matched_lines['requested_ip']))

    def test_top_10(self):
        lp = LogParser('180.76.15.135', 'tests/public_access.log', 10)
        matched_lines, top_lines = lp.parse()
        # test the right number of lines in output
        self.assertEqual(10, len(top_lines))


if __name__ == '__main__':
    unittest.main()
