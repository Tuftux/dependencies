{

	"downloads" : [

		"https://download.sourceforge.net/libpng/libpng-1.6.3.tar.gz"

	],

	"license" : "LICENSE",

	"commands" : [

		"./configure --prefix={buildDir}",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"include/png*",
		"include/libpng*",
		"lib/libpng*{sharedLibraryExtension}*",

	],

	"platform:windows": {
		"commands": [
			"cmake -G \"Visual Studio 15 2017 Win64\""
			" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
			" -DCMAKE_PREFIX_PATH={buildDirWindows}"
			" .",

			"cmake --build . --config Release",
			"cmake --build . --config Release --target INSTALL",
		]
	}
}
