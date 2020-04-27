{

	"downloads" : [

		"https://github.com/Blosc/c-blosc/archive/1.15.1.tar.gz"

	],

	"license" : "LICENSES",

	"commands" : [

		"cmake -DCMAKE_INSTALL_PREFIX={buildDir} .",
		# Note : Blosc does not declare its build dependencies
		# correctly, so we cannot do a parallel build with `-j`.
		"make install VERBOSE=1",

	],

	"manifest" : [

		"include/blosc*.h",
		"lib/libblosc*{sharedLibraryExtension}*",

	],

	"platform:windows": {
		"commands": [
			"cmake -G \"Visual Studio 15 2017 Win64\""
			" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
			" -DCMAKE_PREFIX_PATH={buildDirWindows}"
			" .",

			"cmake --build . --config Release",
			"cmake --build . --config Release --target INSTALL"
		]
	}

}
