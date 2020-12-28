import config


def read_file(input_file):
    in_file = open(config.input_location + input_file).read()
    return in_file.strip()


def write_file(output_file, answer_string):
    with open(config.output_location + output_file, 'w+') as out_file:
        out_file.write(answer_string + '\n')


def read_fasta(input_file):
    answer = {}
    strings = read_file(input_file).split('>')
    strings = [string for string in strings if string != '']

    fasta = {}

    for string in strings:
        string_split = string.split('\n')
        fasta[string_split[0]] = ''.join(string_split[1:])

    return fasta
