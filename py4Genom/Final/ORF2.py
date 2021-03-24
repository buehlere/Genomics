#!/usr/bin/python3
from readFasta import read_fasta

def forward_reading(seq, reader_choice):
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
    orfs = []
    for i in range(0,len(reader)):
        if reader[i] == "ATG":
            for j in range(i,len(reader)):
                if reader[j] in ["TAA", "TAG", "TGA"]:
                    orfs.append("".join(reader[i:j+1])) # remove j+1
                    break
    return(orfs)

def longest_orf(seqs, reading):
    # dict for value pair
    longest = {}
    # for every seq in sequences
    for key, value in seqs.items():
        # forward reading:
        forward = forward_reading(value, reading)
        # find orfs
        orfs = find_orf(forward)
        # find longest orf
        max = 0
        max_orf = ''
        for orf in orfs:
            if(len(orf) > max):
                max = len(orf)
                max_orf = orf
        longest.update({key:max_orf})
    return(longest)

def max_orf(longest_per_seq):
    max_len = 0
    max_key = ''
    max_orf = []
    for key, value in longest_per_seq.items():
        if max_len < len(value):
            max_len = len(value)
            max_key = key
            max_orf = value
    max_info = {'length' : max_len, 'key': max_key, 'orf': max_orf}
    return(max_info)

def find_repeats(seqs, n):
    all_repeats = []
    for key, value in seqs.items():
        seq = value
        repeats = []
        for i in range(0,len(seq),1):
            snip = seq[i:i+n]
            if len(snip) == n:
                repeats.append(snip)
        for j in repeats:
            all_repeats.append(j)
    return(all_repeats)

def freq_repeats(seqs, n):
    repeat_dict = {}
    all_repeats = find_repeats(seqs, n)
    for i in range(0,len(all_repeats),1):
        if all_repeats[i] not in repeat_dict:
            for j in range(i+1,len(all_repeats),1):
                if all_repeats[i] == all_repeats[j]:
                    if all_repeats[i] not in repeat_dict:
                        repeat_dict.update({all_repeats[i]:2})
                    else:
                        repeat_dict[all_repeats[i]] += 1
    return(repeat_dict)

def find_max_repeats(freq_repeats):
    max_value = max(freq_repeats.values())  # maximum value
    max_keys = [k for k, v in freq_repeats.items() if v == max_value]
    return({'value':max_value,'keys':max_keys})
