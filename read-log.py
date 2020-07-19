import re
from collections import OrderedDict
#import pandas as pd

cov_log_default = r"D:\SNPS\Python_ex\cov-log-reader\idir\build-log.txt"

str_to_search_dict = OrderedDict([
    ("cov-build ", "none"), \
    ("Dumping from hostname : ", "none"),  \
    ("Platform info:", "none"), \
    ("cov-build command:", "none"), \
    ("Configuration read from: command", "none"), \
    ("Configuration read from:", "none"), \
    ("Build time (cov-build overall):", "none"), \
    ("compilation units", "") \
    ]);


def read_log_parse_1(cov_log):
    items = iter(str_to_search_dict) 
    key_to_search= next(items)
    with open(cov_log,'r') as file:
        line = file.readline()
        while line.strip():
            m = re.search(re.escape(key_to_search)+'(.+?)\n', line);
            if m:
                if(key_to_search!="compilation units"):
                    #print(m.group(1).strip())
                    str_to_search_dict[key_to_search]=m.group(1).strip();
                    key_to_search= next(items)
                else:
                    print(line);
                    str_to_search_dict[key_to_search]=str_to_search_dict[key_to_search]+ m.group(1).strip();
            line = file.readline()
    return str_to_search_dict;

read_log_parse_1(cov_log_default);
