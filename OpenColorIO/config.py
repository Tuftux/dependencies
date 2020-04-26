{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/OpenColorIO/archive/v1.1.1.tar.gz",
		"https://github.com/imageworks/OpenColorIO-Configs/archive/v1.0_r2.tar.gz",

	],

	"license" : "LICENSE",

	"dependencies" : [ "Python" ],

	"environment" : {

		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"cmake"
		 	" -D CMAKE_INSTALL_PREFIX={buildDir}"
		 	" -D PYTHON={buildDir}/bin/python"
		 	# By default, OCIO will use tr1::shared_ptr. But Maya (2015 and 2016 at least)
			# ships with a libOpenColorIO built using boost::shared_ptr instead. We'd like
			# Gaffer's default packages to be useable in Maya, so we pass OCIO_USE_BOOST_PTR=1
			# to match Maya's build. Even though both Gaffer and Maya respect the VFXPlatform
			# 2016 by using OCIO 1.0.9, this is an example of where the platform is under
			# specified, and we must go the extra mile to get compatibility.
			" -D OCIO_USE_BOOST_PTR=1"
			" -D OCIO_BUILD_TRUELIGHT=OFF"
			" -D OCIO_BUILD_APPS=OFF"
			" -D OCIO_BUILD_NUKE=OFF"
			" .",

		"make clean && make -j {jobs} && make install",

		"mkdir -p {buildDir}/python",
		"mv {buildDir}/lib/python*/site-packages/PyOpenColorIO* {buildDir}/python",

		"mkdir -p {buildDir}/openColorIO",
		"cp ../OpenColorIO-Configs-1.0_r2/nuke-default/config.ocio {buildDir}/openColorIO",
		"cp -r ../OpenColorIO-Configs-1.0_r2/nuke-default/luts {buildDir}/openColorIO",

	],

	"manifest" : [

		"include/OpenColorIO",
		"lib/libOpenColorIO*{sharedLibraryExtension}*",
		"openColorIO",
		"python/PyOpenColorIO*",

	],

	"platform:windows": {
		"commands": [
			"cmake -G \"Visual Studio 15 2017 Win64\""
			" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
			" -DCMAKE_PREFIX_PATH={buildDirWindows}"
			" -DPython_LIBRARY={buildDirWindows}\\libs\\python27.lib"
			" -DPython_INCLUDE_DIR={buildDirWindows}\\include"
			" -DPython_EXECUTABLE={buildDirWindows}\\python.exe"
			" -DOCIO_USE_BOOST_PTR=1"
			" -DOCIO_BUILD_TRUELIGHT=OFF"
			" -DOCIO_BUILD_APPS=OFF"
			" -DOCIO_BUILD_NUKE=OFF"
			" .",

			"cmake --build . --config Release",
			"cmake --build . --config Release --target INSTALL",

			"if not exist {buildDirWindows}\\python md {buildDirWindows}\\python",
			"move {buildDirWindows}\\lib\\site-packages\\PyOpenColorIO{pythonSharedLibraryExtension} {buildDirWindows}\\python\\",

			"if not exist {buildDirWindows}\\openColorIO md {buildDirWindows}\\openColorIO",
			"copy ..\\OpenColorIO-Configs-1.0_r2\\nuke-default\\config.ocio {buildDirWindows}\\openColorIO",
			"copy ..\\OpenColorIO-Configs-1.0_r2\\nuke-default\\luts {buildDirWindows}\\openColorIO"
		]
	}
}
