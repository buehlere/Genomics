
import readFasta as rf
import ORF2 as orf
import sys

# Basic Analysis of Fasta
seqs = rf.read_fasta(sys.argv[1])
seq_lens = rf.lengths(seqs)
print('length of FASTA is ',len(seqs))
print('sequence lengths are: ',seq_lens.items())
print('longest sequence is: ', max(seq_lens, key=seq_lens.get),'with length of', seq_lens[max(seq_lens, key=seq_lens.get)])
print('shortest sequence is: ', min(seq_lens, key=seq_lens.get),'with length of', seq_lens[min(seq_lens, key=seq_lens.get)])

# ORF Analysis
a = orf.forward_reading(seqs[list(seqs.keys())[0]],2)
# ORF 2
seqs_subset = {key: seqs[key] for key in seqs_short}
longest_per_seq_two  = orf.longest_orf(seqs, 2)
max_info_two = orf.max_orf(longest_per_seq_two)
print(max_info_two['length'])
# ORF 3
longest_per_seq_three  = orf.longest_orf(seqs, 3)
max_info_three = orf.max_orf(longest_per_seq_three)
print(seqs[max_info_three['key']].find(max_info_three['orf']))
# ORF 1
longest_per_seq_one  = orf.longest_orf(seqs, 1)
max_info_one = orf.max_orf(longest_per_seq_one)

# longest orf for each reading and seq
print(max_info_one['length'])
print(max_info_two['length'])
print(max_info_three['length'])

# longest forward orf in gi|142022655|gb|EQ086233.1|16
print(len(longest_per_seq_one['gi|142022655|gb|EQ086233.1|16']))
print(len(longest_per_seq_two['gi|142022655|gb|EQ086233.1|16']))
print(len(longest_per_seq_three['gi|142022655|gb|EQ086233.1|16']))

# repeats
# n = 6
freq_repeats = orf.freq_repeats(seqs,6)
max = orf.find_max_repeats(freq_repeats)
print(max)
# n = 12
freq_repeats = orf.freq_repeats(seqs,12)
max = orf.find_max_repeats(freq_repeats)
print(max)
# n = 7 
freq_repeats = orf.freq_repeats(seqs,7)
max = orf.find_max_repeats(freq_repeats)
print(max)
