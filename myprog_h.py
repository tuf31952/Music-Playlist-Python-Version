from random import shuffle
import time

class myprogh:

    # varible to keep track of the number of play counts
    count = 1

    def intial(self, x):

        # open tracking files 
        f = open("track.txt","w+")
        fcount = open("count.txt", "w+")
        fplay = open("playlist.txt", "w+")
        findex = open("index.txt", "w+")
        fintial = open("intial.txt", "w+")
    
        # declare variables for loops
        i = 0
        q = 1
        c = 0

        # create files that will be used to index intial play order where to resume from
        while c < len(x):
            fplay.write("%s\n" % x[c])
            fintial.write("%s\n" % x[c])
            findex.write("%d\n" % q)
            c += 1
            q += 1

        fcount.write("%d" % self.count)

        # get list of songs and write to log file
        while i < len(x):
            c = i + 1
            print ("%d (%d, %d): playing file %s" % (c, c, self.count, x[i]))
            f.write("%d\n" % c)
            time.sleep(0.5)
            i += 1

        # reset file pointer and increment count
        fintial.seek(0)
        self.count += 1
        fcount.write("%d" % self.count)

        # once first playthough is complete without interupt proceed to shuffle list
        self.shuf(x)

    def shuf(self, songlist):

        # open tracking files 
        f = open("track.txt","w")
        fcount = open("count.txt", "a+")
        fplay = open("playlist.txt", "w+")
        findex = open("index.txt", "w+")

        # declare variables for use in tracking log
        shuffle(songlist)
        intialindex = []
        c = 0
        i = 0
        q = 1

        # open intital index to track song index
        with open('intial.txt') as my_file:
            for lines in my_file:
                intialindex.append(lines)

        # new shuffled playlist for resume if needed
        while c < len(songlist):
            fplay.write("%s\n" % songlist[c])
            findex.write("%d\n" % q)
            c += 1
            q += 1

        # while loop to output playlist
        while i < len(songlist):
            index = intialindex.index(songlist[i] + "\n") + 1
            c = i + 1
            print ("%d (%d, %d): playing file %s" % (c, index,  self.count, songlist[i]))
            f.write("%d\n" % c)
            time.sleep(0.5)
            i += 1

        self.count += 1
        fcount.write("%d" % self.count)

    def resume(self):

        # open tracking files 
        f = open("track.txt","r+")
        fcount = open("count.txt", "r+")

        # declare arrays for playlist and indexing of log file
        songs = []
        intialindex = []

        # get the times played count
        for line in fcount.read():
            pass
        last = line

        # get the last track played and continue 
        for lines in f:
            pass
        recent = lines

        # get the intial index for output
        with open('intial.txt') as my_file:
            for lines in my_file:
                intialindex.append(lines)
                
        # open last used playlist to continue from
        with open('playlist.txt') as my_file:
            for lines in my_file:
                songs.append(lines)

        # declare varibles for resume loop
        recent = int(recent)
        x = recent
        self.count = int(last)

        # while loop to continue from last played song
        while x < len(songs):
            c = x + 1
            y = recent + 1
            index = intialindex.index(songs[x]) + 1
            print ("%d (%d, %d): playing file %s\b" % (y, index, self.count, songs[x]))
            f.write("%d\n" % c)
            time.sleep(0.5)
            recent += 1
            x += 1

        self.count += 1

        fcount.write("%d" % self.count)

