#Samuel Nerayo
# c3400 hw3
# python program that simulates a Mark-Sweep garbage collection algorithm.

# Functionality
    #1. get the name of an input file from command lne
    #2. process the file. The first line will contain n the number of the heap blocks
    # The heap block will be identified using the num 0 through n - 1
    # Each subsequent line will contain an ordered pair either in the form:

import sys
from collections import deque

# Initializing dictionaries
roots = {}  # holds ref to root obj
refs = {}  # holds ref to non-root obj

# Step 1: get input file
with open(sys.argv[1], 'r') as file: #open file
    num_blocks = int(file.readline()) #read first line
    for line in file:  # loop throu the remaining lines
        src, dest = line.strip().split(",") #split the line into source
        if src.isalpha():  # if src is letter, then it is a root obj
            roots[src] = int(dest)  #add to root dict
        else:  #else add obj to ref dict
            refs[int(src)] = int(dest)

#  Step 2: Define marking function
marked = set() #holds ref to all marked obj
def mark(obj):
    if obj in marked: #check if obj has already been marked
        return
    marked.add(obj) #mark obj
    if obj in refs: #check if obj has ref to other obj, then mark all of them
        mark(refs[obj])
    if obj in roots:
        mark(roots[obj])

# Step 3: Perform mark-sweep algorithm
for obj in roots.values(): #loop through all root obj
    mark(obj) #mark each root obj & obj that it ref

for obj in refs: #looping through non-root obj
    if obj not in marked: #if obj wasn't marked, it can't be reached therefore swept
        refs[obj] = None #setting ref to none

# Output marked and swept nodes
marked_nodes = sorted(list(marked)) #converting set of marked obj to list and sort
swept_nodes = list(set(range(num_blocks)) - set(marked_nodes)) #look for obj that wasn't marked
print("Marked nodes:", " ".join(map(str, marked_nodes))) #printing maked objt
print("Swept nodes:", " ".join(map(str, swept_nodes))) #print swept objt

