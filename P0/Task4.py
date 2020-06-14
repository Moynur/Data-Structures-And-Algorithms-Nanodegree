"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# create set of outgoing calls
# create set of incoming calls
# create set of outgoing texts
# create set of incoming texts 

def Outbound_callers():
    outbound_calls = []
    for number in calls:
        outbound_calls.append(number[0])
    return set(outbound_calls)

def Incoming_callers():
    inbound_calls = set()
    for number in calls:
        inbound_calls.add(number[1])
    return set(inbound_calls)

def Outbound_texters():
    outbound_texts = set()
    for number in texts:
        outbound_texts.add(number[0])
    return outbound_texts

# incoming_cexters returns all numbers which have received texts
def incoming_texters():
    inbound_texts = []
    for number in texts:
        inbound_texts.append(number[1])
    return set(inbound_texts)

def answer():
    a = Outbound_callers()
    b = incoming_texters()
    c = Outbound_texters()
    d = Incoming_callers()
    return a.difference(b, c, d)

print('These numbers could be telemarketers: ', answer())