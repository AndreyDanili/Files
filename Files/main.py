def get_number_lines():
    files = ['1.txt', '2.txt', '3.txt']
    number_lines = {}
    for document in files:
        with open(document) as file:
            lines = 0
            for line in file:
                lines += 1
            number_lines[document] = lines
    sorted_lines = dict(sorted(number_lines.items(), key=lambda x: x[1]))
    return sorted_lines


def get_merged_file(file_name):
    counted_lines = get_number_lines()
    with open(file_name, 'w') as file:
        for sorted_file in counted_lines:
            file.write(f'{sorted_file}\n')
            file.write(f'{counted_lines[sorted_file]}\n')
            with open(sorted_file) as document:
                for line in document:
                    file.write(f'{line.strip()}\n')


get_merged_file('final_file.txt')
