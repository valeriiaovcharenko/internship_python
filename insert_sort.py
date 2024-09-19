def insertion_sort_descending(data):
    for index in range(1, len(data)):
        current_element = data[index]
        current_position = index
        while current_position > 0 and current_element[1] > data[current_position - 1][1]:
            data[current_position] = data[current_position - 1]
            current_position -= 1
        data[current_position] = current_element
    return data

data_list_1 = [
    ("kate", 23),
    ("inna", 18),
    ("lero", 52),
    ("bob", 100),
    ("joie", 36),
    ("ana", 247)
]

def insertion_sort_ascending(data):
    for index in range(1, len(data)):
        current_element = data[index]
        current_position = index
        while current_position > 0 and current_element[1] < data[current_position - 1][1]:
            data[current_position] = data[current_position - 1]
            current_position -= 1
        data[current_position] = current_element
    return data

data_list_2 = [
    ("anna", 95),
    ("bob", 123),
    ("charlie", 45),
    ("david", 342),
    ("eva", 210),
    ("frank", 58)
]

sorted_descending = insertion_sort_descending(data_list_1)
sorted_ascending = insertion_sort_ascending(data_list_2)

print(f"DESC: {sorted_descending}\nASC: {sorted_ascending}")
