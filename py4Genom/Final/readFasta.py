#!/usr/bin/python3
import sys

def read_fasta(file_path):
    try:
        f = open(file_path)
        print('reading:', file_path)
    except IOError:
        print("File doesn't exists")
    seqs = {}
    for line in f:
        line = line.rstrip()
        if line[0] == '>':
            words = line.split()
            name = words[0][1:]
            seqs[name] = ''
        else:
            seqs[name] = seqs[name] + line
    f.close()
    return  seqs

def lengths(seqs):
    keys = seqs.keys()
    lengths = {}
    for key in keys:
        lengths[key] = len(seqs[key])
    return lengths
