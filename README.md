# GERDPy - Simulation Tool for Geothermal Heat Pipe Surface Heating Systems

GERDPy is a Python-based simulation tool designed to model directly geothermally heated surface deicing systems using
a two-phase thermosiphon and was specifically developed for the project GERDI. Thus, this modelling tool represents a 
very specific system and is not suitable as a general modelling software for borehole heat exchangers.

![title](https://user-images.githubusercontent.com/77793428/214841221-70ab81fb-b504-46df-9ef2-10c96380eec9.png)

The development of GERDPy is fully based on open-source toolboxes and libraries in Python. Some of the modules are 
directly based on the open-source toolbox for the evaluation of thermal response factors for geothermal borehole 
fields, **Pygfunction** by Massimo Cimmino. 
> 🔗 https://github.com/MassimoCimmino/pygfunction

The GUI is based on the PySide6 / PyQt6 interface **PyDracula** created by Wanderson M. Pimenta.
> 🔗 https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6

# Python Version
 For using GERDPy Simulation Tool, Python 3.7.9 must be used. If not installed, click the link below and install Python 3.7.9.
> 🔗 https://www.python.org/downloads/release/python-379/

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
> ### **MacOS and Linux**:
```console
python3.7 guimain.py 
```
The GERPDPy GUI will then open and you can work there from now on.

####Example for Windows:
Open cmd.exe by clicking on the Windows icon and just type 'cmd'. For navigating to a folder use the command 'cd'. 

To navigate one level up in your folders use:
```console
cd ..
```
To navigate to a specific folder and subfolder use:
```console
cd folder\subfolder
```
This is how your console might look: 

![cmd_example](https://github.com/MeMaZAE/Modern_GUI_GerdPy/assets/77793428/d6aad9a5-4bd7-499c-a79f-3ba7905992cd)

# Using GERDPy
For detailed information about functionality and usage of the tool, please read **GERDPy_User Handbook.pdf**.

