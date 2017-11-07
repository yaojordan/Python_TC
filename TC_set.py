#python 3.4
import os
import sys
import shutil



def modify_ini(ini_file):
    with open(ini_file, 'r+') as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
                
            if line.startswith("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"):

                if sys.argv[1] == "TC315":
                    tmp = lines[i].strip() + "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                    lines[i] = tmp
                if sys.argv[1] == "TC348":
                    tmp = lines[i].strip() + "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
                    lines[i] = tmp
                if sys.argv[1] == "TC304":
                    lines[i] = lines[i].replace("false", "true")
    f.close()

    with open(ini_file, 'r+') as f:
        for line in lines:
            f.write(line)
    f.close()



try:
    modify_ini(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

except Exception as e:
    print(e)
    sys.exit(1)
