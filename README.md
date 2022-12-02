# pythonic_way_reading_file

# Description
This repo contains a module with a tiny code (pythonic_readfile.py module). In that code, you can find a pythonic way to read a file line by line by calling a function. Specifically, you want to read a file (e.g. file.txt) from your "main" function using a loop structure in which, in each loop, you call another function to get a line from the file.

# Why this?
There are cases where you want to be independent if you are using a file or some string (e.g. when you are testing your code). Or you want to reduce one level of indentation.

# How ?
You must use yield and manually take care of iter() and next() functions. 
