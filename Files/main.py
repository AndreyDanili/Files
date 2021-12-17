files = ['1.txt', '2.txt', '3.txt']
number_lines = {}
for document in files:
    with open(document) as file:
        lines = 0
        for line in file:
            lines += 1
        number_lines[document] = lines
sorted_lines = dict(sorted(number_lines.items(), key=lambda x: x[1]))

with open('final_file.txt', 'w') as file:
    for sorted_file in sorted_lines:
        file.write(f'{sorted_file}\n')
        file.write(f'{sorted_lines[sorted_file]}\n')
        with open(sorted_file) as document:
            for line in document:
                file.write(f'{line.strip()}\n')
