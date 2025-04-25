import psycopg2
from psycopg2 import sql
from getpass import getpass
import military
import sys


class MilitaryApp:

    def __init__(self):
        pass

    def run(self):
        print('Программа Narfu: Учет военной части')
        print('Автор: Александр Богданов')
        print('Версия: 1.0')
        print('\n\n')
        print('Выберите действие:')
        print('1. Ввод данных')
        print('2. Изменение данных')
        print('3. Удаление данных')
        print('4. Вывод данных')
        print('5. Выход')
        print('\n\n')
        choice = input('Ваш выбор: ')
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            print('Выход из программы')
            sys.exit()

    def test(self):
        test_data_military = military.MilitaryPart.load_from_db(1)
        test_data_vid = military.TypeOfTroops.load_from_db(1)
        test_data_rota = military.Rota.load_from_db(1)
        test_data_komanda = military.Personal.load_from_db(1)
        test_data_dislocation = military.Dislocation.load_from_db(1)

        print("Тестовые данные:")
        print(test_data_dislocation)
        print(test_data_komanda)
        print(test_data_rota)
        print(test_data_vid)
        print(test_data_military)


if __name__ == "__main__":
    app = MilitaryApp()
    app.test()