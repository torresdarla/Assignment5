#Programmed by Darla Torres
#July 20, 2017
#This program will smulate a hotdog eating contest with 3 contestants


import random
import Short
import time

  
def main(limit, roundlimit):
    guess = Short.userString("Pick a winner (Tom, Sally, or Fred):")
    print "Ready, set, eat!"
    print "\n"
    keepGoing = True
    counts = [0,0,0]
    
    while keepGoing:
        t = random.randrange(1,roundlimit)
        s = random.randrange(1,roundlimit)
        f = random.randrange(1,roundlimit)
        counts[0] = counts[0] + t
        counts[1] = counts[1] + s
        counts[2] = counts[2] + f
        time.sleep(3)
        print "chomp... chomp... chomp..."
        print "\n"
        print "Tom has eaten %s hot dogs!" %(counts[0])
        print "Sally has eaten %s hot dogs!" %(counts[1])
        print "Fred has eaten %s hot dogs!" %(counts[2])
        print "\n"
        print "chomp... chomp... chomp..."
        if counts[0] >= limit or counts[1] >= limit or counts[2] >= limit:
          keepGoing = False
          indexWinner = counts.index(max(counts))
    contest = ['Tom', 'Sally', 'Fred']
    winner = contest[indexWinner]
    if guess == winner:
     print "You guessed right, %s wins!" %guess
    else:
     print "You guessed wrong, %s wins!" %winner
     
        
            
main(50,10)