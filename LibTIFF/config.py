{

	"downloads" : [

		"http://download.osgeo.org/libtiff/tiff-4.1.0.zip",

	],

	"license" : "COPYRIGHT",

	"dependencies" : [ "LibJPEG-Turbo" ],

	"environment" : {

		# Needed to make sure we link against the libjpeg
		# in the Gaffer distribution and not the system
		# libjpeg.
		"CPPFLAGS" : "-I{buildDir}/include",
		"LDFLAGS" : "-L{buildDir}/lib",

	},

	"commands" : [

		"./configure --without-x --prefix={buildDir}",
		"make -j {jobs}",
		"make install"

	],

	"manifest" : [

		"include/tiff*",
		"lib/libtiff*{sharedLibraryExtension}*",

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
