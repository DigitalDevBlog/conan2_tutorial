Each step requires entering the command on the command-line.
The steps were tested on MacOS Ventura 13.2.1.

The first step is to create a conan profile. A conan profile contains
the configuration set for things like compiler, build configuration, architecture,
shared or static libraries, etc.

```bash
conan profile detect --force
```

Next:
```bash
conan install . --output=build --build=missing
```

This will create an output folder named 'build'.
-- output: the output folder to be used/created
--build=missing: build packages from source whose binary package is not found.

On macOS:
```bash
cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release
cmake --build .
```

The conan_toolchain.cmake file was generated in the previous step and contains 
all the settings cmake needs to build the code.
