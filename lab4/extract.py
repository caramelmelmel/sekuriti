#!/usr/bin/env python3
# ECB plaintext extraction skeleton file for 50.042 FCS
# Leong Yun Qin Melody 1004489


import argparse
from collections import Counter

def getInfo(headerfile):
    header_file = open(headerfile,'rb')
    header = header_file.read()
    header_len = len(header)

    return header, header_len

def extract(infile,outfile,headerfile):
    header, header_len = getInfo(headerfile)
    encrypted = []
    fin = open(infile,'rb')
    frequency = -1
    fin.read(header_len +1)
    bool_non_empty_bytes = True
    decrypted = []
    fout = open(outfile,'wb')

    while bool_non_empty_bytes:
        byte_input = fin.read(8)
        if byte_input == b"":
            bool_non_empty_bytes = False
            break
        encrypted.append(byte_input)

    #count each of them then put into a dictionary
    freq_count = dict(Counter(encrypted))

    #loop thru the dict for the frequency of the values 
    for block,count in freq_count.items():
        #check for the highest count
        if count > frequency: 
            highest_freq_block = block
            frequency = count
    
    for block in encrypted:
        if block == highest_freq_block:
            bin = b'0' * 8
        else:
            bin = b'1' * 8
        decrypted.append(bin.decode())

    decrypted = ''.join(decrypted).encode()
    fout.write(header)
    fout.write(b'\n')
    fout.write(decrypted)
    return True 

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Extract PBM pattern.')
    parser.add_argument('-i', dest='infile',help='input file, PBM encrypted format')
    parser.add_argument('-o', dest='outfile',help='output PBM file')
    parser.add_argument('-hh', dest='headerfile',help='known header file')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    headerfile=args.headerfile

    print('Reading from: %s'%infile)
    print('Reading header file from: %s'%headerfile)
    print('Writing to: %s'%outfile)

    success=extract(infile,outfile,headerfile)

            
