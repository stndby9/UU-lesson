def calculate_structure_sum(data_structure):
    calculate_structure = []
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            if isinstance(key, str):
                calculate_structure.extend(calculate_structure_sum(len(key)))
            else:
                calculate_structure.extend(calculate_structure_sum(key))
            if isinstance(value, str):
                calculate_structure.extend(calculate_structure_sum(len(value)))
            else:
                calculate_structure.extend(calculate_structure_sum(value))
    elif isinstance(data_structure, (list, tuple)):
        for i in data_structure:
            calculate_structure.extend(calculate_structure_sum(i))
    elif isinstance(data_structure, str):
        calculate_structure.extend(calculate_structure_sum(len(data_structure)))
    elif isinstance(data_structure, set):
        for j in data_structure:
            calculate_structure.extend(calculate_structure_sum(j))
    else:
        calculate_structure.append(data_structure)
    return calculate_structure


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = sum(calculate_structure_sum(data_structure))
print(result)
