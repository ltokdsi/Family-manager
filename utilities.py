def date_to_number(date_str):
    """Функция конвертации строкового представления даты в числовое
    для сравнения"""
    day, month, year = date_str.split('.')
    return int(year) * 10000 + int(month) * 100 + int(day)

def read_tasks(filename):
    """Функция чтения базы данных из текстового файла"""
    tasks = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    info = line.split(';')
                    if len(info) == 7:
                        task_dictionary = {
                            'дата_выдачи': info[0],
                            'время_выдачи': info[1],
                            'дата_выполнения': info[2],
                            'время_выполнения': info[3],
                            'исполнитель': info[4],
                            'описание': info[5],
                            'статус': info[6],
                        }
                        tasks.append(task_dictionary)
    except FileNotFoundError:
        return None
    return tasks
