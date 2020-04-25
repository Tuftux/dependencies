{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/openexr/archive/v2.4.1.tar.gz"

	],

	"license" : "LICENSE.md",

	"dependencies" : [ "Python", "Boost" ],

	"environment" : {

		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			# OpenEXR's CMake setup uses GNUInstallDirs, which unhelpfully
			# puts the libraries in `lib64`. Coax them back.
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D Boost_NO_SYSTEM_PATHS=TRUE"
			" -D Boost_NO_BOOST_CMAKE=TRUE"
			" -D BOOST_ROOT={buildDir}"
			" -D Python_ROOT_DIR={buildDir}"
			" -D Python2_ROOT_DIR={buildDir}"
			" -D Python3_ROOT_DIR={buildDir}"
			"."
		,

		"make VERBOSE=1 -j {jobs}",
		"make install",

		"mkdir -p {buildDir}/python",
		"mv {pythonLibDir}/python{pythonVersion}/site-packages/iex.so {buildDir}/python",
		"mv {pythonLibDir}/python{pythonVersion}/site-packages/imath.so {buildDir}/python",

	],

	"manifest" : [

		"bin/exrheader",
		"include/OpenEXR",
		"lib/libIlmImf*{sharedLibraryExtension}*",
		"lib/libIex*{sharedLibraryExtension}*",
		"lib/libHalf*{sharedLibraryExtension}*",
		"lib/libIlmThread*{sharedLibraryExtension}*",
		"lib/libImath*{sharedLibraryExtension}*",
		"lib/libPyIex*{sharedLibraryExtension}*",
		"lib/libPyImath*{sharedLibraryExtension}*",

		"python/iex.{pythonSharedLibraryExtension}",
		"python/imath.{pythonSharedLibraryExtension}",

	],

	"platform:windows": {
		"commands": [
			"cmake -G \"Visual Studio 15 2017 Win64\""
			" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
			# OpenEXR's CMake setup uses GNUInstallDirs, which unhelpfully
			# puts the libraries in `lib64`. Coax them back.
			" -DCMAKE_INSTALL_LIBDIR={buildDirWindows}\\lib"
			" -DCMAKE_PREFIX_PATH={buildDirWindows}"
			" -DBoost_NO_SYSTEM_PATHS=TRUE"
			" -DBoost_NO_BOOST_CMAKE=TRUE"
			" -DBOOST_ROOT={buildDirWindows}"
			" -DPython_LIBRARY={buildDirWindows}\\libs\\python27.lib"
			" -DPython_INCLUDE_DIR={buildDirWindows}\\include"
			" -DPython2_EXECUTABLE={buildDirWindows}\\python.exe"
			" ."
		,

		"cmake --build . --config Release",
		"cmake --build . --config Release --target INSTALL",

		"mkdir -p {buildDir}/python",
		"mv {pythonLibDir}/python{pythonVersion}/site-packages/iex{pythonSharedLibraryExtension} {buildDir}/python",
		"mv {pythonLibDir}/python{pythonVersion}/site-packages/imath{pythonSharedLibraryExtension} {buildDir}/python",
		]
	}

}
