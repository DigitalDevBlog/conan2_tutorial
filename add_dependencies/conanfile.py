from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.scm import Git
from conan.tools.build import check_max_cppstd, check_min_cppstd


class helloRecipe(ConanFile):
    name = "hello3"
    version = "1.2"

    generators = "CMakeDeps"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of hello package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def validate(self):
        check_min_cppstd(self, "11")
        check_max_cppstd(self, "17")

    def requirements(self):
        self.requires("fmt/8.1.1")

    def source(self):
        # Please, be aware that using the head of the branch instead of an immutable tag
        # or commit is not a good practice in general as the branch may change the contents
        #get(self, "https://github.com/conan-io/libhello/archive/refs/heads/main.zip",
        #    strip_root=True)
        git = Git(self)
        git.clone(url="https://github.com/conan-io/libhello.git", target=".")
        git.checkout("require_fmt")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["hello3"]
