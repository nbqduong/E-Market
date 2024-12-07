import os
import shutil
import subprocess
import sys
import platform


def copy_pyd_files(src_dir, dest_dir):
    print("Copying link files from %s to %s" % (src_dir, dest_dir))
    # Check the operating system to determine the file type (.pyd for Windows, .so for Linux)
    file_extension = '.pyd' if platform.system() == 'Windows' else '.so' if platform.system() == 'Linux' else None
    if not file_extension:
        print("Unsupported operating system")
        return

    # Walk through all directories and files in the source directory
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(file_extension):
                # Construct full file path
                src_file = os.path.join(root, file)
                # Construct the destination file path
                dest_file = os.path.join(dest_dir, file)

                # Copy the file to the destination folder
                print(f"Copying {src_file} to {dest_file}")
                shutil.copy(src_file, dest_file)


def delete_build_folder(build_folder):
    """Deletes the build folder and removes CMakeUserPresets.json if it exists."""
    cmake_presets_file = "CMakeUserPresets.json"

    # Delete the build folder
    if os.path.exists(build_folder):
        print(f"Deleting the build folder: {build_folder}")
        shutil.rmtree(build_folder)
    else:
        print(f"Build folder does not exist: {build_folder}")

    # Delete CMakeUserPresets.json if it exists
    if os.path.exists(cmake_presets_file):
        print(f"Deleting {cmake_presets_file}")
        os.remove(cmake_presets_file)
    else:
        print(f"{cmake_presets_file} does not exist.")


def setup_conan(core_dir):
    """Runs the required Conan and CMake commands."""
    try:
         # Determine the platform and set the appropriate preset
        cmake_preset = "conan-default" if platform.system() == 'Windows' else "conan-debug"

        print("Running Conan install command...")
        subprocess.check_call(
            ["conan", "install", ".", "-s", "build_type=Debug", "--build=missing"],
            cwd=core_dir
        )

        print(f"Running CMake preset for {cmake_preset}...")
        subprocess.check_call(
            ["cmake", "--preset", cmake_preset],
            cwd=core_dir
        )

    except subprocess.CalledProcessError as e:
        print(f"Error during setup conan process: {e}")
        return False
    return True


def build_cmake(core_dir):
    """Builds the project with CMake."""
    try:
        print("Building the project with CMake...")
        subprocess.check_call(
            ["cmake", "--build", "--preset", "conan-debug"],
            cwd=core_dir
        )
    except subprocess.CalledProcessError as e:
        print(f"Error during setup build CMake process: {e}")
        return False
    return True


def main():
    # Set the Core directory dynamically relative to the script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    core_dir = os.path.join(script_dir, "Core")
    build_folder = os.path.join(core_dir, "build")
    application_folder = os.path.join(script_dir, "Application")

    # Check if argument is 'build all' or 'build'
    if len(sys.argv) > 1 and sys.argv[1] == 'build_all':
        # Delete the build folder and run all steps
        delete_build_folder(build_folder)
        if setup_conan(core_dir):
            if build_cmake(core_dir):
                copy_pyd_files(build_folder, application_folder)
    elif len(sys.argv) > 1 and sys.argv[1] == 'build':
        # Just run the build step and copy .pyd files
        if build_cmake(core_dir):
            copy_pyd_files(build_folder, application_folder)
    else:
        print("Invalid argument. Use 'build all' to perform all steps or 'build' to build the project.")


if __name__ == "__main__":
    main()
