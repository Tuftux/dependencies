{

	"downloads" : [

		"https://github.com/imageworks/OpenShadingLanguage/archive/Release-1.10.9.tar.gz"

	],

	"license" : "LICENSE",

	"dependencies" : [ "OpenImageIO", "LLVM" , "Zlib" , "FreeType" ],

	"environment" : {

		# Needed because the build process runs oslc, which
		# needs to link to the OIIO libraries.
		"DYLD_FALLBACK_LIBRARY_PATH" : "{buildDir}/lib",
		"LD_LIBRARY_PATH" : "{buildDir}/lib"
	},

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D STOP_ON_WARNING=0"
			" -D ENABLERTTI=1"
			" -D LLVM_STATIC=1"
			" ..",
		"cd gafferBuild && make install -j {jobs} VERBOSE=1",
		"cp {buildDir}/share/doc/OSL/osl-languagespec.pdf {buildDir}/doc",

	],

	"manifest" : [

		"bin/oslc",
		"bin/oslinfo",
		"include/OSL",
		"lib/libosl*",
		"doc/osl*",
		"shaders",

	],

	"platform:windows": {
		"commands": [
			"if not exist gafferBuild mkdir gafferBuild",
			"cd gafferBuild &&"
				" cmake -G \"Visual Studio 15 2017 Win64\""
				" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
				" -DCMAKE_INSTALL_LIBDIR={buildDirWindows}/lib"
				" -DCMAKE_PREFIX_PATH={buildDirWindows}"
				" -DSTOP_ON_WARNING=0"
				" -DENABLERTTI=1"
				" -DLLVM_STATIC=1"
				" ..",
				
			"set PATH={buildDirWindows}\\bin;{buildDirWindows}\\lib;%CD%\\gafferBuild\\src\\liboslcomp\\Release;%PATH% && cd gafferBuild && cmake --build . --config Release",
			"set PATH={buildDirWindows}\\bin;{buildDirWindows}\\lib;%CD%\\gafferBuild\\src\\liboslcomp\\Release;%PATH% && cd gafferBuild && cmake --build . --config Release --target INSTALL",
			"copy {buildDirWindows}\\share\\doc\\OSL\\osl-languagespec.pdf {buildDirWindows}\\doc\\"
		]
	}
}
