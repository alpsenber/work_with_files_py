import zipfile
import os

class Quest_5():
    def create_zip_archive(self):
        # Создание ZIP-архива
        archive_name = input("Введите имя архива (с расширением .zip): ")
        try:
            with zipfile.ZipFile(archive_name, 'w') as zip_archive:
                print(f"Архив {archive_name} создан.")
        except:
            print("Ошибка при создании архива.")
    
    
    def add_file_to_archive(self):
        # Добавление файла в ZIP-архив
        archive_name = input("Введите имя архива (с расширением .zip): ")
        file_name = input("Введите имя файла, который нужно добавить: ")
        try:
            with zipfile.ZipFile(archive_name, 'a') as zip_archive:
                zip_archive.write(file_name, os.path.basename(file_name))
            print(f"Файл {file_name} успешно добавлен в архив.")
        except:
            print("Ошибка при добавлении файла в архив.")
    
    
    def extract_file_from_archive(self):
        # Разархивирование и вывод информации о файле из ZIP-архива
        archive_name = input("Введите имя архива (с расширением .zip): ")
        file_name = input("Введите имя файла для разархивирования: ")
        try:
            with zipfile.ZipFile(archive_name, 'r') as zip_archive:
                zip_archive.extract(file_name)
                print(f"Файл {file_name} успешно разархивирован.")
            with open(file_name, 'r') as extracted_file:
                file_contents = extracted_file.read()
                print(f"Содержимое файла {file_name}:\n{file_contents}")
        except zipfile.BadZipFile:
            print("Ошибка: указанный файл не является архивом ZIP.")
        except KeyError:
            print(f"Ошибка: файл {file_name} не найден в архиве.")
    
    
    def delete_file_and_archive(self):
        # Удаление файла и ZIP-архива
        file_name = input("Введите имя файла для удаления: ")
        archive_name = input("Введите имя архива, в котором находится файл: ")
        try:
            os.remove(file_name)
            os.remove(archive_name)
            print("Файл и архив успешно удалены.")
        except FileNotFoundError:
            print("Ошибка: указанный файл или архив не найдены.")
    
    def menu(self):
        # Главное меню
        while True:
            print("\nВыберите действие:")
            print("1. Создать ZIP-архив")
            print("2. Добавить файл в архив")
            print("3. Разархивировать файл и вывести информацию")
            print("4. Удалить файл и архив")
            print("5. Выход")
        
            choice = input("Введите номер действия: ")
        
            if choice == '1':
                self.create_zip_archive()
            elif choice == '2':
                self.add_file_to_archive()
            elif choice == '3':
                self.extract_file_from_archive()
            elif choice == '4':
                self.delete_file_and_archive()
            elif choice == '5':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
q = Quest_5()
q.menu()