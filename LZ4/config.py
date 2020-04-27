{

	"downloads" : [

		"https://github.com/lz4/lz4/archive/v1.9.2.tar.gz"

	],

	"license" : "LICENSE",

	"commands" : [

		"./configure --prefix={buildDir}",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

	],

	"platform:windows": {
		"commands": [
			"cd contrib\\cmake_unofficial && cmake -G \"Visual Studio 15 2017 Win64\""
			" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
			" -DCMAKE_PREFIX_PATH={buildDirWindows}"
			" -DBUILD_STATIC_LIBS=ON"
			" .",

			"cd contrib\\cmake_unofficial && cmake --build . --config Release",
			"cd contrib\\cmake_unofficial && cmake --build . --config Release --target INSTALL",
		]
	}
}
