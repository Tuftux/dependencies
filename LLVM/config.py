{

	"downloads" : [

		"https://github.com/llvm/llvm-project/releases/download/llvmorg-9.0.1/llvm-9.0.1.src.tar.xz",
		#"http://releases.llvm.org/5.0.1/cfe-5.0.1.src.tar.xz"

	],

	"license" : "LICENSE.TXT",

	"commands" : [

		"mv ../cfe* tools/clang",
		"mkdir build",
		"cd build &&"
			" cmake"
			" -DCMAKE_INSTALL_PREFIX={buildDir}"
			" -DCMAKE_BUILD_TYPE=Release"
			" -DLLVM_ENABLE_RTTI=ON"
			" ..",
		"cd build && make install -j {jobs}"

	],

	"platform:windows": {
		"commands": [
			#"move ..\\cfe* tools\\clang",
			"if not exist build mkdir build",
			"cd build &&"
				" cmake -G \"Visual Studio 15 2017 Win64\""
				" -DCMAKE_INSTALL_PREFIX={buildDirWindows}"
				" -DCMAKE_BUILD_TYPE=Release"
				" -DLLVM_ENABLE_RTTI=ON"
				" -DLLVM_TARGETS_TO_BUILD=\"X86\""
				" -DLLVM_ENABLE_EH=ON"
				" -DLLVM_TEMPORARILY_ALLOW_OLD_TOOLCHAIN=ON"
				" ..",

			"cd build && cmake --build . --config Release",
			"cd build && cmake --build . --config Release --target INSTALL",
		]
	}
}
