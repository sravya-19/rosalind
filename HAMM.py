import file_process as fp
input_file = 'rosalind_hamm.txt'

string1, string2 = fp.read_file(input_file).split('\n')

zipped_list = zip(list(string1), list(string2))

count = 0
for tup in zipped_list:
    if tup[0] != tup[1]:
        count += 1

fp.write_file(input_file, str(count))
