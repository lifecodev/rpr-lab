import psycopg2
from psycopg2 import sql

class Database(object):
    """
    Класс для работы с базой данных PostgreSQL.
    """

    def __init__(self, user, password):
        """
        Инициализация класса.
        :param user: Имя пользователя для подключения к базе данных.
        :param password: Пароль для подключения к базе данных.
        """
        self.conn = None
        self.current_user = user
        self.password = password

        self.connect()

    def connect(self):
        """
        Подключение к базе данных PostgreSQL.
        :return: None
        """
        try:
            self.conn = psycopg2.connect(
                dbname="rpr",
                user=self.current_user,
                password=self.password,
                host="localhost",
                port="5432"
            )
            print("Успешное подключение к базе данных!")
        except Exception as e:
            print(f"Ошибка подключения: {e}")

    def close(self):
        """
        Закрытие соединения с базой данных.
        :return: None
        """
        if self.conn:
            self.conn.close()
            print("Соединение с базой данных закрыто.")

    def use_func(self, func_name, *args):
        """
        Выполнение функции в базе данных.
        :param func_name: Имя функции.
        :param args: Аргументы для функции.
        :return: Результат выполнения функции.
        """
        try:
            with self.conn.cursor() as cursor:
                cursor.callproc(func_name, args)
                self.conn.commit()
                return cursor.fetchall()
        except Exception as e:
            print(f"Ошибка выполнения функции: {e}")
            return None

    def execute_query(self, query, params=None):
        """
        Выполнение SQL-запроса.
        :param query: SQL-запрос в виде строки.
        :param params: Параметры для подстановки в запрос (по умолчанию None).
        :return: None
        """
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                self.conn.commit()
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")

    def fetch_query(self, query, params=None):
        """
        Выполняет SQL-запрос и возвращает все результаты.

        :param query: SQL-запрос в виде строки.
        :param params: Параметры для подстановки в запрос (по умолчанию None).
        :return: Список кортежей с результатами запроса или None в случае ошибки.
        """
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            return None

    def fetch_query_one(self, query, params=None):
        """
        Выполняет SQL-запрос и возвращает одну строку результата.
        :param query: SQL-запрос в виде строки.
        :param params: Параметры для подстановки в запрос (по умолчанию None).
        :return: Кортеж с результатами запроса или None в случае ошибки.
        """
        try:
            with self.conn.cursor() as cursor:

                cursor.execute(query, params)
                return cursor.fetchone()
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            return None



