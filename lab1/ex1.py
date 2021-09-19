#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out


# Import libraries
import sys
import argparse
import string

def enc(letter, key):
    return chr((ord(letter)+key)%256)

def dec(letter, key):
    return enc(letter, -key)

def doStuff(filein, fileout, mode_e_d, key):
    # open file handles to both files
    fin = open(filein, mode="r", encoding="utf-8", newline="\n")  # read mode
    fin_b = open(filein, mode="rb")  # binary read mode
    fout = open(fileout, mode="w", encoding="utf-8", newline="\n")  # write mode
    fout_b = open(fileout, mode="wb")  # binary write mode
    c = fin.read()  # read in file into c as a str

    #loop thru to get each character for enc and dec 
    output_to_file = ""

    if (mode_e_d == "e"):
        for character in c:
            output_to_file += enc(character, key)
    
    # and write to fileout
    if(mode_e_d == "d"):
        for character in c:
            output_to_file += dec(character, key)
    
    fout.write(output_to_file)

    # close all file streams
    fin.close()
    fin_b.close()
    fout.close()
    fout_b.close()


# our main function
if __name__ == "__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="filein", help="input file")
    parser.add_argument("-o", dest="fileout", help="output file")

    #add for enc and key
    parser.add_argument("-m", dest="mode",help="type e for encryption or d for decryption")
    #how many shifts
    parser.add_argument("-k", dest="key",type=int)
    # parse our arguments
    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout
    #check the keys
    if((1<=args.key<=len(string.printable)-1) == False):
        raise ValueError('The value of the key must be between 1 and that of string.printable')
    
    #check mode arguments
    if(args.mode.lower() == "e" or args.mode.lower()=="d"):
        doStuff(filein, fileout, args.mode.lower(), args.key)
    else:
        raise SyntaxError('The mode has to be only \"d" or \"e" case insensitive')

    
    

    

    # all done
