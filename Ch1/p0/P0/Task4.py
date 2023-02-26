"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from itertools import chain

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

num_text=set(chain.from_iterable([(sender, reciever) for sender, reciever, _ in texts]))

callers = set()
recievers = set()

for caller, reciever, _, _ in calls :
    callers.add(caller)
    recievers.add(reciever)

telemarketers = callers - (num_text|recievers)

print("These numbers could be telemarketers: ")

for num in sorted(telemarketers) :  # Return a new sorted list from the items in iterable
    print(num)
