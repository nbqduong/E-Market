from conan import ConanFile
from conan.tools.cmake import cmake_layout


class ExampleRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def build(self):
        self.settings.compiler.cppstd = "17"  # Or "20" depending on your project
        # Other build steps


    def requirements(self):
        self.requires("pybind11/2.13.6")
        self.requires("qt/6.7.3")

    def layout(self):
        cmake_layout(self)