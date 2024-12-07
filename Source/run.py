import os
import shutil
import subprocess
import sys

def copy_pyd_files(src_dir, dest_dir):
    # Walk through all directories and files in the source directory
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".pyd"):
                # Construct full file path
                src_file = os.path.join(root, file)
                # Construct the destination file path
                dest_file = os.path.join(dest_dir, file)

                # Copy the file to the destination folder
                print(f"Copying {src_file} to {dest_file}")
                shutil.copy(src_file, dest_file)

def delete_build_folder(build_folder):
    """Deletes the build folder."""
    if os.path.exists(build_folder):
        print(f"Deleting the build folder: {build_folder}")
        shutil.rmtree(build_folder)
    else:
        print(f"Build folder does not exist: {build_folder}")

def setup_conan():
    """Runs the required Conan and CMake commands."""
    try:
        print("Running Conan install command...")
        subprocess.check_call(["conan", "install", ".", "-s", "build_type=Debug", "--build=missing"])

        print("Running CMake preset for debug...")
        subprocess.check_call(["cmake", "--preset", "conan-default"])

    except subprocess.CalledProcessError as e:
        print(f"Error during setup conan process: {e}")
        return False
    return True

def build_cmake():
    try:
        print("Building the project with CMake...")
        subprocess.check_call(["cmake", "--build", "--preset", "conan-debug"])
    except subprocess.CalledProcessError as e:
        print(f"Error during setup conan process: {e}")
        return False
    return True


def main():
    # Specify the source (build folder) and destination (Application folder) directories
    build_folder = "build"  # Replace with your build folder path
    application_folder = "Application"  # Replace with your application folder path
    # Check if argument is 'build all' or 'build'
    if len(sys.argv) > 1 and sys.argv[1] == 'build_all':
        # Delete the build folder and run all steps
        delete_build_folder(build_folder)
        if setup_conan():
            if  build_cmake():
                copy_pyd_files(build_folder, application_folder)
    elif len(sys.argv) > 1 and sys.argv[1] == 'build':
        # Just run the build step and copy .pyd files
        if build_cmake():
            copy_pyd_files(build_folder, application_folder)
    else:
        print("Invalid argument. Use 'build all' to perform all steps or 'build' to build the project.")

if __name__ == "__main__":
    main()