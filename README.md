# GERDPy - Simulation Tool for Geothermal Heat Pipe Surface Heating Systems

GERDPy is a Python-based simulation tool designed to model directly geothermally heated surface deicing systems using
a two-phase thermosiphon and was specifically developed for the project GERDI. Thus, this modelling tool represents a 
very specific system and is not suitable as a general modelling software for borehole heat exchangers.

![title](https://user-images.githubusercontent.com/77793428/214841221-70ab81fb-b504-46df-9ef2-10c96380eec9.png)

The development of GERDPy is fully based on open-source toolboxes and libraries in Python. Some of the modules are 
directly based on the open-source toolbox for the evaluation of thermal response factors for geothermal borehole 
fields, **Pygfunction** by Massimo Cimmino. 
> 🔗 https://github.com/MassimoCimmino/pygfunction

The GUI is based on the PySide / PyQt interface **PyDracula** created by Wanderson M. Pimenta.
> 🔗 https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6

# Python Version
 For using GERDPy Simulation Tool, Python 3.7.9 or a higher version must be used. This document will assume Python 3.7.9 is used.
 If not installed, click the link below and install Python 3.7.9.
> 🔗 https://www.python.org/downloads/release/python-379/

You may check if Python is added to PATH variable on your System. Therefore click 'Start' and search for 'environment variables'.
Then add the following paths to the PATH variable.
> C:\Users\username\AppData\Local\Programs\Python\Python37\
> C:\Users\username\AppData\Local\Programs\Python\Python37\Scripts

# Required Packages
For operating GERDPy correctly, some Python Packages are required. Therefore navigate to the folder, where GERDPy is located 
and run the command below in your preferred console (e.g. cmd for Windows, Terminal for MacOS or Linux).
If your System already satisfies all requirements, you can skip this section.
> ### **Windows**:
```console
py -3.7 install_packages.py
```
> ### **MacOS and Linux**:
```console
python3.7 install_packages.py 
```

# Running
Inside your preferred console navigate to the folder, where GERDPy is located and run the commands below depending on your system.

> ### **Windows**:
```console
py -3.7 guimain.py
```
or run the batch file
```console
.\GERDPy.bat
```

> ### **MacOS and Linux**:
```console
python3.7 guimain.py 
```
or run the shell script
```console
./GERDPy.sh
```
The GERPDPy GUI will then open and you can work there from now on.

####Example for Windows:
Open cmd.exe by clicking on the Windows icon and type 'cmd' for searching for 'cmd.exe'. For navigating to a folder in cmd use the command 'cd'.
Alternatively, navigate to the folder in Windows Explorer, type 'cmd' in the address bar and press enter.

To navigate one level up in your folders use:
```console
cd ..
```
To navigate to a specific folder and subfolder use:
```console
cd folder\subfolder
```
This is how your console might look: 

![cmd_example](https://github.com/zae-bayern/GERDPy/assets/77793428/1b69a326-45f2-42f9-9473-b5847eee3c7e)

# Using GERDPy
For detailed information about functionality and usage of the tool, please read **GERDPy_User Handbook.pdf**.

# Optional: Activate cython support
Make sure cython is installed:
```console
pip install cython
```

Then open the file 'GERDPySim/`__init__.py`' and on line 5 change 'use_cython = False' to 'use_cython = True' to activate.
