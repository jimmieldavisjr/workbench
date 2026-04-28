import os
import sys
import platform

def show_python_info():
    print("=== PYTHON ENVIRONMENT INFO ===")
    print("Python Version:", sys.version)
    print("Executable:", sys.executable)
    print("Platform:", platform.platform())
    print("Working Directory:", os.getcwd())

show_python_info()