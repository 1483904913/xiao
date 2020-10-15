import sys
import xiao1.py
import xiao2.py
sys.modules['xiao1'].__dict__.clear()
sys.modules['xiao2'].__dict__.clear()
xiao1.py
xiao2.py