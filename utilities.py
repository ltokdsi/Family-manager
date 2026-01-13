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
                if not line:
                    continue
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
        print('Файл не найден! Создаю новую базу данных')
        with open(filename, 'w', encoding='utf-8') as file:
            pass
        return []
    return tasks

def add_task_to_file(filename, task):
    """Добавление строки в файл"""
    try:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                if file.read().strip():
                    is_empty = False
        except FileNotFoundError:
            is_empty = True
        with open(filename, 'a', encoding='utf-8') as file:
            if is_empty:
                prefix = ""
            else:
                prefix = "\n"
            line = (f"{prefix}{task['дата_выдачи']};"
                    f"{task['время_выдачи']};"
                    f"{task['дата_выполнения']};"
                    f"{task['время_выполнения']};"
                    f"{task['исполнитель']};{task['описание']};"
                    f"{task['статус']}")
            file.write(line)
        return True
    except Exception as e:
        print(f"Ошибка при записи: {e}")
        return False


def save_all_tasks(filename, tasks):
    """Полная перезапись файла (для удаления)"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for task in tasks:
                line = (f"\n{task['дата_выдачи']};"
                        f"{task['время_выдачи']};"
                        f"{task['дата_выполнения']};"
                        f"{task['время_выполнения']};"
                        f"{task['исполнитель']};{task['описание']};"
                        f"{task['статус']}")
                file.write(line)
        return True
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")
        return False

def validate_date(date_str):
    """Проверка на реальность даты"""
    try:
        parts = date_str.split('.')
        if len(parts) != 3:
            return False
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
        if not (1 <= day <= 31):
            return False
        if not (1 <= month <= 12):
            return False
        if not (1900 <= year <= 2100):
            return False
        if month == 2 and day > 29:
            return False
        return True
    except (ValueError, IndexError):
        return False

def validate_time(time_str):
    """Проверка формата ЧЧ:ММ и реальность времени"""
    try:
        if ':' not in time_str:
            return False
        parts = time_str.split(':')
        if len(parts) != 2:
            return False
        hours = int(parts[0])
        minutes = int(parts[1])
        if (0 <= hours <= 23) and (0 <= minutes <= 59):
            return True
        return False
    except (ValueError, IndexError):
        return False

def validate_name(name):
    """Проверяет, что имя состоит только из букв"""
    cleaned_name = name.replace(' ', '')
    if not cleaned_name:
        return False
    return cleaned_name.isalpha()
