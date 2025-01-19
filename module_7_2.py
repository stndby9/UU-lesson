import pprint


def custom_write(file_name, strings):
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')
    for line_number in range(len(strings)):
        line = strings[line_number]
        byte_position = file.tell()
        file.write(line + '\n')
        strings_positions[(line_number + 1, byte_position)] = line

    return strings_positions


info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
