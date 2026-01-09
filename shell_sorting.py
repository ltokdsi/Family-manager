def shell_sort(array,compare_func):
    """Реализация сортировки Шелла с использованием
    функции сравнения"""
    length = len(array)
    gap = length//2
    while gap > 0:
        for current_index in range(gap, length):
            temp = array[current_index]
            insert_position = current_index
            while (insert_position >= gap and
                   compare_func(array[insert_position - gap],
                                temp) > 0):
                array[insert_position] = array[insert_position - gap]
                insert_position -= gap
            array[insert_position] = temp
        gap //= 2
