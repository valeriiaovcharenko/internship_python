def sort_selection(list):
    length = len(list)
    for i in range(length):
        min_idx = i
        for j in range(i + 1, length):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

original_list = [80, 56, 23, 10, 57, 40]
sorted_list = sort_selection(original_list)
print("Sorted list:", sorted_list)
