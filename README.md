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

## Examples
Search for ip 180.76.15.135

```
# ./weblog_helper.py --ip 180.76.15.135 --log-file public_access.log.txt
180.76.15.135 - - [02/Jun/2015:17:05:23 -0700] "GET /logs/access_140730.log HTTP/1.1" 200 979626 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"
180.76.15.135 - - [02/Jun/2015:19:50:23 -0700] "GET /War/?C=N;O=A HTTP/1.1" 200 733 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"
```

Search for subnet 180.76.15.0/24
 
```
# ./weblog_helper.py --ip 180.76.15.0/24 --log-file public_access.log.txt
180.76.15.135 - - [02/Jun/2015:17:05:23 -0700] "GET /logs/access_140730.log HTTP/1.1" 200 979626 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"
180.76.15.137 - - [02/Jun/2015:17:05:28 -0700] "GET /logs/access_140730.log HTTP/1.1" 200 7849856 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"
180.76.15.17 - - [02/Jun/2015:17:20:23 -0700] "GET /logs/access_141026.log HTTP/1.1" 200 45768 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"
180.76.15.20 - - [02/Jun/2015:17:23:05 -0700] "GET /logs/access_140817.log HTTP/1.1" 200 54711 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "redlug.com"
180.76.15.15 - - [02/Jun/2015:17:35:23 -0700] "GET /paperarticles/0302LowPay.htm HTTP/1.1" 200 1596 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"
180.76.15.146 - - [02/Jun/2015:17:50:23 -0700] "GET /Socialist/05MayGamaJH.htm HTTP/1.1" 200 5181 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"
180.76.15.27 - - [02/Jun/2015:18:05:23 -0700] "GET /Archive/SPArchives1969.htm HTTP/1.1" 200 905 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"
180.76.15.138 - - [02/Jun/2015:18:20:23 -0700] "GET /paper2004JD/0410AntiRac.htm HTTP/1.1" 200 1745 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"
...
```

Get also top 10 ip

```
# ./weblog_helper.py --ip 180.76.15.135 --log-file public_access.log.txt --top 10
180.76.15.135 - - [02/Jun/2015:17:05:23 -0700] "GET /logs/access_140730.log HTTP/1.1" 200 979626 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"
180.76.15.135 - - [02/Jun/2015:19:50:23 -0700] "GET /War/?C=N;O=A HTTP/1.1" 200 733 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"

--------- Top 10 IP ---------
78.29.246.2             6978
37.237.168.123          215
93.79.202.178           189
31.184.238.128          160
157.55.39.31            50
157.55.39.1             35
78.189.152.25           28
157.55.39.180           26
151.80.31.151           19
157.55.39.181           16
```

Run test suite

```
# ./weblog_helper.py --tests
test_no_ip_addr (test_log_parser.LogParserParametersTest) ... ok
test_no_log_file_name (test_log_parser.LogParserParametersTest) ... ok
test_wrong_ip_addr (test_log_parser.LogParserParametersTest) ... ok
test_wrong_log_file_name (test_log_parser.LogParserParametersTest) ... ok
test_found_ip_addr (test_log_parser.LogParserTest) ... ok
test_found_subnet_addr (test_log_parser.LogParserTest) ... ok
test_no_found_ip_addr (test_log_parser.LogParserTest) ... ok
test_no_found_subnet_addr (test_log_parser.LogParserTest) ... ok
test_top_10 (test_log_parser.LogParserTest) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.519s

OK
```
