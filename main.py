import copying
import logic
import shell_sorting
import utilities
import data_editor


def print_tasks(tasks, tittle):
    """Универсальная функция для вывода списка задач"""
    print(tittle)
    if not tasks:
        print('Список пуст или задачи не найдены')
    else:
        for count, task in enumerate(tasks,1):
            print(f"{count}){task['дата_выдачи']} "
                  f"{task['время_выдачи']} -> "
                  f"{task['дата_выполнения']} "
                  f"{task['время_выполнения']} | "
                  f"{task['исполнитель']} | "
                  f"{task['описание']} | {task['статус']}")
    input('Нажмите Enter для возвращения в главное меню ')

print('Добро пожаловать в программу "Семейный менеджер"!')
def show_menu():
    """Функция для отображения интерфейса и получения выбора"""
    print('ГЛАВНОЕ МЕНЮ')
    print('Действия:')
    print('1. Отчет 1: Список задач за прошедшие N дней')
    print('2. Отчет 2: Проваленные задачи')
    print('3. Отчет 3: Активные задачи (получена или в процессе)')
    print('4. Просмотреть исходный список')
    print('5. Добавить новую задачу')
    print('6. Удалить существующую задачу')
    print('7. Выход из программы')

    while True:
        choice = input('Выберите действие (1-7): ').strip()
        if choice in ['1','2','3','4','5','6','7']:
            return choice
        print('Некорректный ввод! Введите число от 1 до 7')

def main():
    """Главная функция программы "Семейный менеджер",
     отображающая меню, обрабатывающая выбор пользователя"""
    original_data = utilities.read_tasks('family_tasks.txt')
    if not original_data:
        print('База данных сейчас пуста. Но вы можете использовать '
              'пункт 5, чтобы добавить задачи')
    while True:
        user_choice = show_menu()
        if user_choice == '7':
            print('Программа успешно завершена! До свидания!')
            break

        working_tasks = copying.copy_list(original_data)

        if user_choice == '1':
            print('Отчет 1. Список задач за прошедшие N дней')

            while True:
                today_input = input('Введите сегодняшнюю дату '
                                    '(ДД.ММ.ГГГГ) или 0 '
                                    'для отмены: ').strip()
                if today_input == '0':
                    current_date_number = None
                    break
                if utilities.validate_date(today_input):
                    current_date_number = (
                        utilities.date_to_number(today_input))
                    break
                else:
                    print('Ошибка! Введите дату корректно в формате '
                          '(ДД.ММ.ГГГГ). Помните: в месяце 1-12, '
                          'а дней 1-31! Год от 1900 до 2100!')
            if today_input == '0':
                continue

            number_of_days = None
            while True:
                number_of_days_string = input('Введите число дней N '
                                   '(или 0 для отмены): ')
                if number_of_days_string == '0':
                    number_of_days = None
                    break
                if not number_of_days_string.isdigit():
                    print('Введите целое положительное число!')
                    continue
                number_of_days = int(number_of_days_string)
                if number_of_days < 0:
                    print('Введите целое положительное число!')
                    number_of_days = None
                    continue
                break

            if number_of_days is None:
                continue

            filtered = []
            for task in working_tasks:
                task_date = (
                    utilities.date_to_number(task['дата_выдачи']))
                if current_date_number - task_date < number_of_days:
                    if current_date_number >= task_date:
                        filtered.append(task)
            shell_sorting.shell_sort(filtered, logic.compare_report_1)
            print_tasks(filtered, f"Задачи за последние "
                                  f"{number_of_days} дней")

        elif user_choice == '2':
            print('Отчет 2. Проваленные задачи')
            all_names = []
            for task in original_data:
                names = task['исполнитель'].lower()
                if names not in all_names:
                    all_names.append(names)
            while True:
                print(f"Доступные имена: {', '.join(all_names)}")
                name = input('Введите имя члена семьи:'
                             ' (0 для отмены) ').strip()
                if name == '0':
                    print('Действие отменено')
                    break
                if name.lower() in all_names:
                    break
                else:
                    print('Некорректное имя! Попробуйте снова')
            if name == '0':
                continue

            filtered = []
            for current_task in working_tasks:
                if (current_task['исполнитель'].lower() ==
                        name.lower()):
                    if current_task['статус'] == 'провалена':
                        filtered.append(current_task)
            shell_sorting.shell_sort(filtered, logic.compare_report_2)
            print_tasks(filtered,
                        f'Проваленные задачи исполнителя {name}')

        elif user_choice == '3':
            print('Отчет 3. Активные задачи (получена или '
                  'в процессе)')
            filtered = []
            for current_task in working_tasks:
                current_status = current_task['статус']
                if (current_status == 'получена' or
                        current_status == 'в процессе'):
                    filtered.append(current_task)
            shell_sorting.shell_sort(filtered,
                                     logic.compare_report_3)
            print_tasks(filtered, 'Список активных задач')

        elif user_choice == '4':
            print_tasks(original_data, 'Исхдный список '
                                       'без сортировок')
        elif user_choice == '5':
            (data_editor.add_new_task
             ('family_tasks.txt', original_data))
            original_data = utilities.read_tasks('family_tasks.txt')

        elif user_choice == '6':
            original_data = data_editor.delete_task('family_tasks.txt'
                                                    , original_data)
if __name__ == '__main__':
    main()
