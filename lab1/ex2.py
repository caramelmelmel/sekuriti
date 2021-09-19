#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out
# Leong Yun Qin Melody
#Student ID: 1004489

# Import libraries
import sys
import argparse
import string

def enc(byte, key):
    return ((byte + key)%256)

def dec(byte, key):
    return enc(byte, -key)

def doStuff(filein, fileout, key, mode):
    # open file handles to both files
    
    fin_b = open(filein, mode="rb")  # binary read mode
    fout_b = open(fileout, mode="wb")  # binary write mode
    c = fin_b.read()  # read in file into c as a str
    # and write to fileout
    output = bytearray()
    input_to_byte = bytearray(c)
    if mode == "e":
        for b in input_to_byte:
            output.append(enc(b, key))
    if mode == "d":
        for b in input_to_byte:
            output.append(dec(b, key))
    #write the bytearray to the enc file 
    fout_b.write(output)

    # close all file streams
    fin_b.close()
    fout_b.close()



# our main function
if __name__ == "__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="filein", help="input file")
    parser.add_argument("-o", dest="fileout", help="output file")
    parser.add_argument("-k", dest="key", help="key", type=int)
    parser.add_argument("-m", dest="mode", help="encryption or decryption")
    # parse our arguments
    args = parser.parse_args()
    mode = args.mode
    key= args.key
    filein = args.filein
    fileout = args.fileout

    #check key 
    if((0 <= key <=255) == False):
        raise ValueError('The value of the key must be between 1 and that of 255')
    
    #check mode
    if((mode.lower()== "e" or mode.lower()=="d")):
        pass
    else:
        raise SyntaxError('The mode has to be only \"d" or \"e" case insensitive')
    #TODO input as the size of bytes 
    #TODO how many characters each byte shifted
    #TODO consider ASCII 256 
    #TODO write an enc and dec function + and - respectively


    doStuff(filein, fileout, key, mode.lower())

    # all done
