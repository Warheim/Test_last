from Functions_work import *


def doc_people(doc_number: str):
    result = 0
    for ask in documents:
        if doc_number in ask.values():
            result = ask['name']
            return result
    if result == 0:
        return 'Неверный номер!'


def doc_shelf(doc_number: str):
    result = 0
    for key, value in directories.items():
        if doc_number in value:
            result = key
            return result
    if result == 0:
        return 'Неверный номер!'


def doc_list():
    res = []
    for ask in documents:
        step = f'{ask["type"]} {ask["number"]} {ask["name"]}'
        res.append(step)
    return res


def doc_add(add_shelf: str, add_type: str, add_number: str, add_name: str):
    if add_shelf in directories.keys() and add_type and add_number and add_name:
        documents.append({'type': add_type, 'number': add_number, 'name': add_name})
        for key, value in directories.items():
            if key == add_shelf:
                value.append(add_number)
    else:
        return 'Неверный номер!'


def doc_delete(doc_number: str):
    control = []
    for ask in directories.values():
        for look in ask:
            if look == doc_number:
                control.append(look)
                ask.remove(look)
    for task in documents:
        if task['number'] == doc_number:
            return documents.remove(task)
    if len(control) == 0:
        return 'Неверный номер!'


def doc_move():
    def enter_number(doc_number: str):
        temp = []
        for ask in directories.values():
            for task in ask:
                temp.append(task)
        if doc_number in temp:
            for ask in directories.values():
                for task in ask:
                    if task == doc_number:
                        result = doc_number
                        ask.remove(task)
                        return result
        else:
            return 'Неверный номер!'

    def enter_shelf(add_shelf: str):
        if add_shelf in directories.keys():
            return add_shelf
        else:
            return 'Неверный номер!'

    number = enter_number(input('Введите номер документа: '))
    shelf = enter_shelf(input('Введите номер полки: '))

    for key, value in directories.items():
        if key == shelf:
            value.append(number)
    return f'Документ перемещён.'


def doc_add_shelf(add_shelf: str):
    if add_shelf not in directories.keys():
        directories[add_shelf] = []
        return f'Полка {add_shelf} создана.'
    else:
        return 'Неверный номер!'




