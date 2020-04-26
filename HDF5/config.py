{

	"downloads" : [

		"https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.20/src/hdf5-1.8.20.tar.gz"

	],

	"license" : "COPYING",

	"commands" : [

		"./configure --prefix={buildDir} --enable-threadsafe --disable-hl --with-pthread=/usr/include",

		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"lib/libhdf5*{sharedLibraryExtension}*",

	],

	"platform:windows": {
		"commands": [
			"if not exist \"build\" md build",
			"cd build && cmake -G \"Visual Studio 15 2017 Win64\""
			" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
			" -DCMAKE_PREFIX_PATH={buildDirWindows}"
			" -DBUILD_TESTING=OFF"
			" -DBUILD_SHARED_LIBS:BOOL=ON"
			" -DHDF5_BUILD_TOOLS=OFF"
			" -DHDF5_BUILD_EXAMPLES=OFF"
			" -DHDF5_ENABLE_THREADSAFE:BOOL=ON"
			" ..",

			"cd build && cmake --build . --config Release",
			"cd build && cmake --build . --config Release --target INSTALL"
		]
	}

}
