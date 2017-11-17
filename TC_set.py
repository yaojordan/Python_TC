#python 3.4
import os
import sys
import shutil



def modify_ini(ini_file):
    with open(ini_file, 'r+') as f:
        lines = f.readlines()

        for i, line in enumerate(lines):

            if line.startswith("-XXX=") and sys.argv[1] == "TC207":
                lines.remove(line)
                lines.insert(12, "-XXX=XXX\n" )

            if line.startswith("-XXX=") and sys.argv[1] == "TC304":
                lines[i] = lines[i].replace("false", "true")

            if line.startswith("-XXX="):

                if sys.argv[1] == "TC315":
                    tmp = lines[i].strip() + "\n-XXX=false\n"
                    lines[i] = tmp
                elif sys.argv[1] == "TC348":
                    tmp = lines[i].strip() + "\n-XXX=XXX\n"
                    lines[i] = tmp
                elif sys.argv[1] == "TC206":
                    tmp = lines[i].strip() + "\n-XXX=http://xxx/checker.php\n"
                    lines[i] = tmp
                #elif sys.argv[1] == "TC365":
                #    tmp = lines[i].strip() + "\n-DPRESERVE_SYMBOLS=true\n"
                #    lines[i] = tmp
    f.close()

    with open(ini_file, 'r+') as f:
        for line in lines:
            f.write(line)
    f.close()



try:
    modify_ini(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXX')

except Exception as e:
    print(e)
    sys.exit(1)
