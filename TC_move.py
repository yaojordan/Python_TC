#TC258
import os
import sys
import shutil




try:
	while os.path.isdir(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'):
	
		#TC258
		if sys.argv[1] == "TC258start":
			shutil.move(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\msys')
			sys.exit(0)
		
		if sys.argv[1] == "TC258done":
			shutil.move(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\config')
			sys.exit(0)
		
		#TC264		
		if sys.argv[1] == "TC264start":
			shutil.copytree(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\TemplateLaunches', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXTemplateLaunches')
			sys.exit(0)
			
		if sys.argv[1] == "TC264done":
			shutil.rmtree(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\TemplateLaunches')
			sys.exit(0)
		
		#TC187
		if sys.argv[1] == "TC187start":
			shutil.copy(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
			sys.exit(0)
			
		if sys.argv[1] == "TC187done":
			shutil.copy(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
			sys.exit(0)
			
		#TC257
		if sys.argv[1] == "TC257start":

			shutil.move(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
			shutil.copy(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
			sys.exit(0)
			
			
		if sys.argv[1] == "TC257done":
			shutil.copy(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
			shutil.move(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', )
			sys.exit(0)

		#TC334
		if sys.argv[1] == "TC334start":
			shutil.copy(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
			sys.exit(0)
			
		if sys.argv[1] == "TC334done":
			shutil.copy(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
			sys.exit(0)
		
		if sys.argv[1] == "TC190":
		
			if os.path.exists(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXCoverage'):
				sys.exit(0)
			else:
				shutil.copytree(rXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXoverage', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXCoverage')
			
			if os.path.exists(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXRegister'):
				sys.exit(0)
			else:
				shutil.copytree(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXRegister', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXRegister')
				
			if os.path.exists(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtOption'):
				sys.exit(0)
			else:
				shutil.copytree(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOption', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOption')
				
			if os.path.exists(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXarm'):
				sys.exit(0)
			else:
				shutil.copytree(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXarm', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXarm')			

			if os.path.exists(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXarm'):
				sys.exit(0)
			else:
				shutil.copytree(r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXarm', r'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXarm')
						
		#if sys.argv[1] == "TC267start":
		#	shutil.copy()
		#	sys.exit(0)
		
		#if sys.argv[1] == "TC267done":
		#	shutil.remove()
		#	sys.exit(0)
		
except Exception as e:
	print e
	sys.exit(1)
