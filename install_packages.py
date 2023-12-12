import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'matplotlib'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'numpy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'scipy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'PySide2'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'PyQt5'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'CoolProp'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'openpyxl'])
