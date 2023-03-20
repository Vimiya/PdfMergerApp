"""
This is the main program which calls the starting function to build the PdfMerger app
Menu and operations
"""
from start import starting
from app_functions import *
writelogs('main', 'info', 'main program started')
try:
    starting()
except Exception as e:
    writelogs('main', 'error', 'Some error occurred while calling starting()')
    writelogs('main', 'exception', 'e')
else:
    writelogs('main', 'info','The Application worked successfully')
