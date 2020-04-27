{

	"downloads" : [

		"https://github.com/github/cmark/archive/0.28.3.gfm.12.tar.gz",

	],

	"license" : "COPYING",

	"commands" : [

		"mkdir build",
		"cd build && cmake -D CMAKE_INSTALL_PREFIX={buildDir} ..",
		"cd build && make -j {jobs} && make install",

	],

	"manifest" : [

		"lib/libcmark*{sharedLibraryExtension}*"

	],

	"platform:windows": {
		"commands": [
			"if not exist build mkdir build",
			"cd build && cmake -G \"Visual Studio 15 2017 Win64\""
			" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
			" -DCMAKE_PREFIX_PATH={buildDirWindows}"
			" ..",

			"cd build && cmake --build . --config Release",
			"cd build && cmake --build . --config Release --target INSTALL"
		]
	}
}
