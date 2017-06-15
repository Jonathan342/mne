# mne
A python module that allows for easy command line stream editing, similair to perl -ne 

This module allows the user to use python from the command line in a similair way to perl -ne '`code`', which executes the code in a loop around lines piped to it in the command line.

To do so, simply do

    python -mne $'`your code`' 

For example:

    cat input_file.txt|python -mne $'L=L.rstrip();values = L.split("\t");\nif (float(values[1])>.001): print (values[1])'

will print every line of input_file.txt that has a first column value greater than or equal to .001. Note the $ before the code. That is necessary if you want to include control statements (e.g. if and while ).

This module is slightly modified from this stack overflow answer here: http://stackoverflow.com/questions/4427542/how-to-do-sed-like-text-replace-with-python 

A key point of this module that distinguishes it from other similair ideas (e.g. pyp: https://code.google.com/p/pyp/) is that it allows control statements, which provides more flexibility. 

