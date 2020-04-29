{

	"downloads" : [

		"https://github.com/GafferHQ/resources/archive/0.54.2.0.tar.gz"

	],

	"license" : None,

	"commands" : [

		"cp -r resources {buildDir}",

	],

	"manifest" : [

		"resources",

	],

	"platform:windows": {
		"commands": [
			"xcopy /y /E /q /I resources {buildDirWindows}\resources"
		]
	}

}
