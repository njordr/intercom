# Web logs parser
This module parse a log file from a web server and search for a specified ip/subnet address. It could also display the top "n" ip addresses in the log file.

## Usage
```
Usage: weblog_helper.py [OPTIONS]

  Main function to parse web log file

Options:
  --ip TEXT             IP address to check
  --log-file TEXT       Log File to parse
  --top INTEGER         Number of records to include in the top list
  --tests / --no-tests  Run tests
  --help                Show this message and exit.
```
