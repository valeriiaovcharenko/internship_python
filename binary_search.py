def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        middle = (left + right) // 2
        if sorted_list[middle] == target:
            return middle
        elif sorted_list[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

number_list = list(range(0, 100))
search_number = 80

result = binary_search(number_list, search_number)
print(f"The number we're searching for is {search_number}. Found at position {result}.")
