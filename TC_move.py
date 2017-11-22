#TC258
import os
import sys
import shutil




try:
	while os.path.isdir(r'D:\tools\CoreTracer_x86'):
	
		#TC258
		if sys.argv[1] == "TC258start":
			shutil.move(r'D:\tools\Coretracer_x86\config\JythonLib', r'D:\tools\CoreTracer_x86\msys')
			sys.exit(0)
		
		if sys.argv[1] == "TC258done":
			shutil.move(r'D:\tools\CoreTracer_x86\msys\JythonLib', r'D:\tools\Coretracer_x86\config')
			sys.exit(0)
		
		#TC264		
		if sys.argv[1] == "TC264start":
			shutil.copytree(r'\\mtksdtwt02\package\DM7_MD32\elf_image\TemplateLaunches', r'D:\tools\Coretracer_x86\config\TemplateLaunches')
			sys.exit(0)
			
		if sys.argv[1] == "TC264done":
			shutil.rmtree(r'D:\tools\Coretracer_x86\config\TemplateLaunches')
			sys.exit(0)
		
		#TC187
		if sys.argv[1] == "TC187start":
			shutil.copy(r'D:\tools\tmp\TC_tmp\TC187\MD32_DM6_evb_jtag.debugger', r'D:\tools\Coretracer_x86\config\Target')
			sys.exit(0)
			
		if sys.argv[1] == "TC187done":
			shutil.copy(r'D:\tools\tmp\TC_tmp\TC187\origin\MD32_DM6_evb_jtag.debugger', r'D:\tools\Coretracer_x86\config\Target')
			sys.exit(0)
			
		#TC257
		if sys.argv[1] == "TC257start":

			shutil.move(r'D:\tools\Coretracer_x86\config\Target', r'D:\tools\CoreTracer_x86\msys')
			shutil.copy(r'D:\tools\tmp\TC_tmp\TC257\MD32_DM6_evb_jtag.debugger', r'D:\tools\Coretracer_x86\msys\Target')
			sys.exit(0)
			
			
		if sys.argv[1] == "TC257done":
			shutil.copy(r'D:\tools\tmp\TC_tmp\TC257\origin\MD32_DM6_evb_jtag.debugger', r'D:\tools\Coretracer_x86\msys\Target')
			shutil.move(r'D:\tools\CoreTracer_x86\msys\Target', r'D:\tools\Coretracer_x86\config', )
			sys.exit(0)

		#TC334
		if sys.argv[1] == "TC334start":
			shutil.copy(r'D:\tools\tmp\TC_tmp\TC334\MD32_md32s.cpureg', r'D:\tools\CoreTracer_x86\config\CPURegister')
			sys.exit(0)
			
		if sys.argv[1] == "TC334done":
			shutil.copy(r'D:\tools\tmp\TC_tmp\TC334\origin\MD32_md32s.cpureg', r'D:\tools\CoreTracer_x86\config\CPURegister')
			sys.exit(0)
		
			
		#if sys.argv[1] == "TC267start":
		#	shutil.copy()
		#	sys.exit(0)
		
		#if sys.argv[1] == "TC267done":
		#	shutil.remove()
		#	sys.exit(0)
		
except Exception as e:
	print e
	sys.exit(1)