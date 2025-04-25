import os
from dotenv import load_dotenv
from database import Database

load_dotenv()
DB = Database(os.getenv("DB_USER"), os.getenv("DB_PASSWORD"))

class MilitaryPart:
    def __init__(self, part_id, type_of_troops=None, companies=None, dislocation=None):
        """
        Класс для работы с воинской частью.
        :param part_id: ID воинской части.
        :param type_of_troops: ID вида войск.
        :param companies: Количество рот.
        :param dislocation: ID места дислокации.
        """
        self.part_id = part_id
        self.type_of_troops = type_of_troops
        self.companies = companies
        self.dislocation = dislocation

    @staticmethod
    def load_from_db(part_id):
        """
        Загружает данные о воинской части из базы данных.
        :param part_id: ID воинской части.
        :return: Объект MilitaryPart.
        """
        result = DB.fetch_query_one("SELECT * FROM \"bogdanov.a\".\"Воинская часть\" WHERE номер_части = %s", (part_id,))

        if result:
            return MilitaryPart(
                part_id=result[0],
                dislocation=result[1],
                type_of_troops=result[2],
                companies=result[3]

            )
        else:
            raise ValueError("Воинская часть не найдена в базе данных.")

    def save_to_db(self):
        """
        Сохраняет данные о воинской части в базе данных.
        """
        DB.use_func("add_military_part", self.dislocation, self.type_of_troops, self.companies)

    def __delete__(self, instance):
        """
        Удаляет воинскую часть из базы данных.
        :param instance: Объект базы данных.
        """
        DB.use_func("delete_military_part", self.part_id)

    def __str__(self):
        return f"ID: {self.part_id}, Вид войск: {self.type_of_troops}, Количество рот: {self.companies}, ID места дислокации: {self.dislocation}"

    def update(self, value_name, value):
        """
        Обновляет данные о воинской части в базе данных.
        :param value_name: Имя поля для обновления.
        :param value: Новое значение.
        """
        if value_name == "номер_части":
            raise ValueError("Нельзя обновить номер части.")
        if value_name == "номер_дислокации":
            self.dislocation = value
        if value_name == "номер_вида_войск":
            self.type_of_troops = value
        if value_name == "количество_рот":
            self.companies = value

        DB.use_func("update_military_part", self.part_id, value_name, value)




class TypeOfTroops:
    def __init__(self, troop_id, name):
        """
        Класс для работы с видами войск.
        :param troop_id: ID вида войск.
        :param name: Название вида войск.
        """
        self.name = name
        self.id = troop_id

    @staticmethod
    def load_from_db(troop_id):
        """
        Загружает данные о виде войск из базы данных.
        :param troop_id: ID вида войск.
        :return: Объект TypeOfTroops.
        """
        result = DB.fetch_query_one("SELECT * FROM \"bogdanov.a\".\"Вид войск\" WHERE номер_вида_войск = %s", (troop_id,))

        if result:
            return TypeOfTroops(
                troop_id=result[0],
                name=result[1]
            )
        else:
            raise ValueError("Вид войск не найден в базе данных.")

    def save_to_db(self):
        """
        Сохраняет данные о виде войск в базе данных.
        """
        DB.use_func("add_vid_voisk", self.name)

    def __delete__(self, instance):
        """
        Удаляет вид войск из базы данных.
        :param instance: Объект базы данных.
        """
        DB.use_func("delete_vid_voisk", self.id)

    def __str__(self):
        return f"ID: {self.id}, Название: {self.name}"

    def update(self, value_name, value):
        """
        Обновляет данные о виде войск в базе данных.
        :param value_name: Имя поля для обновления.
        :param value: Новое значение.
        """
        if value_name == "номер_вида_войск":
            raise ValueError("Нельзя обновить номер вида войск.")
        if value_name == "название":
            self.name = value

        DB.use_func("update_vid_voisk", self.id, value_name, value)

class Dislocation:
    def __init__(self, dislocation_id, country, city, area):
        """
        Класс для работы с местами дислокации.
        :param dislocation_id: ID места дислокации.
        :param country: Страна.
        :param city: Город.
        :param area: Занимаемая площадь.
        """
        self.id = dislocation_id
        self.country = country
        self.city = city
        self.area = area


    @staticmethod
    def load_from_db(dislocation_id):
        """
        Загружает данные о месте дислокации из базы данных.
        :param dislocation_id: ID места дислокации.
        :return: Объект Dislocation.
        """
        result = DB.fetch_query_one("SELECT * FROM \"bogdanov.a\".\"Место дислокации\" WHERE номер_дислокации = %s", (dislocation_id,))

        if result:
            return Dislocation(
                dislocation_id=result[0],
                country=result[1],
                city=result[2],
                area=result[3]
            )
        else:
            raise ValueError("Место дислокации не найдено в базе данных.")

    def save_to_db(self):
        """
        Сохраняет данные о месте дислокации в базе данных.
        """
        DB.use_func("add_dislocation", self.country, self.city, self.area)

    def __delete__(self, instance):
        """
        Удаляет место дислокации из базы данных.
        :param instance: Объект базы данных.
        """
        DB.use_func("delete_dislocation", self.id)

    def __str__(self):
        return f"ID: {self.id}, Страна: {self.country}, Город: {self.city}, Занимаемая площадь: {self.area}"

    def update(self, value_name, value):
        """
        Обновляет данные о месте дислокации в базе данных.
        :param value_name: Имя поля для обновления.
        :param value: Новое значение.
        """
        if value_name == "номер_дислокации":
            raise ValueError("Нельзя обновить номер дислокации.")
        if value_name == "страна":
            self.country = value
        if value_name == "город":
            self.city = value
        if value_name == "занимаемая_площадь":
            self.area = value

        DB.use_func("update_dislocation", self.id, value_name, value)

class Personal:
    def __init__(self, personal_id, rota, surname, rank, year_of_service_start=None, year_of_birth=None, awards=None, military_events=None):
        """
        Класс для работы с личным составом.
        :param personal_id: ID личного состава.
        :param rota: ID роты.
        :param surname: Фамилия.
        :param rank: Звание.
        :param year_of_service_start: Год начала службы.
        :param year_of_birth: Год рождения.
        :param awards: Награды.
        :param military_events: Военные события.
        """
        self.personal_id = personal_id
        self.rota = rota
        self.surname = surname
        self.rank = rank
        self.year_of_service_start = year_of_service_start
        self.year_of_birth = year_of_birth
        self.awards = awards
        self.military_events = military_events

    @staticmethod
    def load_from_db(personal_id):
        """
        Загружает данные о личном составе из базы данных.
        :param personal_id: ID личного состава.
        :return: Объект Personal.
        """
        result = DB.fetch_query_one("SELECT * FROM \"bogdanov.a\".\"Личный состав\" WHERE номер_служащего = %s", (personal_id,))

        if result:
            return Personal(
                personal_id=result[0],
                rota=result[1],
                surname=result[2],
                rank=result[3],
                year_of_service_start=result[4],
                year_of_birth=result[5],
                awards=result[6],
                military_events=result[7]
            )
        else:
            raise ValueError("Личный состав не найден в базе данных.")

    def save_to_db(self):
        """
        Сохраняет данные о личном составе в базе данных.
        """
        DB.use_func("add_personal", self.rota, self.surname, self.rank, self.year_of_service_start, self.year_of_birth, self.awards, self.military_events)

    def __delete__(self, instance):
        """
        Удаляет личный состав из базы данных.
        :param instance: Объект базы данных.
        """
        DB.use_func("delete_personal", self.personal_id)

    def __str__(self):
        return f"ID: {self.personal_id}, ID роты: {self.rota}, Фамилия: {self.surname}, Звание: {self.rank}, Год начала службы: {self.year_of_service_start}, Год рождения: {self.year_of_birth}, Награды: {self.awards}, Военные события: {self.military_events}"

    def update(self, value_name, value):
        """
        Обновляет данные о личном составе в базе данных.
        :param value_name: Имя поля для обновления.
        :param value: Новое значение.
        """
        if value_name == "номер_служащего":
            raise ValueError("Нельзя обновить номер служащего.")
        if value_name == "номер_роты":
            self.rota = value
        if value_name == "фамилия":
            self.surname = value
        if value_name == "звание":
            self.rank = value
        if value_name == "год_начала_службы":
            self.year_of_service_start = value
        if value_name == "год_рождения":
            self.year_of_birth = value
        if value_name == "награды":
            self.awards = value
        if value_name == "военные_события":
            self.military_events = value

        DB.use_func("update_personal", self.personal_id, value_name, value)

class Rota:
    def __init__(self, rota_id, name, count):
        """
        Класс для работы с ротами.
        :param rota_id: ID роты.
        :param name: Название роты.
        :param count: Количество служащих.
        """
        self.rota_id = rota_id
        self.name = name
        self.count = count

    @staticmethod
    def load_from_db(rota_id):
        """
        Загружает данные о роте из базы данных.
        :param rota_id: ID роты.
        :return: Объект Rota.
        """
        result = DB.fetch_query_one("SELECT * FROM \"bogdanov.a\".\"Рота\" WHERE номер_роты = %s", (rota_id,))

        if result:
            return Rota(
                rota_id=result[0],
                name=result[1],
                count=result[2]
            )
        else:
            raise ValueError("Рота не найдена в базе данных.")

    def save_to_db(self):
        """
        Сохраняет данные о роте в базе данных.
        """
        DB.use_func("add_rota", self.name, self.count)

    def __delete__(self, instance):
        """
        Удаляет роту из базы данных.
        :param instance: Объект базы данных.
        """
        DB.use_func("delete_rota", self.rota_id)

    def __str__(self):
        return f"ID: {self.rota_id}, Название: {self.name}, Количество служащих: {self.count}"

    def update(self, value_name, value):
        """
        Обновляет данные о роте в базе данных.
        :param value_name: Имя поля для обновления.
        :param value: Новое значение.
        :return: None
        """

        if value_name == "номер_роты":
            raise ValueError("Нельзя обновить номер роты.")
        if value_name == "название":
            self.name = value
        if value_name == "количество_служащих":
            self.count = value

        DB.use_func("update_rota", self.rota_id, value_name, value)


