import re
import pandas as pd

cov_log = r"D:\SNPS\Python_ex\cov-log-reader\idir\build-log.txt"
str_to_search = ["cov-build ", "Dumping from hostname : ", "Platform info:", "cov-build command:", "Build time (cov-build overall):"];
search_index=0;

with open(cov_log,'r') as file:
    line = file.readline()
    while line.strip():
        m = re.search(re.escape(str_to_search[search_index])+'(.+?)\n', line);
        if m:
            print(m.group(1).strip())
            search_index=search_index+1;
        line = file.readline()
        if(search_index==len(str_to_search)): break;
        #print(line)

