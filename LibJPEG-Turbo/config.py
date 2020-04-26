{

	"downloads" : [

		"https://download.sourceforge.net/project/libjpeg-turbo/1.5.2/libjpeg-turbo-1.5.2.tar.gz",

	],

	"license" : "LICENSE.md",

	"commands" : [

		"./configure --prefix={buildDir}",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"include/jconfig.h",
		"include/jerror.h",
		"include/jmorecfg.h",
		"include/jpeglib.h",

		"lib/libjpeg*{sharedLibraryExtension}*",

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
