{

	"downloads" : [

		"https://github.com/alembic/alembic/archive/1.7.8.tar.gz"

	],

	"license" : "LICENSE.txt",

	"dependencies" : [ "Python", "OpenEXR", "Boost", "HDF5" ],

	"commands" : [

		"cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D Boost_NO_SYSTEM_PATHS=TRUE"
			" -D Boost_NO_BOOST_CMAKE=TRUE"
			" -D BOOST_ROOT={buildDir}"
			" -D ILMBASE_ROOT={buildDir}"
			" -D HDF5_ROOT={buildDir}"
			" -D ALEMBIC_PYILMBASE_INCLUDE_DIRECTORY={buildDir}/include/OpenEXR"
			" -D USE_HDF5=TRUE"
			" -D USE_ARNOLD=FALSE"
			" -D USE_PRMAN=FALSE"
			" -D USE_MAYA=FALSE"
			" ."
		,

		"make VERBOSE=1 -j {jobs}",
		"make install",

	],

	"manifest" : [

		"bin/abcconvert",
		"bin/abcecho",
		"bin/abcechobounds",
		"bin/abcls",
		"bin/abcstitcher",
		"bin/abctree",

		"include/Alembic",

		"lib/libAlembic*",

		"python/alembic*",

	],

	"platform:windows": {
		"commands": [
			"cmake -G \"Visual Studio 15 2017 Win64\""
			" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
			" -DCMAKE_PREFIX_PATH={buildDirWindows}"
			" -DBoost_NO_SYSTEM_PATHS=TRUE"
			" -DBoost_NO_BOOST_CMAKE=TRUE"
			" -DBOOST_ROOT={buildDirWindows}"
			" -DILMBASE_ROOT={buildDirWindows}"
			" -DHDF5_ROOT={buildDirWindows}"
			" -DALEMBIC_PYILMBASE_INCLUDE_DIRECTORY={buildDirWindows}/include/OpenEXR"
			" -DUSE_HDF5=TRUE"
			" -DUSE_ARNOLD=FALSE"
			" -DUSE_PRMAN=FALSE"
			" -DUSE_MAYA=FALSE"
			" .",

		"cmake --build . --config Release",
		"cmake --build . --config Release --target INSTALL",
		]
	}
}
