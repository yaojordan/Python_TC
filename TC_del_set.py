#python 2.7
import os
import sys
import shutil



def delete(ini_file):
	with open(ini_file, 'r+') as f:
		lines = f.readlines()#read all lines
		#print(lines)
		
		if sys.argv[1] == "TC304":
			for i, line in enumerate(lines):
				if line.startswith("-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX="):
					lines[i] = lines[i].replace("true", "false")
					lines.pop()
					
		elif sys.argv[1] == "TC315":
			for i, line in enumerate(lines):
				if line.startswith("-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=false"):
					lines[i] = lines[i].replace("-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=false", "")
					lines.pop()
					
		elif sys.argv[1] == "TC348":
			for i, line in enumerate(lines):
				if line.startswith("-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=Workspaces"):
					lines[i] = lines[i].replace("-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=Workspaces", "")
					lines.pop()
					
		elif sys.argv[1] == "TC206":
			for i, line in enumerate(lines):
				if line.startswith("-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXp"):
					lines[i] = lines[i].replace("-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "")
					lines.pop()
					
		elif sys.argv[1] == "TC258":
			for i, line in enumerate(lines):
				if line.startswith("-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"):
					lines[i] = lines[i].replace("-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "")
					lines.pop()
					
		elif sys.argv[1] == "TC257":
			for i, line in enumerate(lines):
				if line.startswith("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"):
					lines[i] = lines[i].replace("-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "")
					lines.pop()					
		
		else:
			lines.pop()#Delete last line
			
	f.close()

	with open(ini_file, 'w') as f:
		#print(lines)
		f.writelines(lines)
	f.close()

try:
	delete(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

except Exception as e:
	print e
	sys.exit(1)
