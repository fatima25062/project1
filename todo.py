# todo.py
# Простое консольное приложение для управления списком задач
# Каждая задача хранится как словарь: {'title': str, 'completed': bool}

tasks = []  # глобальный список задач

def show_tasks():
    """Отображает все задачи с их статусом и номерами."""
    if not tasks:
        print("Список задач пуст.")
    else:
        for i, task in enumerate(tasks, 1):
            status = '✓' if task['completed'] else ' '
            print(f"{i}. [{status}] {task['title']}")

def add_task(title):
    """Добавляет новую задачу (по умолчанию не выполнена)."""
    tasks.append({'title': title, 'completed': False})
    print(f"Задача '{title}' добавлена.")

def delete_task(index):
    """Удаляет задачу по её номеру (индексу + 1)."""
    try:
        removed = tasks.pop(index - 1)
        print(f"Задача '{removed['title']}' удалена.")
    except IndexError:
        print("Ошибка: задачи с таким номером не существует.")

def mark_done(index):
    """Отмечает задачу как выполненную."""
    try:
        tasks[index - 1]['completed'] = True
        print(f"Задача '{tasks[index - 1]['title']}' отмечена как выполненная.")
    except IndexError:
        print("Ошибка: задачи с таким номером не существует.")

if __name__ == "__main__":
    while True:
        print("\n--- Меню ---")
        print("1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Выход")
        choice = input("Выберите действие (1-5): ").strip()

        if choice == '1':
            show_tasks()

        elif choice == '2':
            title = input("Введите текст задачи: ").strip()
            if title:
                add_task(title)
            else:
                print("Задача не может быть пустой.")

        elif choice == '3':
            try:
                idx = int(input("Введите номер задачи для отметки: "))
                mark_done(idx)
            except ValueError:
                print("Ошибка: введите целое число.")

        elif choice == '4':
            try:
                idx = int(input("Введите номер задачи для удаления: "))
                delete_task(idx)
            except ValueError:
                print("Ошибка: введите целое число.")

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите пункт из меню.")