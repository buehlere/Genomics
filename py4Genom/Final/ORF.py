#!/usr/bin/python3
from readFasta import read_fasta

def forward_reading(seq, reader_choice):
    # print(seq)
    # reader 1
    reader1 = [seq[i:i+3] for i in range(0, len(seq), 3)]
    # reader 2
    reader2 = [seq[i:i+3]  for i in range(1, len(seq), 3)]
    reader2.insert(0,seq[0])
    # reader 3
    reader3 = [seq[i:i+3] for i in range(2, len(seq), 3)]
    reader3.insert(0,seq[0:2])
    if reader_choice == 1:
        return reader1
    elif reader_choice == 2:
        return reader2
    elif reader_choice == 3:
        return reader3

def find_orf(reader):
    i = 0
    start_i = ""
    end_i = 0
    orfs = []
    for strand in reader:
        if strand == "ATG":
            start_i = i
        if strand in ["TAA", "TAG", "TGA"] and start_i != "":
            end_i = i + 1
            orfs.append(''.join(reader[start_i:end_i]))
        i += 1
    return(orfs)

def analyze_orf(file, reader_choice):
    # orfs = []
    orfs = {}
    seqs = read_fasta(file)
    # print(seqs)
    for key in seqs:
        reader = forward_reading(seqs[key], reader_choice)
        orfs[key] = find_orf(reader)
    return orfs

def find_max_orf(orfs):
    seq_name = ""
    file_max = ""
    for key in orfs:
        seq = orfs[key]
        #print(orfs[key])
        seq_max = ""
        for i in seq:
            if len(i) > len(seq_max):
                seq_max = i
        print(key, 'longest ORF is:', len(seq_max))
        if len(seq_max) > len(file_max):

            file_max = seq_max
            seq_name = key
    return seq_name, file_max

def find_repeats(seq, n):
    repeats = {}
    for i in range(0, len(seq)):
        repeat = seq[i:i+n] # generate possible repeats
        if len(repeat) == n:
            if repeat not in repeats:
                repeats[repeat] = 1 # initiate record
            else:
                # count repeated repeats
                repeats[repeat] = repeats.get(repeat) + 1
    return repeats

def analyze_repeats(seqs, n):
    repeats = {}
    for key in seqs:
        repeats[key] = find_repeats(seqs[key], n)
    return repeats

def most_occur(seqs):
    file_repeats = {}
    for seq in seqs:
        seq_re = seqs.get(seq)
        for repeat in seq_re:
            number = seq_re.get(repeat)
            if repeat not in file_repeats:
                file_repeats[repeat] = number  # initiate record
            else:
                # count repeated repeats
                file_repeats[repeat] = file_repeats.get(repeat) + number
    return file_repeats

def find_max_re(repeats):
    seq_name = ""
    file_max = 0
    for key in repeats:
        seq_max = list(repeats[key].items())
        seq_max = [x[1] for x in seq_max]
        # for i in range(0, len(seq_max)):
        #     seq_max[i] = int(seq_max[i])
        seq_max = max(seq_max)
        if seq_max > file_max:
            file_max = seq_max
            seq_name = key
    return seq_name, file_max
#(ATG), and ends with a stop codon (TAA, TAG or TGA). For instance, ATGAAATAG is an ORF of length 9.

# Given an input reading frame on the forward strand (1, 2, or 3) your program should be able to
#identify all ORFs present in each sequence of the FASTA file, and answer the following questions:
#what is the length of the longest ORF in the file? What is the identifier of the sequence
#containing the longest ORF? For a given sequence identifier,
#what is the longest ORF contained in the sequence represented by that identifier?
#What is the starting position of the longest ORF in the sequence that contains it?
#The position should indicate the character number in the sequence.
#For instance, the following ORF in reading frame 1:
