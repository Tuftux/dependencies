{

	"downloads" : [

		"https://github.com/OpenImageIO/oiio/archive/Release-1.8.12.tar.gz"

	],

	"license" : "LICENSE",

	"dependencies" : [ "Boost", "Python", "OpenEXR", "LibTIFF", "LibPNG", "LibJPEG-Turbo", "OpenColorIO" ],

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D USE_FFMPEG=NO"
			" -D USE_PYTHON=NO"
			# These next two disable `iv`. This fails to
			# build on Mac due to OpenGL deprecations, and
			# we've never packaged it anyway.
			" -D USE_OPENGL=NO"
			" -D USE_QT=NO"
			" ..",
		"cd gafferBuild && make install -j {jobs} VERBOSE=1",
		"cp {buildDir}/share/doc/OpenImageIO/openimageio.pdf {buildDir}/doc",

	],

	"manifest" : [

		"bin/maketx",
		"bin/oiiotool",

		"include/OpenImageIO",
		"lib/libOpenImageIO*{sharedLibraryExtension}*",

		"doc/openimageio.pdf",

	],

	"platform:windows": {
		"commands": [
			"if not exist gafferBuild mkdir gafferBuild",
			"cd gafferBuild &&"
				" cmake -G \"Visual Studio 15 2017 Win64\""
				" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
				" -DCMAKE_INSTALL_LIBDIR={buildDirWindows}\\lib"
				" -DCMAKE_PREFIX_PATH={buildDirWindows}"
				" -DUSE_FFMPEG=NO"
				" -DUSE_PYTHON=NO"
				# These next two disable `iv`. This fails to
				# build on Mac due to OpenGL deprecations, and
				# we've never packaged it anyway.
				" -DUSE_OPENGL=NO"
				" -DUSE_QT=NO"
				" ..",

			"cd gafferBuild && cmake --build . --config Release",
			"cd gafferBuild && cmake --build . --config Release --target INSTALL",

			"copy {buildDirWindows}\\share\\doc\\OpenImageIO\\openimageio.pdf {buildDirWindows}\\doc\\"
		]
	}
}
