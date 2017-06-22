# Provide emulation of `perl -ne` for python
#Author: Joshua Broyde,  (Honig lab and Califano lab, at Columbia University Medial Center)
#Date: June 2017

# Usage:
#
#     python -mne $'<program>'

# In, `<program>`, use the variable `L` to read and change the current line.
# The $ is important, because it python has significant whitespace.You need to put '\n' between lines if you have conditions or for loops.

# Example:
#
#         python -mne $'L = re.sub("pattern", "replacement", L)'

# Another Example:
#
#	cat input_file.txt|python -mne $'L=L.rstrip();values = L.split("\t");\nif (float(values[1])>.001): print (values[1])'
# 

#This second example will read input_file.txt,split the string by tabs and print out the second value if it is greater than 1. 
#If you want to have more modules at your disposal from the command line, just have them imported in this module. 
#  Another example
# python -mne $'if ">" in L:\n L=L.strip();v=list(L);del v[-1]\n print(*v,sep="")\nelse:\n print(L,end="")'

# This script is slightly modified from this stack overlfow answer here: http://stackoverflow.com/questions/4427542/how-to-do-sed-like-text-replace-with-python 
#
from __future__ import print_function
import re
import sys
import math
import os
import string
exec(open("/Users/joshuabroyde/Scripts/Modules/myfunctions.py").read())
#Add more modules if you want from the command line



for L in sys.stdin:
	try:
		exec(sys.argv[1])
		 #L,
	except:
		#sys.exit('-p destination: $!\n')
		pass


