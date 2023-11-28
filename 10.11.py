# try:
#     print(int('qewer'))
# except ValueError:
#     print("my v value error")
# except ZeroDivisionError:
#     print("eto zero division error")
# except:
#     print("my tut")

# with open('new.txt.txt', mode='w', encoding='utf-8') as n_file:
#     n_file.write('hola')

# import json
#
# word = "ChatGPT вызвал разногласия в общественном мнении. Некоторые считают, что он может заменить некоторых специалистов, в то время как другие относятся к нему очень скептически. Наша цель - поделиться опытом работы с ChatGPT и предоставить маркетологам несколько практических советов как использовать нейросеть для написания текста на русском."
# characters_count = {}
#
# for character in word:
#     if character in characters_count.keys():
#         characters_count[character] += 1
#     else:
#         characters_count[character] = 1
# try:
#     file = open('data.json', 'w', encoding='utf-8')
#     json.dump(characters_count, file, indent=4)
#     file.close()
# except:
#     print('file unavailable')

# class MyException(Exception):
#
#     def __init__(self, text):
#         self.text = text
#
# raise MyException("my exception")

class InvalidObjectType(Exception):

    def __init__(self, text):
        self.text = text


class Department:

    def __init__(self, department_name, director=None):

        self.__department_name = department_name

        if isinstance(director, Person):

            self.__director = director

        else:

            raise InvalidObjectType('director должен быть обьектом класса Person')

        self.__employees = []

    def add_employees(self, person):

        if isinstance(person, Person):

            self.__employees.append(person)

        else:

            raise InvalidObjectType("Обьект должен быть класса Person")


class Person:

    def __init__(self, name, surname, position):
        self.__name = name

        self.__surname = surname

        self.__position = position


person1 = Person('Paver', 'Durov', 'CTO')

person2 = Person('Magzhan', 'Zh', 'backend developer')

department = Department('IT', person1)

department.add_employees(person2)

