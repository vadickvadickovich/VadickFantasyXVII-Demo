from distutils.core import setup
import py2exe
import os, sys

origIsSystemDLL = py2exe.build_exe.isSystemDLL # save the orginal before we edit it
def isSystemDLL(pathname):
    # checks if the freetype and ogg dll files are being included
    if os.path.basename(pathname).lower() in ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll"):
            return 0
    return origIsSystemDLL(pathname) # return the orginal function
py2exe.build_exe.isSystemDLL = isSystemDLL # override the default function with this one

setup(
    console = [
        {
            "script": "VadickFantasyXVI.py",                    ### Main Python script    
            "icon_resources": [(0, "images/icon.ico")]     ### Icon to embed into the PE file.
        }
    ],
) 