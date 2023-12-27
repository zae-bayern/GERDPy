import subprocess
import sys
import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import __version__ as PySide2_Version

# check if resources file fits current Qt/PySide version, recompile if not
def compile_qrc(qrc_path, output_path):
    """
    Compiles a .qrc file into a Python module using pyside2-rcc.
    Recompiles only if the output file is missing or compiled with a different PySide2 version.

    Args:
        qrc_path (str): Path to the .qrc file.
        output_path (str): Path for the output Python file.
    """
    qt_version_comment = f"# Compiled with PySide2 version {PySide2_Version}\n"

    # Check if the output file already exists and matches the current PySide2 version via comment
    if os.path.exists(output_path):
        with open(output_path, 'r') as file:
            first_line = file.readline()
            if first_line == qt_version_comment:
                print(f"Resource file {output_path} already exists and is up-to-date. Skipping recompilation.")
                return

    # Compile the .qrc file
    try:
        command = ['pyside2-rcc', qrc_path, '-o', output_path]
        subprocess.run(command, check=True)

        # Add a comment to the top of the file with the PySide2 version
        with open(output_path, 'r+') as file:
            content = file.read()
            file.seek(0, 0)
            file.write(qt_version_comment + content)

        print(f"Compiled {qrc_path} to {output_path} with PySide2 version {PySide2_Version}")
    except subprocess.CalledProcessError as e:
        print(f"Error compiling resource file: {e}")

compile_qrc("../resources.qrc", "resources_rc.py")

# GUI FILE
from .ui_main import Ui_MainWindow

# APP SETTINGS
from .app_settings import Settings

# IMPORT FUNCTIONS
from .ui_functions import *

# APP FUNCTIONS
from .app_functions import *

# USE FUNCTIONS
from .use_functions import *
