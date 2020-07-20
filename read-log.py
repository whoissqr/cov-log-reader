import re
import os
from collections import OrderedDict
import pprint

cwd = os.getcwd()
cov_log_default = cwd + r"/idir/build-log.txt"

str_to_search_dict = OrderedDict([
    ("cov-build ", "none"),
    ("Dumping from hostname : ", "none"),
    ("Platform info", "none"),
    ("cov-build command:", "none"),
    ("Configuration read from: command", "none"),
    ("Configuration read from:", "none"),
    ("Build time (cov-build overall):", "none"),
    ("compilation units", "")
    ])


def read_log_parse_1(cov_log):
    items = iter(str_to_search_dict)
    key_to_search = next(items)
    with open(cov_log, 'r') as file:
        line = file.readline()
        while line:
            m = re.search(re.escape(key_to_search)+'(.+?)\n', line)
            if m:
                if(key_to_search != "compilation units"):
                    str_to_search_dict[key_to_search] = m.group(1).strip()
                    key_to_search = next(items)
                else:
                    str_to_search_dict[key_to_search] += m.group(1).strip()
            line = file.readline()
    return str_to_search_dict


read_log_parse_1(cov_log_default)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(str_to_search_dict)
