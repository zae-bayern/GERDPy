import os
import platform
import importlib

use_cython = False
module_names = ['R_th', '_main', 'boreholes', 'gfunction', 'heat_transfer', 'heating_element', 'heating_element_utils', 'heatpipes', 'load_aggregation', 'load_generator', 'load_generator_utils', 'utilities', 'weather_data']

if use_cython:
  from .compile_cython import *
  compile_cython_files_in_directory(".")

  for name in module_names:
    # Determine the correct extension based on the operating system
    extension = ".pyd" if platform.system() == "Windows" else ".so"
    cython_module_path = os.path.join(os.path.dirname(__file__), name + extension)

    # Check if the Cython compiled module exists
    if os.path.exists(cython_module_path):
      try:
        __import__(f'{name}.pyx', fromlist=['*'])
      except ImportError:
        print(f"Failed to import Cython module {name}, falling back to Python version.")
        __import__(f'{name}.py', fromlist=['*'])
    else:
      print(f"Cython module {name} not found, using Python version.")
      __import__(f'{name}.py', fromlist=['*'])
else:
  # Import the regular Python module
  #__import__(f'{name}', fromlist=['*'])
  for module_name in module_names:
    globals()[module_name] = importlib.import_module('.' + module_name, package=__name__)
