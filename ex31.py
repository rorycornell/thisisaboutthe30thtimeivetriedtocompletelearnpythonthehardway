print "You enter a dark room with two doors. Do you go through Door #1, Door #2, or Door #3"
door = raw_input("> ")

if door == "1":
    print "There is a giant bear here eating a cheese cake. What do you do"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off.  Good Job!"
    elif bear == "2":
        print "The bear eats your legs off. Good Job!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1: Blueberries."
    print "2: Yellow jacket clothespins."
    print "3: Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

elif door == "3":
    print "You wake up on election day. Who do you vote for?"
    print "1: Donald Trump"
    print "2: Hillary Clinton"
    print "3: Other"

    vote = raw_input("> ")
    if vote == "1":
        print "The Wall is built. America is made great again."
    else:
        print "White men are made illegal and you have to check your privilege"

else:
    print "You stumble around and fall on a knife and die.  Good job!"
