#!/usr/bin/env python

import sys
import argparse
import string
from os import listdir
from os.path import isfile, join
import os
import time
from myprog_h import myprogh

def main():

    # parser to take arguments given in command line as variables and be able to accept files as input
    parser=argparse.ArgumentParser(
    description='''Help page for myprog: ''')
    parser.add_argument('inputDirectory', help='Path to the input directory.')
    parser.add_argument('-help', action='store_true', help='Show the help screen.')
    args=parser.parse_args()

    # output the help screen if user enters in -help
    if args.help:
        parser.print_help()
        exit(0)

    # assign variables 
    x = args.inputDirectory
    onlyfiles = [f for f in listdir(x) if isfile(join(x, f))]
    i = 0
    c = myprogh()

    # open file for writing
    f = open("track.txt","a+")

    # check if log is not used and if it is to resume playback else will create the intial runthrough
    if (os.stat("track.txt").st_size == 0):
        c.intial(onlyfiles)
    else:
        c.resume()

    # infinte loop to keep shuffeling throuhg music playlist
    while 1:
        c.shuf(onlyfiles)


if __name__ == "__main__": 
    main()