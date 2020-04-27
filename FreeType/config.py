{

	"downloads" : [

		"https://download.savannah.gnu.org/releases/freetype/freetype-2.9.1.tar.gz",

	],

	"license" : "docs/FTL.TXT",

	"environment" : {

		"LDFLAGS" : "-L{buildDir}/lib",
		"PKG_CONFIG_PATH" : "{buildDir}/lib/pkgconfig",

	},

	"commands" : [

		"./configure --prefix={buildDir} --with-harfbuzz=no",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"include/freetype2",
		"lib/libfreetype*{sharedLibraryExtension}*",

	],

	"platform:windows": {
		"commands": [
			"if not exist build mkdir build",
			# Fix broken CMake install
			"copy include\\freetype\\config\\ build\\include\\freetype\\config\\",
			"cd build && cmake -G \"Visual Studio 15 2017 Win64\""
			" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
			" -DCMAKE_PREFIX_PATH={buildDirWindows}"
			" -DFT_WITH_HARFBUZZ=OFF"
			" ..",

			"cd build && cmake --build . --config Release",
			"cd build && cmake --build . --config Release --target INSTALL"
		]
	}

}
