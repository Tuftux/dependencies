{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/openvdb/archive/v7.0.0.tar.gz"

	],

	"license" : "LICENSE",

	"dependencies" : [ "Blosc", "TBB", "OpenEXR", "Python" ],

	"environment" : {

		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"mkdir build",
		"cd build && cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			# OpenVDB's CMake setup uses GNUInstallDirs, which unhelpfully
			# puts the libraries in `lib64`. Coax them back.
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D OPENVDB_BUILD_PYTHON_MODULE=ON"
			" -D PYOPENVDB_INSTALL_DIRECTORY={buildDir}/python"
			" .."
		,

		"cd build && make VERBOSE=1 -j {jobs} && make install",

	],

	"manifest" : [

		"include/openvdb",
		"include/pyopenvdb.h",
		"lib/libopenvdb*{sharedLibraryExtension}*",
		"python/pyopenvdb*",

	],

	"platform:windows": {
		"commands": [
			"xcopy /y /e ..\\..\\patches\\7.0.0",

			"if not exist build mkdir build",
			"cd build && cmake -G \"Visual Studio 15 2017 Win64\""
			" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
			" -DCMAKE_PREFIX_PATH={buildDirWindows}"
			" -DPython_LIBRARY={buildDirWindows}\\libs\\python27.lib"
			" -DPython_INCLUDE_DIR={buildDirWindows}\\include"
			" -DPython_EXECUTABLE={buildDirWindows}\\python.exe"
			" -DCMAKE_INSTALL_LIBDIR={buildDirWindows}\\lib"
			" -DOPENVDB_BUILD_PYTHON_MODULE=ON"
			" -DPYOPENVDB_INSTALL_DIRECTORY={buildDirWindows}\\python"
			" -DTBB_ROOT={buildDirWindows}"
			" -DBLOSC_ROOT={buildDirWindows}"
			" ..",

			"cd build && cmake --build . --config Release",
			"cd build && cmake --build . --config Release --target INSTALL",
		]
	}

}
