from pathlib import Path
import sys,unittest,requests,time

addr=Path(str(Path().cwd()).split('Interfice')[0])/'Interfice'/'data'
sys.path.append(str(addr))
from variable import *
