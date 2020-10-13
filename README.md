# Aleatory
This is Aleatory a random file numbers generator.
it gives a random integer or float to the terminal.
Or it could make a csv, json or excel file full of random integers or floats.

Warning: must have pandas,openpyxl and random libraries from python installed 

It's use this way:

 --n --i <minimum> <maximum> this display a random integer bweteen minimum and maximum (both of them must be integers) including them

 --n --f <minimum> <maximum> same as above but with floats (minimum and maximum could be integers or floats )

--csv --i <minimum> <maximum> <number of rows> <number of columns> <name of the file> <path where the file would be> This creates a csv file with a name in the path you specify

--csv --f <minimum> <maximum> <number of rows> <number of columns> <name of the file> <path where the file would be> same than above but with floats

--json --i <minimum> <maximum> <number of rows> <number of columns> <name of the file> <path where the file would be> same but with json file

--json --f <minimum> <maximum> <number of rows> <number of columns> <name of the file> <path where the file would be>

--excel --i <minimum> <maximum> <number of rows> <number of columns> <name of the file> <path where the file would be>
  
--excel --f <minimum> <maximum> <number of rows> <number of columns> <name of the file> <path where the file would be>


Examples: Try

./rand.py --n --f 0 100

./rand.py --csv --f 20 200 100 5 Imanexample /home/username
