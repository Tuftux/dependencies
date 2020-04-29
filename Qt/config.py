{

	"downloads" : [

		"http://download.qt.io/official_releases/qt/5.12/5.12.8/single/qt-everywhere-src-5.12.8.tar.xz"

	],

	"dependencies" : [ "LibPNG", "LibTIFF", "LibJPEG-Turbo", "FreeType" ],

	"license" : "LICENSE.LGPLv21",

	"environment" : {

		"PKG_CONFIG_PATH" : "{buildDir}/lib/pkgconfig",

	},

	"commands" : [

		"./configure"
			" -prefix {buildDir}"
			" -plugindir {buildDir}/qt/plugins"
			" -release"
			" -opensource -confirm-license"
			" -no-rpath"
			" -no-dbus"
			" -skip qtconnectivity"
			" -skip qtwebengine"
			" -skip qt3d"
			" -skip qtdeclarative"
			" -skip qtwebchannel"
			" -no-libudev"
			" -no-icu"
			" -qt-pcre"
			" -nomake examples"
			" -nomake tests"
			" {extraArgs}"
			" -I {buildDir}/include -I {buildDir}/include/freetype2"
			" -L {buildDir}/lib"
		,

		"make -j {jobs} && make install",

	],

	"manifest" : [

		"bin/moc",
		"bin/qmake",
		"bin/rcc",
		"bin/uic",

		"include/Qt*",

		"lib/libQt*",
		"lib/Qt*.framework",

		"mkspecs",
		"qt",
		"lib/cmake",

	],

	"platform:linux" : {

		"environment" : {

			"LD_LIBRARY_PATH" : "{buildDir}/lib",

		},

		"variables" : {

			"extraArgs" : "-qt-xcb",

		},

	},

	"platform:osx" : {

		"variables" : {

			"extraArgs" : "-no-freetype",

		},

	},

	"platform:windows" : {

		"downloads" : [

			"http://download.qt.io/official_releases/qt/5.12/5.12.8/single/qt-everywhere-src-5.12.8.zip"

		],

		"variables" : {

			"extraArgs" : "",

		},

		"environment" : {

			"PKG_CONFIG_PATH" : "{buildDirWindows}\\lib\\pkgconfig",
			"PATH": "{buildDirWindows}\\bin;%PATH%",
			"BUILD_DIR": "{buildDirWindows}"  # We need to store this as a environment variable or the command gets too long and the build fails.
		},

		"commands": [
			#"nmake distclean",
			" configure"
			" -prefix %BUILD_DIR%"
			" -plugindir %BUILD_DIR%\\qt\\plugins"
			" -mp"
			" -release"
			" -opensource -confirm-license"
			" -no-rpath"
			" -no-dbus"
			" -skip qtconnectivity"
			" -skip qtwebengine"
			" -skip qt3d"
			" -skip qtdeclarative"
			" -skip qtwebchannel"
			" -no-libudev"
			" -no-icu"
			" -qt-pcre"
			" -opengl desktop"
			" -nomake examples"
			" -nomake tests"
			" -I %BUILD_DIR%\\include -I %BUILD_DIR%\\include\\freetype2"
			" -L %BUILD_DIR%\\lib",

			"nmake",
			"nmake install"
		]

	},

}
