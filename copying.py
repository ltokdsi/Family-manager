def copy_list(original_list):
    """Функция создания глубокой копии списка словарей"""
    new_list = []
    for item in original_list:
        new_item = {}
        for key, value in item.items():
            new_item[key] = value
        new_list.append(new_item)
    return new_list
