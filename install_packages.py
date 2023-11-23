import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'matplotlib'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'numpy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'scipy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'PySide6==6.2.3'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'PyQt6==6.2.3'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'CoolProp'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'openpyxl'])

