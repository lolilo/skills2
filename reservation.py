"""
Reservation finder

Along with this file, you'll find two files named units.csv and reservations.csv with fields in the following format

units.csv
location_id, unit_size

reservations.csv
location_id, reservation_start_date, reservation_end_date

You will write a simple application that manages a reservation system. It will have two commands, 'available' and 'reserve' with the following behaviors:

available <date> <number of occupants> <length of stay>
This will print all available units that match the criteria. 
Any unit with capacity equal or greater to the number of occupants will be printed out.

Example:
SeaBnb> available 10/10/2013 2 4
Unit 10 (Size 3) is available
Unit 20 (Size 2) is available

reserve <unit number> <start date> <length of stay>
This creates a record in your reservations that indicates the unit has been reserved. It will print a message indicating its success.

A reservation that ends on any given day may be rebooked for the same evening, ie:
    
    If a reservation ends on 10/10/2013, a different reservation may be made starting on 10/10/2013 as well.

Example:
SeaBnb> reserve 10 10/11/2013 3 
Successfully reserved unit 10 for 3 nights

Reserving a unit must make the unit **unavailable for later reservations. Here's a sample session:

SeaBnb> available 10/10/2013 2 4
Unit 10 (Size 3) is available
Unit 20 (Size 2) is available
SeaBnb> reserve 10 10/11/2013 3 
Successfully reserved unit 10 for 3 nights
SeaBnb> available 10/10/2013 2 4
Unit 20 (Size 2) is available
SeaBnb> reserve 10 10/11/2013 3 
Unit 10 is unavailable during those dates
SeaBnb> quit

Notes:
Start first by writing the functions to read in the csv file. These have been stubbed for you. 
Then write the availability function, then reservation. 
Test your program at each step (it may be beneficial to write tests in a separate file.) 
Use the 'reservations' variable as your database. 
Store all the reservations in there, including the ones from the new ones you will create.

The datetime and timedelta classes will be immensely helpful here, as will the strptime function.
"""

import sys
import datetime

from os.path import exists

def parse_one_record(line):
    """Take a line from reservations.csv and return a dictionary representing that record. 
    (hint: use the datetime type when parsing the start and end date columns)

    reservations.csv
    location_id, reservation_start_date, reservation_end_date"""
    # (location_id, reservation_start_date, reservation_end_date) -- what to make a key? 
    # location_id should be a key? value should be (rereservation_start_date, reservation_end_date)?
    # if value is None, the particular room is available. 

    # noooooooooooo, after consulting with Classic Nick
    # {(room: 'ID', start_date: '', end_date: '')}
    # Then create a list of dictionaries. 


    # format the reservation as a tuple, (unit_ID, start, end)
    split_line = line.split(', ')
    split_line[2] = split_line[2].strip()

    # datetime data type
    for date in range(len(split_line[1:]) + 1)[1:]:
        date_as_datetime_datatype = datetime.datetime.strptime(split_line[date], '%m/%d/%Y')
        split_line[date] = date_as_datetime_datatype
    # print split_line

    # need to iterate over the last two items in the split_line list, which are dates
    # for date in range(len(split_line[1:]) + 1)[1:]:

    #     # split the date on '/'
    #     split_line[date] = split_line[date].split('/')

    #     # date takes in year, month, day parameters
    #     # need correct formatting to use datetime 
    #     date_reformatted = [split_line[date][2], split_line[date][0], split_line[date][1]]
    #     split_line[date] = tuple(date_reformatted)
    #     # print 'date is ', split_line

    d = {}
    d['room'] = split_line[0]
    d['start_date'] = split_line[1]
    d['end_date'] = split_line[2]

    # {'room': '1', 'end_date': datetime.datetime(2014, 1, 9, 0, 0), 
    # 'start_date': datetime.datetime(2014, 1, 1, 0, 0)}

    return d

def read_units(in_file):
    """Read in the file units.csv and returns a list of all known units.

    units.csv
    location_id, unit_size"""

    known_units = []
    f = open(in_file)

    # go line by line in units.csv and append each unit as tuple, (location_id, unit_size)
    in_file_ended = False
    while not in_file_ended:
        indata = f.readline()
        if indata == '':
            in_file_ended = True
            break
        split_indata = indata.split(', ')
        split_indata[1] = split_indata[1].strip()
        # print split_indata
        known_units.append(tuple(split_indata))

        # we just want a list of the units - don't need size
        # no, that's poor word choice
        # known_units.append(split_indata[0])

    return known_units

def read_existing_reservations(in_file):
    """Reads in the file reservations.csv and returns a list of reservations."""
    # reservations is a list of dictionaries 
    reservations = []
    f = open(in_file)

    in_file_ended = False
    while not in_file_ended:
        indata = f.readline()
        if indata == '':
            in_file_ended = True
            break

        # feed tuple into function to change it into a dictionary, 
        # {(room: 'ID', start_date: '', end_date: '')}
        reservation_as_dict = parse_one_record(indata)
        # append to list of reservations
        reservations.append(reservation_as_dict)

    return reservations

def available(units, reservations, start_date, occupants, stay_length):
    """
    available <date> <number of occupants> <length of stay>
    This will print all available units that match the criteria. 
    Any unit with capacity equal or greater to the number of occupants will be printed out.

    Example:
    SeaBnb> available 10/10/2013 2 4
    Unit 10 (Size 3) is available
    Unit 20 (Size 2) is available
    """

    # convert start_date to datetime type
    start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y')
    # calculate end_date
    end_date = start_date + datetime.timedelta(days = int(stay_length))
    

    # units is a list of tuples, length 2
    # reservations is a list of dictionaries

    units_of_proper_size = []
    for unit in units:
        unit_size = unit[1]
        if unit_size >= occupants:
            # add to list of possible units. must check for existing reservation later
            units_of_proper_size.append(unit)

    # print units_of_proper_size


    # for unit in units: 
    #     if 

    unit_id = 0
    print "Unit %d is available" % unit_id

def reserve(units, reservations, unit_id, start_date, stay_length):
    print "Successfully reserved"

def main():
    args = sys.argv    

    # Ensure proper files given. 
    if len(args) < 3:
        print "Please provide the python script, units.csv, and reservations.csv."

    # Check if args exists
    for f in args:
        if not exists(f):
            print "%r does not exist." % f
            return 

    units = read_units(args[2])
    # print 'units are ', units
    reservations = read_existing_reservations(args[1])  
    # print 'reservations are ', reservations

    while True:
        command = raw_input("SeaBnb> ")
        cmd = command.split()
        if cmd[0] == "available":
            # look up python variable arguments for explanation of the *
            available(units, reservations, *cmd[1:])
        elif cmd[0] == "reserve":
            reserve(units, reservations, *cmd[1:])
        elif cmd[0] == "quit":
            sys.exit(0)
        else:
            print "Unknown command"

if __name__ == "__main__":
    main()




"""
    user@chromebox-003:~/src/skills2$ python
    Python 2.7.3 (default, Sep 26 2013, 20:03:06) 
    [GCC 4.6.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import datetime
    >>> today = date.today()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'date' is not defined
    >>> import time
    >>> today = date.today()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'date' is not defined
    >>> from datetime import date
    >>> today = date.today()
    >>> today
    datetime.date(2014, 2, 17)
    >>> print today
    2014-02-17
    >>> date(10/16/2013)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Required argument 'month' (pos 2) not found
    >>> date(10,16,2013)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: month must be in 1..12


    >>> date(2013,12,13)
    datetime.date(2013, 12, 13)
    >>> n = date(2013,12,13)
    >>> print n
    2013-12-13
    >>> print n > today
    False
    >>> print n < today
    True


class datetime.date(year, month, day)
class datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])

"""
"""
d = '2/2/2013'
datetime.datetime.strptime(d, '%m/%d/%Y')
datetime.datetime(2013, 2, 2, 0, 0)

>>> haha = datetime.datetime.strptime(d, '%m/%d/%Y')
>>> haha
datetime.datetime(2013, 2, 2, 0, 0)
>>> haha.strftime(new)
'2013-02-02'



>>> format
'2013-02-02'
>>> type(format)
<type 'str'>
>>> format > 2012-02-02
True
>>> format > 2013-02-03
True
>>> 


>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2014, 2, 17, 17, 4, 41, 529036)
>>> haha
datetime.datetime(2013, 2, 2, 0, 0)
>>> haha > datetime.now()
False
>>> type(haha)
<type 'datetime.datetime'>


# THIS IS THE DATETIME DATA TYPE. SHIT. 

Date = datetime.datetime.strptime(StartDate, "%m/%d/%y")

EndDate = Date + datetime.timedelta(days=10)



"""

