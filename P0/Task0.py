"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    v = texts[1]
    print('last record of texts, %s texts %s at a time %s' % (v[0], v[1], v[2]))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    x = calls[-1]
    print('last record of calls, %s calls %s at a time %s, lasting %s seconds' % (x[0], x[1], x[2], x[3]))


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

