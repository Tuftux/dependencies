{

	"downloads" : [

		"https://ftp.gnome.org/pub/GNOME/sources/ttf-bitstream-vera/1.10/ttf-bitstream-vera-1.10.tar.gz"
	],

	"license" : "COPYRIGHT.TXT",

	"commands" : [

		"mkdir -p {buildDir}/fonts",
		"cp *.ttf {buildDir}/fonts"

	],

	"manifest" : [

		"fonts",

	],

	"platform:windows": {
		"commands": [
			"if not exist {buildDirWindows}\\fonts mkdir {buildDirWindows}\\fonts",
			"copy *.ttf {buildDirWindows}\\fonts\\"
		]
	}

}
