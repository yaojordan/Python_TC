#python 2.7
import os
import sys
import shutil



def delete(ini_file):
    with open(ini_file, 'r+') as f:
        lines = f.readlines()#read all lines
        lines.pop()#Delete last line
    f.close()

    with open(ini_file, 'w') as f:
        #print(lines)
        f.writelines(lines)
    f.close()

try:
    delete(r'D:\tools\CoreTracer_x86\CoreTracer.ini')

except Exception as e:
    print e
    sys.exit(1)
