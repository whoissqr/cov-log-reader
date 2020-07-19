import re
#import pandas as pd

cov_log_default = r"D:\SNPS\Python_ex\cov-log-reader\idir\build-log.txt"

str_to_search = ["cov-build ", \
    "Dumping from hostname : ", \
    "Platform info:", \
    "cov-build command:", \
    "Configuration read from: command", \
    "Configuration read from:", \
    "Build time (cov-build overall):", \
    "compilation units"];


def read_log_parse_1(cov_log):
    search_index=0;
    with open(cov_log,'r') as file:
        line = file.readline()
        while line.strip():
            
            m = re.search(re.escape(str_to_search[search_index])+'(.+?)\n', line);
            if m:
                if(search_index<7):
                    print(m.group(1).strip())
                    search_index=search_index+1;
                else:
                    print(line);
            line = file.readline()
            if(search_index==len(str_to_search)): break;
            #print(line)

read_log_parse_1(cov_log_default);
