{

	"downloads" : [

		"https://www.openssl.org/source/openssl-1.1.1g.tar.gz",

	],

	"license" : "LICENSE",

	"commands" : [

		"./config --prefix={buildDir} -fPIC",
		"make -j {jobs}",
		"make install",

	],

	"platform:osx" : {

		"environment" : {

			"KERNEL_BITS" : "64",

		},

	},

	"platform:windows": {

		"commands": [
			"perl ./Configure VC-WIN64A no-asm --prefix={buildDir} --openssldir={buildDir}",
			"nmake -f makefile",
			"nmake -f makefile install"
		],

	},

}
