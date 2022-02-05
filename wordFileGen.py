#Written by Bryson Carroll

import random as rd
import os

def generate_words():
    rd.seed()
    length = rd.randint(1,10)
    rand_string = ''
    for i in range(length):
        rand_string += chr(rd.randint(ord('a'), ord('z')))
    return rand_string

def generate_file():
    file_path = os.getcwd() + "/words.txt"
    fo = open(file_path, 'w')
    for i in range(1000):
        fo.write(generate_words() + '\n')
    fo.close

generate_file()