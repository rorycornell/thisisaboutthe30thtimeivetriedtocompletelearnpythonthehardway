people = int(raw_input("How many people are there? "))
cars = int(raw_input("How many cars are there? "))
buses = int(raw_input("How many buses are there? "))

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We cannot decide."

if buses > cars:
    print "There is to many buses."
elif buses < cars:
    print "Maybe we should take the buses."
else:
    print "We cannot decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
