#python 3.4
import os
import sys
import shutil



def modify_ini(ini_file):
    with open(ini_file, 'r+') as f:
        lines = f.readlines()

        for i, line in enumerate(lines):

            if line.startswith("-DVERSION=") and sys.argv[1] == "TC207":
                lines.remove(line)
                lines.insert(12, "-DVERSION=AutoTesting\n" )

            if line.startswith("-DENABLE_GDB_INDEX_ELF="):
                if sys.argv[1] == "TC304":
                    lines[i] = lines[i].replace("false", "true")
                elif sys.argv[1] == "TC315":
                    tmp = lines[i].strip() + "\n-DENABLE_DEFAULT_WATCH_ADDRESS_COLUMN=false\n"
                    lines[i] = tmp
                elif sys.argv[1] == "TC348":
                    tmp = lines[i].strip() + "\n-DHIDE_PREFERENCE_PAGES=Workspaces\n"
                    lines[i] = tmp
                elif sys.argv[1] == "TC361":
                    tmp = lines[i].strip() + "\n-DPROMPT_NEW_DISASSEMBLY_VIEW=true\n"
                    lines[i] = tmp
                elif sys.argv[1] == "TC361":
                    tmp = lines[i].strip() + "\n-DPROMPT_NEW_DISASSEMBLY_VIEW=true\n"
                    lines[i] = tmp
                elif sys.argv[1] == "TC365":
                    tmp = lines[i].strip() + "\n-DPRESERVE_SYMBOLS=true\n"
                    lines[i] = tmp
                elif sys.argv[1] == "TC315":
                    tmp = lines[i].strp() + "\n-DENABLE_DEFAULT_WATCH_ADDRESS_COLUMN=false\n"
                    lines[i] = tmp
    f.close()

    with open(ini_file, 'r+') as f:
        for line in lines:
            f.write(line)
    f.close()



try:
    modify_ini(r'C:\Users\vend_dt076\Desktop\Test\CoreTracer.ini')

except Exception as e:
    print(e)
    sys.exit(1)
