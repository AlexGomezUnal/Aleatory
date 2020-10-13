# Aleatory
This is Aleatory a random file numbers generator.
it gives a random integer or float to the terminal.
Or it could make a csv, json or excel file full of random integers or floats.

Warning: must have pandas,openpyxl and random libraries from python installed 

It's use this way:

python3 --n --i <minimum> <maximum> this display a random integer bweteen minimum and maximum (both of them must be integers) including them

python3 --n --f <minimum> <maximum> same as above but with floats (minimum and maximum could be integers or floats )

python3 --csv --i <minimum> <maximum> <number of rows> <number of columns> <name of the file> <path where the file would be> This creates a csv file with a name in the path you specify

python3 --csv --f <minimum> <maximum> <number of rows> <number of columns> <name of the file> <path where the file would be> same than above but with floats

python 3 --json --i <minimum> <maximum> <number of rows> <number of columns> <name of the file> <path where the file would be> same but with json file

python3 --json --f <minimum> <maximum> <number of rows> <number of columns> <name of the file> <path where the file would be>

python3 --excel --i <minimum> <maximum> <number of rows> <number of columns> <name of the file> <path where the file would be>

python3 --excel --f <minimum> <maximum> <number of rows> <number of columns> <name of the file> <path where the file would be>


Examples: Try

Python3 --n --f 0 100
Python3 --csv --f 20 200 100 5 Imanexample /home/username
