"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
z = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for numbers in texts:
        z.add(numbers[0])
        z.add(numbers[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for numbers in calls:
        z.add(numbers[0])
        z.add(numbers[1])

print(f'There are {len(z)} different telephone numbers in the records.')

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
