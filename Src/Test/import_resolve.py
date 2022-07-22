import os
import sys

def import_resolve()-> None:
    """Resolves ModuleNotFoundError"""
    PATH = os.path.abspath(path= os.getcwd()+"\\Src\\DS\\")
    sys.path.append(PATH)
