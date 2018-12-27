import esky.bdist_esky
from esky.bdist_esky import Executable as Executable_Esky
from cx_Freeze import setup, Executable
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

include_files = ['img/background.jpg', 'img/player.gif']
setup(
    name='my_game',
    version='1.0.0',
    options={
        'build_exe': {
            'packages': ['os', 'sys', 'ctypes', 'win32con', 'img'],
            'include_files': include_files,
            'include_msvcr': True,
        },
        'bdist_esky': {
            'freezer_module': 'cx_freeze',
        }
    },
    data_files=include_files,
    scripts=[
        Executable_Esky(
            "main.py",
            gui_only=True,
            ),
    ],
    executables=[Executable('main.py', base='Win32GUI')]
)
