def sum_even_index_multiply_last(arr):
    if not arr:
        return 0
    sum_even_index = sum(arr[i] for i in range(0, len(arr), 2))
    return sum_even_index * arr[-1]


print(sum_even_index_multiply_last([0, 1, 7, 2, 4, 8]))
print(sum_even_index_multiply_last([1, 3, 5]))
print(sum_even_index_multiply_last([6]))
print(sum_even_index_multiply_last([]))