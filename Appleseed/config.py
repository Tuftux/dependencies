{

	"downloads" : [

		"https://github.com/appleseedhq/appleseed/archive/2.1.0-beta.tar.gz"

	],

	"license" : "LICENSE.txt",

	"dependencies" : [ "Python", "Xerces", "OpenShadingLanguage", "OpenImageIO", "Boost", "LibPNG", "OpenEXR" , "LZ4"],

	"environment" : {

		# Needed so that `oslc` can be run to compile
		# shaders during the build.
		"DYLD_FALLBACK_LIBRARY_PATH" : "{buildDir}/lib",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",
		"PATH": "{buildDirWindows}\\bin;{buildDirWindows}\\lib;%PATH%",
		# Appleseed embeds minizip, which appears to require a later version
		# of zlib than CentOS 6 provides. These defines disable encryption,
		# which isn't needed anyway, and fixes the problem.
		# See https://github.com/appleseedhq/appleseed/issues/1597.
		"CFLAGS" : "-DNOCRYPT -DNOUNCRYPT",

	},

	"commands" : [

		"mkdir build",

		"cd build &&"
			" cmake"
			" -D WITH_CLI=ON"
			" -D WITH_STUDIO=OFF"
			" -D WITH_TOOLS=OFF"
			" -D WITH_TESTS=OFF"
			" -D WITH_SAMPLES=OFF"
			" -D WITH_DOXYGEN=OFF"
			" -D WITH_PYTHON=ON"
			" -D WITH_PYTHON2_BINDINGS={withPython2Bindings}"
			" -D WITH_PYTHON3_BINDINGS={withPython3Bindings}"
			" -D USE_STATIC_BOOST=OFF"
			" -D USE_STATIC_OIIO=OFF"
			" -D USE_STATIC_OSL=OFF"
			" -D USE_EXTERNAL_ZLIB=ON"
			" -D USE_EXTERNAL_EXR=ON"
			" -D USE_EXTERNAL_PNG=ON"
			" -D USE_EXTERNAL_XERCES=ON"
			" -D USE_EXTERNAL_OSL=ON"
			" -D USE_EXTERNAL_OIIO=ON"
			" -D USE_SSE=ON"
			" -D WARNINGS_AS_ERRORS=OFF"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D CMAKE_INSTALL_PREFIX={buildDir}/appleseed"
			" -D PYTHON_INCLUDE_DIR={pythonIncludeDir}"
			" -D Boost_PYTHON_LIBRARY_RELEASE={buildDir}/lib/libboost_python{pythonMajorVersion}{pythonMinorVersion}{sharedLibraryExtension}"
			" ..",

		"cd build && make install -j {jobs} VERBOSE=1"

	],

	"variant:Python:2" : {

		"variables" : {

			"withPython2Bindings" : "ON",
			"withPython3Bindings" : "OFF",

		},

	},

	"variant:Python:3" : {

		"variables" : {

			"withPython2Bindings" : "OFF",
			"withPython3Bindings" : "ON",

		},

	},

	"manifest" : [

		"appleseed/bin/appleseed.cli",
		"appleseed/include",
		"appleseed/lib",
		"appleseed/samples",
		"appleseed/schemas",
		"appleseed/settings",
		"appleseed/shaders",

	],

	"platform:windows": {
		"commands": [
			"xcopy /y /e ..\\..\\patches\\2.1.0",
			"if not exist build mkdir build",

			"cd build &&"
				" cmake -G \"Visual Studio 15 2017 Win64\""
				" -DWITH_CLI=ON"
				" -DWITH_STUDIO=OFF"
				" -DWITH_TOOLS=OFF"
				" -DWITH_TESTS=OFF"
				" -DWITH_SAMPLES=OFF"
				" -DWITH_DOXYGEN=OFF"
				" -DWITH_PYTHON=ON"
				" -DWITH_PYTHON2_BINDINGS={withPython2Bindings}"
				" -DWITH_PYTHON3_BINDINGS={withPython3Bindings}"
				" -DUSE_STATIC_BOOST=OFF"
				" -DUSE_STATIC_OIIO=OFF"
				" -DUSE_STATIC_OSL=OFF"
				" -DUSE_STATIC_EXR=OFF"
				" -DUSE_FIND_PACKAGE_FOR_ZLIB=ON"
				" -DUSE_FIND_PACKAGE_FOR_EXR=ON"
				" -DUSE_FIND_PACKAGE_FOR_PNG=ON"
				" -DUSE_FIND_PACKAGE_FOR_XERCES=ON"
				" -DUSE_FIND_PACKAGE_FOR_OSL=ON"
				" -DUSE_FIND_PACKAGE_FOR_OIIO=ON"
				" -DUSE_FIND_PACKAGE_FOR_OCIO=ON"
				" -DUSE_FIND_PACKAGE_FOR_LZ4=ON"
				" -DUSE_SSE=ON"
				" -DWARNINGS_AS_ERRORS=OFF"
				" -DOPENEXR_ROOT={buildDirWindows}"
				" -DILMBASE_ROOT={buildDirWindows}"
				" -DXERCES_INCLUDE_DIR={buildDirWindows}"
				" -DXERCES_LIBRARY={buildDirWindows}\\lib\\xerces-c_3.lib"
				" -DLLVM_LIBS_DIR={buildDir}/lib"
				" -DCMAKE_PREFIX_PATH={buildDirWindows}"
				" -DCMAKE_INSTALL_PREFIX={buildDirWindows}\\appleseed"
				" -DPython_LIBRARY={buildDirWindows}\\libs\\python27.lib"
				" -DPython_INCLUDE_DIR={buildDirWindows}\\include"
				" -DPython_EXECUTABLE={buildDirWindows}\\python.exe"
				" -DBoost_PYTHON_LIBRARY_RELEASE={buildDirWindows}\\lib\\libboost_python{pythonMajorVersion}{pythonMinorVersion}{sharedLibraryExtension}"
				" ..",

			"cd build && cmake --build . --config Release",
			"cd build && cmake --build . --config Release --target INSTALL",
		]
	}
}
