from datetime import datetime
import json


def add():
    notes = read_notes()
    note = {
        'id': len(notes) + 1,
        'title': input_title(),
        'msg': input_body(),
        'data': datetime.now().strftime('%d.%m.%Y'),
        'editData': None
    }
    notes.append(note)
    save(notes)
    return 'Заметка добавлена.'

def input_title():
    return input('Введите заголовок заметки: ').title()

def input_body():
    return input('Введите тело заметки: ').title()


def delete(id):
    notes = read_notes()
    note_to_delete = None
    for note in notes:
        if note['id'] == id:
            note_to_delete = note
            break
    if note_to_delete:
        notes.remove(note_to_delete)
        save(notes)
        return f'Заметка {id} удалена!'
    else:
        return 'Заметка не найдена!'
    
def read_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
        return notes
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f'Ошибка при чтении заметки: {e}')
        return []
    
def save(notes):
    try:
        with open('notes.json', 'w') as file:
            json.dump(notes, file)
    except Exception as e:
        print(f'Ошибка при сохранении заметки: {e}')

def edit(id, title, body):
    notes = read_notes()
    for note in notes:
        if note['id'] == id:
            note['title'] = title
            note['msg'] = body
            note['editData'] = datetime.now().strftime('%d.%m.%Y')
            save(notes)
            return 'Успешно отредактировано!'
    return 'Заметка не найдена!'

def print_notes():
    notes = read_notes()
    for note in notes:
        print(note)

def print_note(id):
    id = int(id)
    notes = read_notes()
    for note in notes:
        if note['id'] == id:
            print(note)

def filter():
    start_date = datetime.strptime(input('Начальная дата (ДД.ММ.ГГГГ): '), '%d.%m.%Y')
    end_date = datetime.strptime(input('Конечная дата (ДД.ММ.ГГГГ): '), '%d.%m.%Y')  
        
    filtered_notes = []
    for note in read_notes():
        created_date = datetime.strptime(note['data'], '%d.%m.%Y')
        updated_date = created_date
        if note['editData']:
            updated_date = datetime.strptime(note['editData'], '%d.%m.%Y')            
        if start_date <= created_date <= end_date or start_date <= updated_date <= end_date:
            filtered_notes.append(note)
    for note in filtered_notes:
            print(note)

def main():
    print ('Меню пользователя: \n'
               '1. Добавить заметку\n'
               '2. Редактировать заметку\n'
               '3. Удалить заметку\n'
               '4. Показать список всех заметок\n'
               '5. Показать одну заметку\n'
               '6. Фильтр по дате\n'
               '7. Выход\n')
    while True:
        command=input('Выберите необходимую команду: ')

        while command not in('1', '2', '3', '4', '5', '6', '7'):
            print('Некорректный ввод, повторите запрос')
            command=input('Выберите необходимую команду: ')
    
        match command:
            case "1":
                print(add())
            case "2":
                id = int(input('Введите ID заметки: '))
                title = input('Новый заголовок заметки: ')
                body = input('Новое тело заметки: ')
                print(edit(id, title, body))
            case "3":
                id = int(input('Введите ID заметки для удаления: '))
                print(delete(id))
            case "4":
                print_notes()
            case "5":
                print_note(input('Введите ID: '))
            case "6":
                filter()
            case "7":
                print('Завершение программы')
        print() 

main()
