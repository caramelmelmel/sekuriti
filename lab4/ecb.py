#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.042 FCS
# Completed by: 
#Leong Yun Qin Melody 1004489

#Collaborated with: 
# Leon Tjandra 

from present import *
import argparse
import os
import sys
import math

nokeybits=80
blocksize=64

#we use present function and present_inv function from the present.py

#the key has to be converted to the integer
#READ FILE // 8 to get all the previous blocks
def pad_binary(binary, padding):
    # e.g.0b100 -> 0b00100  pads in the front
    return bin(binary)[2:].zfill(padding)

#convert binary to bytes
def binary_to_bytes(binary):
    return int(binary).to_bytes(8, byteorder='big')

#convert bytes back to bin
def bytes_to_bin(bytes):
    block_binary = ''
    for byte in bytes:
        block_binary += pad_binary(byte, 8)
    return block_binary

def binary_to_int(binary_str):
    return int(binary_str,2)


def ecb(infile,outfile,key,mode):
    input_file = open(infile,mode='rb')
    output_file = open(outfile,mode='wb')

    # the ecb mode works by dividing the blocks into chunks then cipher from there
    #number of 64 bits from there
    read_input = input_file.read()
    enc_byte = b''

    if mode.lower() == 'e':
        #sep out into blocks
        for i in range(math.ceil(len(read_input)/8)):
            block = read_input[i * 8:(i + 1)*8]
            if len(block) < 8:
                block = block.ljust(8, b'0')
            block_binary_string = bytes_to_bin(block)
            #convert to integer
            block_binary_int = binary_to_int(block_binary_string)
            encrypted_block = present(block_binary_int, key)
            enc_block_bytes = binary_to_bytes(encrypted_block)
            enc_byte += enc_block_bytes
        output_file.write(enc_byte)
    
    if mode.lower() == 'd':
        for i in range(math.ceil(len(read_input)/8)):
            block = read_input[i * 8:(i + 1)*8]
            if len(block) < 8:
                block = block.ljust(8, b'0')
            block_binary_string = bytes_to_bin(block)
            #convert to integer
            block_binary_int = binary_to_int(block_binary_string)
            encrypted_block = present_inv(block_binary_int, key)
            block_byte = binary_to_bytes(encrypted_block)
            
            #last block
            if i == len(read_input) // 8 - 1:
                        block_byte = block_byte.rstrip(b'0')
            enc_byte += block_byte
        output_file.write(enc_byte)

    print('finished writing to file')

    #good practice
    input_file.close()
    output_file.close()
    

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode = args.mode.lower()

    
    keyfile_handle = open(keyfile, 'r')
    keyfile_content = keyfile_handle.read()
    keyfile_content = keyfile_content.rstrip() #remove the last character if it is newline \n character
    try:
        key = int(keyfile_content, 16) #int with base 16 or hexadecimal value key
        if (0x00000000000000000000 <= key <= 0xFFFFFFFFFFFFFFFFFFFF == False):
            sys.exit("Key must be 80 bits") #Max Key size is 80 bits
    except ValueError: # Error for non numerical keys
        sys.exit("Value Error - Key must be in hexadecimal number form")

    ecb(infile,outfile,key,mode)




