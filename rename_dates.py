#! python3
# Changes the date in file name from US format (MM-DD-YYYY) to european format (DD-MM-YYYY).
# Based on 'Automate the Boring Stuff with Python' by Al Sweigart, project from chapter 10.
# https://automatetheboringstuff.com/2e/chapter10/

import re
import os
import shutil

regex = re.compile((r'''
(.*?)
([0-1]?\d)-
(([0-2]?\d)|3[0-1])-
([0-2]?\d+)
(.*?)$
'''), re.VERBOSE)

files = os.listdir('..')

for filename in files:
    date_filename = regex.search(filename)
    try:
        if date_filename.groups():
            before_date = date_filename.group(1)
            day = date_filename.group(3)
            month = date_filename.group(2)
            year = date_filename.group(5)
            after_date = date_filename.group(6)
            new_name = before_date + day + '-' + month + '-' + year + after_date
            if int(month) <= 12 and int(day) <= 31:
                shutil.move(filename, new_name)
                print(f'Renamed file: {date_filename.group()} -> {new_name}')
            else:
                print(f'Did not rename file {filename}: incorrect date.')
    except AttributeError:
        print(f'Did not rename file {filename}: no date.')
