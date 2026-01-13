import utilities


def add_new_task(filename, current_tasks):
    """Функция для добавления новой задачи в базу данных"""
    print('Добавление новой задачи')
    # дата выдачи
    date_out = input('Дата выдачи (ДД.ММ.ГГГГ) '
                     '(или 0 для отмены): ').strip()
    if date_out == '0':
        return print('Отмена записи')
    while not utilities.validate_date(date_out):
        date_out = ((input('Ошибка! Введите дату корректно '
                          '(ДД.ММ.ГГГГ) (или 0 для отмены): '))
                    .strip())
        if date_out == '0':
            return print('Отмена записи')

    # время выдачи
    time_out = input('Время выдачи (ЧЧ:ММ) '
                     '(или 0 для отмены): ').strip()
    if time_out == '0':
        return print('Отмена записи')
    while not utilities.validate_time(time_out):
        time_out = input('Ошибка! Введите время корректно (ЧЧ:ММ)'
                         ' (или 0 для отмены): ').strip()
        if time_out == '0':
            return print('Отмена записи')

    # дата исполнения
    date_of_completion = input('Дата исполнения (ДД.ММ.ГГГГ) '
                               '(или 0 для отмены): ').strip()
    if date_of_completion == '0':
        return print('Отмена записи')
    while not utilities.validate_date(date_of_completion):
        date_of_completion = (
            input('Ошибка! Введите дату корректно (ДД.ММ.ГГГГ)'
                  ' (или 0 для отмены): ')).strip()
        if date_of_completion == '0':
            print('Отмена записи')

    # время исполнения
    execution_time = input('Время исполнения (ЧЧ:ММ) '
                           '(или 0 для отмены): ').strip()
    if execution_time == '0':
        return print('Отмена записи')
    while not utilities.validate_time(execution_time):
        execution_time = (
            input('Ошибка! Введите время корректно (ЧЧ:ММ)'
                  ' (или 0 для отмены): ')).strip()
        if execution_time == '0':
            return print('Отмена записи')

    # проверка логики дат
    date_out_num = utilities.date_to_number(date_out)
    date_comp_num = utilities.date_to_number(date_of_completion)
    if date_comp_num < date_out_num:
        print('\nОшибка! Дата выполнения не может '
              'быть раньше даты выдачи.')
        print('Запись отменена')
        return
    if date_comp_num == date_out_num:
        time_out_num = int(time_out.replace(':',''))
        time_comp_num = int(execution_time.replace(':',''))
        if time_comp_num < time_out_num:
            print('Время выполнения не может быть раньше '
                  'времени выдачи (если это один день)!')
            print('Запись отменена')
            return

    # исполнитель
    while True:
        display_names = []
        for task in current_tasks:
            name = task['исполнитель'].capitalize()
            if name not in display_names:
                display_names.append(name)
        print(f"Уже есть в базе: {display_names}")
        name = input('Введите исполнителя '
                     '(или 0 для отмены): ').strip()
        if name == '0':
            print('Отмена записи')
            return
        if not utilities.validate_name(name):
            print('Имя должно содерать только буквы!')
            continue
        final_name = ""
        found = False
        for task in current_tasks:
            original_name = task['исполнитель']
            if original_name.lower() == name.lower():
                final_name = original_name
                found = True
                break
        if not found:
            temp_name = name.capitalize()
            while True:
                confirm = input(f"Имени {temp_name} нет в списке."
                                f" Добавить как новое?"
                                f" (y/n) (0-отмена): ")
                if confirm.lower() == 'y':
                    final_name = temp_name
                    print(f"Исполнитель определен как: "
                          f"{final_name} (новое имя)")
                    break
                elif confirm.lower() == 'n' or confirm == '0':
                    final_name = None
                    break
                else:
                    print('Неккоректный ввод! Введити y или n.'
                          ' (или 0 для отмены)')
            if final_name:
                break
            else:
                if confirm == '0':
                    print('Отмена записи')
                    return
                print('Введите имя заново: ')
                continue
        else:
            print(f"Исполнитель определен как: {final_name}")
            break

    # описание
    description = (
        input('Введите описание задачи (что нужно сделать)'
              ' (или 0 для отмены): ').strip())
    if description == '0':
        print('Отмена записи')
        return
    while not description:
        description = input('Описание не может быть пустым!'
                            ' Введите задачу или 0.')
        if description == '0':
            print('Отмена записи')
            return

    # статус
    while True:
        print('\nВыберите статус задачи:')
        print('1. получена (по умолчанию)')
        print('2. в процессе')
        print('3. успешно выполнена')
        print('4. провалена')
        choice = input('Введите номер (1-4, или 0 для отмены)'
                       ' или Enter (оставить получена): ').strip()
        if choice == '0':
            print('Отмена записи')
            return
        elif choice == '1' or choice == '':
            status = "получена"
            break
        elif choice == '2':
            status = "в процессе"
            break
        elif choice == '3':
            status = "успешно выполнена"
            break
        elif choice == '4':
            status = "провалена"
            break
        else:
            print('Введите только цифру от 1 до 4 или 0')

    new_task = {
        'дата_выдачи':date_out, 'время_выдачи': time_out,
        'дата_выполнения': date_of_completion,
        'время_выполнения': execution_time, 'исполнитель': final_name,
        'описание': description, 'статус' : status
    }
    if utilities.add_task_to_file(filename, new_task):
        print(f"Успешно. Задача для {final_name} добавлена в файл.")

def delete_task(filename, tasks):
    """Функция для удаления существующей записи из файла"""
    print('\nУдаление записи')
    if not tasks:
        print('База пустая, удалять нечего')
        return tasks

    for count, task in enumerate(tasks, 1):
        print(f"{count}){task['дата_выдачи']} "
              f"{task['время_выдачи']} -> "
              f"{task['дата_выполнения']} "
              f"{task['время_выполнения']} | "
              f"{task['исполнитель']} | "
              f"{task['описание']} | {task['статус']}")
    while True:
        try:
            user_input = int(input('\nВведите номер задачи для '
                                   'удаления (или 0 для отмены): '))
            if user_input == 0:
                print('Удаление отменено')
                return tasks
            choice = int(user_input)
            if 0 < choice <=len(tasks):
                removed = tasks.pop(choice - 1)
                if utilities.save_all_tasks(filename, tasks):
                    print(f"Запись  {choice}){removed['исполнитель']}"
                          f"; {removed['описание']} удалена")
                return tasks
            else:
                print('Задачи с таким номером не существует')
        except ValueError:
            print('Ошибка! Введите целое число!')
