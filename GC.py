import file_process as fp
input_file = 'rosalind_gc.txt'


def get_gc_content(string):
    return (string.count('G') + string.count('C')) / float(len(string))

dna_strings = fp.read_fasta(input_file)
max_gc = 0.0
max_gc_string = ''

for name in dna_strings:
    gc_content = get_gc_content(dna_strings[name])
    print(gc_content, max_gc)
    if gc_content > max_gc:
        max_gc = gc_content
        max_gc_name = name

answer = '%s\n%2.6f' % (max_gc_name, max_gc * 100)

fp.write_file(input_file, answer)
