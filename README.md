[![](https://img.shields.io/badge/license-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)

connectivity_test
=================

`connectivity_test`_ tests connectivity to a given host and port within a given timeout period.

### Installation
```bash
$ pip install connectivity_test
```

### Examples
Simple usage
```python
>>> from connectivity_test import connectivity_test
>>> connectivity_test("www.google.com",443,5)
True
```

Usage when importing the entire module
```python
>>> import connectivity_test
>>> connectivity_test.connectivity_test("www.google.com",443,5)
True
```

With variables explained
```python
>>> connectivity_test(host="www.google.com",port=443,timeout=30)
```

Usage as main (standalone script) - Use connectivity_test.py directly
```bash
$ python3 connectivity_test --help
Usage: python3 connectivity_test.py [option1] arg1 [option2] arg2 ...

Tests connectivity to a given host/ip and port based on options specified. If
no options are specified then options marked with (default) will be used.

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -i HOST, --host=HOST  Hostname or ip address: www.google.com (default)
  -p PORT, --port=PORT  Port number: 443 (default)
  -t TIMEOUT, --timeout=TIMEOUT
                        Timeout in seconds: 5 (default)

Created by Taahirj to hopefully make things easier when testing connectivity
where tools like telnet are not available.
```

