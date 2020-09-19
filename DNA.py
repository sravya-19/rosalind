
input_location = 'downloads/rosalind_dna.txt'

file = open(input_location).readlines()
string = file[0].strip()

print('%r %r %r %r' % (string.count('A'), string.count(
    'C'), string.count('G'), string.count('T')))
