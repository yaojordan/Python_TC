#python 2.7
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
				
			if line.startswith("-DENABLE_GDB_INDEX_ELF=") and sys.argv[1] == "TC304":
				lines[i] = lines[i].replace("false", "true")
				
			#if line.startswith("-DPRESERVE_SYMBOLS="):
			if line.startswith("-DENABLE_GDB_INDEX_ELF="):	
				if sys.argv[1] == "TC315":
					tmp = lines[i].strip() + "\n-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=false\n"
					lines[i] = tmp
				elif sys.argv[1] == "TC348":
					tmp = lines[i].strip() + "\n-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=Workspaces\n"
					lines[i] = tmp
				elif sys.argv[1] == "TC206":
					tmp = lines[i].strip() + "\n-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=http://xxx/checker.php\n"
					lines[i] = tmp
				elif sys.argv[1] == "TC258":
					tmp = lines[i].strip() + "\n-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
					lines[i] = tmp
				elif sys.argv[1] == "TC257":
					tmp = lines[i].strip() + "\n-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
					lines[i] = tmp

				
	f.close()
	
	with open(ini_file, 'r+') as f:
		for line in lines:
			f.write(line)
	f.close()

try:
	modify_ini(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
	
except Exception as e:
	print e
	sys.exit(1)
