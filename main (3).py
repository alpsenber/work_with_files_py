import os
import shutil
import json
import xml.etree.ElementTree as ET
import zipfile
import pathlib
import stat

class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getCountry(self):
        return self.country

class Hero:
    def __init__(self, nickname, fraction, health):
        self.nickname = nickname
        self.fraction = fraction
        self.health = health

    def getNickname(self):
        return self.nickname

    def getFraction(self):
        return self.fraction

    def getHealth(self):
        return self.health

def show_menu():
    print("1. Вывести информацию о логических дисках")
    print("2. Работа с файлами")
    print("3. Работа с форматом JSON")
    print("4. Работа с форматом XML")
    print("5. Создание zip архива")
    print("6. Выход")

def option1():
    print("Информация о логических дисках:")
    for drive in os.popen("wmic logicaldisk get caption, volumename, size, filesystem"):
        print(drive.strip())

def option2():
    print("Введите название файла: ")
    file_name = input()
    # Создание файла
    open(file_name, "w").close()
    print("Файл успешно создан.")

    # Запись в файл
    user_input = input("Введите строку для записи в файл: ")
    with open(file_name, "w") as file:
        file.write(user_input)
    print("Строка успешно записана в файл.")

    # Чтение файла
    with open(file_name, "r") as file:
        content = file.read()
    print(f"Содержимое файла: {content}")

    # Удаление файла
    os.remove(file_name)
    print("Файл успешно удален.")

def option3():

    def create(file_name):
        with open(file_name, "w") as file:
            json.dump([], file)

    def insert(file_name, json_data):
        with open(file_name, "w") as file:
            json.dump(json_data, file)

    def read(file_name):
        with open(file_name, "r") as file:
            print(file.read())

    def delete(file_name):
        path = str(pathlib.Path.cwd()) + "\\" + file_name
        if os.path.isfile(path):
            os.remove(path)
            print("Успешно удалён")
        else:
            print("Данного файла не существует")

    file_name = input("Введите название файла: ") + ".json"
    person = Person(input("Имя "), input("Возраст "), input("Страна "))
    json_data = {"name": person.getName(), "age": person.getAge(), "country": person.getCountry()}
    create(file_name)
    insert(file_name, json_data)
    read(file_name)
    delete(file_name)

def option4():
    def create_xml_file(hero, xml_file_name):
        # Создание корневого элемента
        root = ET.Element("hero")

        # Создание дочерних элементов и добавление атрибутов
        nickname = ET.SubElement(root, "nickname")
        nickname.text = hero.getNickname()

        fraction = ET.SubElement(root, "fraction")
        fraction.text = hero.getFraction()

        health = ET.SubElement(root, "health")
        health.text = str(hero.getHealth())

        # Создание XML-дерева
        tree = ET.ElementTree(root)

        # Запись XML-дерева в файл
        tree.write(xml_file_name)

        print("Файл XML успешно создан.")

    def read_xml_file(xml_file_name):
        # Чтение XML файла
        tree = ET.parse(xml_file_name)
        root = tree.getroot()

        # Получение значений из XML и вывод в консоль
        nickname = root.find("nickname").text
        fraction = root.find("fraction").text
        health = int(root.find("health").text)

        print("Nickname:", nickname)
        print("Fraction:", fraction)
        print("Health:", health)

    # Ввод названия файла от пользователя
    xml_file_name = input("Введите название XML файла: ") + ".xml"

    # Создание объекта класса Hero
    hero = Hero(input("Никнейм: "), input("Фракция: "), int(input("Здоровье: ")))

    # Создание XML файла с сериализацией объекта hero
    create_xml_file(hero, xml_file_name)

    # Чтение XML файла и вывод содержимого в консоль
    read_xml_file(xml_file_name)

    # Удаление файла XML
    os.remove(xml_file_name)
    print("Файл XML успешно удален.")


def option5():
    print("Введите название архива: ")
    zip_file_name = input()

    with zipfile.ZipFile(zip_file_name, "w") as zip_archive:
        pass
    print("Архив успешно создан.")

    selected_file = input("Введите имя файла для добавления в архив: ")
    with zipfile.ZipFile(zip_file_name, "a") as zip_archive:
        zip_archive.write(selected_file)
    print("Файл успешно добавлен в архив.")

    # extracted_file_path = os.path.join(os.getcwd(), zip_file_name)
    with zipfile.ZipFile(zip_file_name, "r") as zip_archive:
        zip_archive.extract(selected_file, './1/')
    print(f"Файл успешно разархивирован.")

    zip_file_size = os.path.getsize(zip_file_name)
    print(f"Размер архива: {zip_file_size}")

    #shutil.rmtree(selected_file)
    os.remove(selected_file)
    os.remove(zip_file_name)
    print("Файл и архив успешно удалены.")

# Основной цикл меню
while True:
    show_menu()
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        option4()
    elif choice == "5":
        option5()
    elif choice == "6":
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")