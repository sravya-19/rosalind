import config
download_name = 'rosalind_dna.txt'

in_file = open(config.input_location + download_name).readlines()
string = in_file[0].strip()

answer = '%r %r %r %r' % (string.count('A'), string.count(
    'C'), string.count('G'), string.count('T'))


with open(config.output_location + download_name, 'w+') as out_file:
    out_file.write(answer + '\n')
