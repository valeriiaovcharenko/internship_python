def quicksort(q_list):
    if len(q_list) < 2:
        return q_list
    else:
        pivot = q_list[0]
        less = [element for element in q_list[1:] if element <= pivot]
        greater = [element for element in list[1:] if element > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

original_list = [15, 47, 65, 80, 1, 10, 30, 52, 56]
sorted_numbers = quicksort(original_list)

print("A sorted string of numbers:", sorted_numbers)
