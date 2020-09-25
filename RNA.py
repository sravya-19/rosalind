import config
download_name = 'rosalind_rna.txt'

in_file = open(config.input_location + download_name).readlines()
string = in_file[0].strip()

string = string.replace('T', 'U')

with open(config.output_location + download_name, 'w+') as out_file:
    out_file.write(string + '\n')
