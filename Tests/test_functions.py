import unittest
from Functions import *
from Functions_work import *


class TestFunc(unittest.TestCase):
    """Создаём объекты для простоты тестирования нахождения в них элементов"""
    def setUp(self):
        self.people = []
        for person in documents:
            self.people.append(person['name'])
        self.people.append('Неверный номер!')
        self.doc_number = []
        for number in documents:
            self.doc_number.append(number['number'])
        self.doc_number.append('Неверный номер!')
        self.doc_type = []
        for doctype in documents:
            self.doc_type.append(doctype['type'])
        self.doc_type.append('Неверный номер!')
        self.shelf = []
        for shelf in directories.keys():
            self.shelf.append(shelf)
        self.shelf.append('Неверный номер!')

    def test_doc_people(self):
        """Тестируем нахождение человека по номеру документа"""
        result = doc_people('11-2')
        standard = self.people
        self.assertIn(result, standard)

    def test_doc_shelf(self):
        """Тестируем нахождение полки по номеру документа"""
        result = doc_shelf('11-2')
        standard = self.shelf
        self.assertIn(result, standard)

    def test_doc_list(self):
        """Тестируем через сравнение правильность строк вывода документа"""
        result = doc_list()
        standard = str
        for item in result:
            self.assertIs(type(item), standard)

    def test_doc_add(self):
        """Тестируем создание документа"""
        shelf, type_doc, number, name = '3', 'passport', '777', 'John Doe'
        doc_add(shelf, type_doc, number, name)
        standard = doc_list()
        self.assertIn(f'{type_doc} {number} {name}', standard)
        self.assertIn(shelf, self.shelf)

    def test_doc_delete(self):
        """Тестируем удаление документа"""
        doc = '11-2'
        doc_delete(doc)
        self.assertNotIn(doc, directories.values())
        for item in documents:
            self.assertNotEqual(doc, item['number'])

    # def tearDown(self):
        # print(doc_people('11-2'))
        # print(doc_shelf('11-2'))
        # print(doc_list())
        # print(documents)
        # print(directories)
