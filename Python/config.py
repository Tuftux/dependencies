{

	"publicVariables" : {

		"pythonIncludeDir" : "{buildDir}/include/python{pythonABIVersion}",
		"pythonLibDir" : "{buildDir}/lib",

	},

	"variants" : [ "2", "3" ],

	"license" : "LICENSE",

	"dependencies" : [ "OpenSSL" ],

	"commands" : [

		"./configure --prefix={buildDir} {libraryType} --enable-unicode=ucs4",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"bin/python",
		"bin/python*[0-9]",

		"include/python*",

		"lib/libpython*{sharedLibraryExtension}*",
		"lib/Python.framework*",
		"lib/python{pythonVersion}",

	],

	"variables" : {

		"libraryType" : "--enable-shared",

	},

	"variant:2" : {

		"downloads" : [

			"https://www.python.org/ftp/python/2.7.17/Python-2.7.17.tgz",

		],

		"publicVariables" : {

			"pythonVersion" : "2.7",
			"pythonABIVersion" : "2.7",
			"pythonMajorVersion" : "2",
			"pythonMinorVersion" : "7",

		},

	},

	"variant:3" : {

		"downloads" : [

			"https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz",

		],

		"publicVariables" : {

			"pythonVersion" : "3.7",
			# Python 3 unconditionally puts these infuriating "m" ABI suffixes on
			# everything. This is intended to allow different types of Python builds
			# to exist in the same place, but that's not a problem we have. The problem
			# we _do_ have is that a bunch of our projects get tripped up by these
			# suffixes. See : https://www.python.org/dev/peps/pep-3149.
			"pythonABIVersion" : "3.7m",
			"pythonMajorVersion" : "3",
			"pythonMinorVersion" : "7",

		},

		"symbolicLinks" : [

			( "{buildDir}/bin/python", "python3" ),

		],

	},

	"platform:osx" : {

		"variables" : {

			"libraryType" : "--enable-framework={buildDir}/lib",

		},

		"publicVariables" : {

			"pythonIncludeDir" : "{buildDir}/lib/Python.framework/Headers",
			"pythonLibDir" : "{buildDir}/lib/Python.framework/Versions/{pythonVersion}/lib",

		},

		"symbolicLinks" : [

			( "{buildDir}/bin/python", "../lib/Python.framework/Versions/Current/bin/python{pythonMajorVersion}" ),
			( "{buildDir}/bin/python{pythonMajorVersion}", "../lib/Python.framework/Versions/Current/bin/python{pythonMajorVersion}" ),
			( "{buildDir}/bin/python{pythonVersion}", "../lib/Python.framework/Versions/Current/bin/python{pythonVersion}" ),

		],

	},

	"platform:windows" : {
		"commands": [
			"xcopy /y /e ..\\..\\patches\\2.7.17",
			"CALL PCbuild\\build.bat -e -m -v -p=x64 \"/p:PlatformToolset=v140\"",
			"xcopy /y /E Include {buildDirWindows}\\include\\",
			"xcopy /y /E Lib {buildDirWindows}\\Lib\\",
			"for /r PCBuild\\amd64 %a in (*.dll) do xcopy /y /q \"%a\" {buildDirWindows}\\DLLs\\ /i",
			"for /r PCBuild\\amd64 %a in (*.pdb) do xcopy /y /q \"%a\" {buildDirWindows}\\DLLs\\ /i",
			"for /r PCBuild\\amd64 %a in (*.pyd) do xcopy /y /q \"%a\" {buildDirWindows}\\DLLs\\ /i",
			"for /r PCBuild\\amd64 %a in (*.lib) do xcopy /y /q \"%a\" {buildDirWindows}\\libs\\ /i",
			"for /r PCBuild\\amd64 %a in (*.exe) do xcopy /y /q \"%a\" {buildDirWindows}\\bin\\ /i",
			"copy PCBuild\\amd64\\python27.dll {buildDirWindows}\\python27.dll",
			"copy PC\\pyconfig.h {buildDirWindows}\\include\\pyconfig.h"
		]
	}

}
