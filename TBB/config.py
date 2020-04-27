{

	"downloads" : [

		"https://github.com/01org/tbb/archive/2018_U5.tar.gz"

	],

	"license" : "LICENSE",

	"commands" : [

		"make -j {jobs} stdver=c++11",
		"cp -r include/tbb {buildDir}/include",
		"{installLibsCommand}",

	],

	"manifest" : [

		"include/tbb",
		"lib/libtbb*{sharedLibraryExtension}*",

	],

	"platform:linux" : {

		"environment" : {

			"tbb_os" : "linux",

		},

		"variables" : {

			"installLibsCommand" : "cp build/*_release/*.so* {buildDir}/lib",

		},

	},

	"platform:osx" : {

		"environment" : {

			"tbb_os" : "macos",

		},

		"variables" : {

			"installLibsCommand" : "cp build/macos_*_release/*.dylib {buildDir}/lib",

		},

	},

	"platform:windows" : {

		"environment" : {

			"tbb_os" : "windows",

		},

		"commands": [
			"cd build\\vs2013 && devenv makefile.sln /upgrade",
			"cd build\\vs2013 && devenv makefile.sln /build \"Release|x64\" /project tbb",
			"cd build\\vs2013 && devenv makefile.sln /build \"Release|x64\" /project tbbmalloc",
			"cd build\\vs2013 && devenv makefile.sln /build \"Release|x64\" /project tbbmalloc_proxy",

			"if not exist {buildDirWindows}\\include\\tbb\\ mkdir {buildDirWindows}\\include\\tbb\\",
			"xcopy /y /E /q /I include\\tbb {buildDirWindows}\\include\\tbb\\",
			"copy build\\vs2013\\x64\\Release\\*.dll {buildDirWindows}\\lib",
			"copy build\\vs2013\\x64\\Release\\*.lib {buildDirWindows}\\lib"
		]

	},

}
