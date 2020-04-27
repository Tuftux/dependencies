{

	"downloads" : [

		"https://downloads.sourceforge.net/project/glew/glew/2.1.0/glew-2.1.0.tgz"

	],

	"license" : "LICENSE.txt",

	"commands" : [

		"mkdir -p {buildDir}/lib64/pkgconfig",
		"make clean && make -j {jobs} install GLEW_DEST={buildDir} LIBDIR={buildDir}/lib",

	],

	"manifest" : [

		"include/GL",
		"lib/libGLEW*{sharedLibraryExtension}*",

	],

	"platform:windows": {
		"commands": [
			"cd build\\cmake && cmake -G \"Visual Studio 15 2017 Win64\""
			" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
			" -DCMAKE_PREFIX_PATH={buildDirWindows}"
			" .",

			"cd build\\cmake && cmake --build . --config Release",
			"cd build\\cmake && cmake --build . --config Release --target INSTALL"
		]
	}
}

