import utilities


def compare_report_1(task1,task2):
    """Сравнение для отчета 1: дата выдачи(убывание) + статус"""
    date1 = utilities.date_to_number(task1['дата_выдачи'])
    date2 = utilities.date_to_number(task2['дата_выдачи'])

    if date1 < date2:
        return 1
    elif date1 > date2:
        return -1
    else:
        status_order = {
            'успешно выполнена': 1,
            'в процессе': 2,
            'получена': 3,
            'провалена': 4
        }
        status_priority1 = status_order.get(task1['статус'],5)
        status_priority2 = status_order.get(task2['статус'],5)
        if status_priority1 > status_priority2:
            return 1
        elif status_priority1 < status_priority2:
            return -1
        else:
            return 0

def compare_report_2(task1,task2):
    """Сравнение для отчета 2: дата выполнения(убывание) +
    описание(возрастание)"""
    date1 = utilities.date_to_number(task1['дата_выполнения'])
    date2 = utilities.date_to_number(task2['дата_выполнения'])

    if date1 < date2:
        return 1
    elif date1 > date2:
        return -1
    else:
        if task1['описание'].lower() > task2['описание'].lower():
            return 1
        elif task1['описание'].lower() < task2['описание'].lower():
            return -1
        else:
            return 0

def compare_report_3(task1,task2):
    """Сравнение для отчета 3:исполнитель(возрастание) +
    дата выполнения(возрастание)"""
    name1 = task1['исполнитель'].lower()
    name2 = task2['исполнитель'].lower()

    if name1 > name2:
        return 1
    elif name1 < name2:
        return -1
    else:
        date1 = utilities.date_to_number(task1['дата_выполнения'])
        date2 = utilities.date_to_number(task2['дата_выполнения'])
        if date1 > date2:
            return 1
        elif date1 < date2:
            return -1
        else:
            return 0
