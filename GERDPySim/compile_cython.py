import os
import glob
from setuptools import setup
from Cython.Build import cythonize

def compile_cython_files_in_directory(directory):
    """
    Compiles all Cython (.pyx) files in the specified directory.

    Args:
    - directory (str): The path to the directory containing .pyx files.
    """
    # Search for all .pyx files in the directory
    pyx_files = glob.glob(os.path.join(directory, "*.pyx"))

    for pyx_file in pyx_files:
        module_name = os.path.splitext(os.path.basename(pyx_file))[0]
        compile_cython_module(module_name, pyx_file)

def compile_cython_module(module_name, pyx_file):
    """
    Compiles a Cython module.

    Args:
    - module_name (str): The name of the module (without extension).
    - pyx_file (str): The path to the Cython .pyx file.
    """
    # Determine the correct extension based on the operating system
    extension = ".pyd" if platform.system() == "Windows" else ".so"
    compiled_module_filename = f"{module_name}{extension}"
    compiled_module_path = os.path.join(os.path.dirname(pyx_file), compiled_module_filename)

    if not os.path.exists(compiled_module_path):
        print(f"Compiling {pyx_file}...")
        setup(
            name=module_name,
            ext_modules=cythonize(pyx_file),
            script_args=['build_ext', '--inplace'],
            options={'build_ext': {'inplace': True, 'force': True}},
            zip_safe=False
        )
        print(f"{pyx_file} compiled successfully.")
    else:
        print(f"{compiled_module_path} already exists. Skipping compilation.")


# Usage example
if __name__ == "__main__":
    # Specify the directory containing .pyx files
    compile_cython_files_in_directory("GERDPySim")
