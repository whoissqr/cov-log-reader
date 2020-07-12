import re
import pandas as pd

cov_log = r"D:\SNPS\ws\python-cloud\test-lark\idir\build-log.txt"

with open(cov_log,'r') as file:
    line = file.readline()
    while line.strip():
        m = re.search('Dumping from hostname : (.+?)\n', line);
        if m:
            print("Host Name: " +m.group(1))

        m = re.search("Platform info: (.+?)\n", line);
        if m:
            print("OS:        " + m.group(1))

        m= re.search("cov-build command:(.+?)\n", line);

        if m:
            print("cov-build CMD: "+ m.group(1))

        line = file.readline()
        #print(line)

