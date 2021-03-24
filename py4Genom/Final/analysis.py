
import readFasta as rf
import ORF as orf
import sys

# Basic Analysis of Fasta
seqs = rf.read_fasta(sys.argv[1])
seq_lens = rf.lengths(seqs)
print('length of FASTA is ',len(seqs))
print('sequence lengths are: ',seq_lens.items())
print('longest sequence is: ', max(seq_lens, key=seq_lens.get),'with length of', seq_lens[max(seq_lens, key=seq_lens.get)])
print('shortest sequence is: ', min(seq_lens, key=seq_lens.get),'with length of', seq_lens[min(seq_lens, key=seq_lens.get)])

# Analyze ORFs
orfs = orf.analyze_orf(sys.argv[1], 2)
name, max = orf.find_max_orf(orfs)
print(name, 'has the longest with length of:', len(max))

# REPEATS
repeats = orf.analyze_repeats(seqs, 12)
name, max = orf.find_max_re(repeats)
print(name,'is the sequence with the most repeates' max)
all_repeats = orf.most_occur(repeats)
max = 0
name = ""
for key in all_repeats:
    value = all_repeats.get(key)
    if value > max:
        max = value
        name = key
print(name, 'is the most ocurring repeat',max)
