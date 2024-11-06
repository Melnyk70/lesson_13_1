# ДЗ 13.1. Група студентів
# Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# На його основі створіть клас Студент (перевизначте метод виведення інформації).
# Створіть клас Група, екземпляр якого складається з об'єктів класу Студент. Реалізуйте методи додавання, видалення студента та метод пошуку студента на прізвище.
# Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, інакше - None.
# У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)
# Визначте для групи метод str() для повернення списку студентів у вигляді рядка.
# Нижче наведені заготовки, які необхідно доповнити.

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender  # Зберігає стать людини
        self.age = age  # Зберігає вік людини
        self.first_name = first_name  # Зберігає ім'я людини
        self.last_name = last_name  # Зберігає прізвище людини

    def __str__(self):
        # Повертає рядок з основною інформацією про людину
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)  # Виклик ініціалізатора класу Human
        self.record_book = record_book  # Зберігає номер залікової книжки студента

    def __str__(self):
        # Повертає рядок з розширеною інформацією про студента
        return f'{super().__str__()}, Record Book: {self.record_book}'


class Group:
    def __init__(self, number):
        self.number = number  # Зберігає номер групи
        self.group = set()  # Ініціалізує пусту множину для студентів

    def add_student(self, student):
        self.group.add(student)  # Додає студента до групи

    def delete_student(self, last_name):
        student = self.find_student(last_name)  # Знаходить студента по прізвищу
        if student:
            self.group.remove(student)  # Видаляє студента з групи, якщо знайдено

    def find_student(self, last_name):
        for student in self.group:  # Перебирає всіх студентів у групі
            if student.last_name == last_name:
                return student  # Повертає студента, якщо прізвище співпадає
        return None  # Повертає None, якщо студента не знайдено

    def __str__(self):
        # Створює рядок з інформацією про всіх студентів у групі
        all_students = ''.join(str(student) for student in self.group)
        return (f'Group Number: {self.number}'
                f'{all_students}')  # Повертає номер групи та список студентів


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')  # Створює екземпляр студента
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')  # Створює ще одного екземпляра студента
gr = Group('PD1')  # Створює екземпляр групи
gr.add_student(st1)  # Додає першого студента до групи
gr.add_student(st2)  # Додає другого студента до групи
print(gr)  # Виводить інформацію про групу та студентів

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'  # Перевіряє правильність пошуку студента
assert gr.find_student('Jobs2') is None, 'Test2'  # Перевіряє, що студент з таким прізвищем не знайдено
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'  # Перевіряє, що метод пошуку повертає екземпляр класу Student

gr.delete_student('Taylor')  # Видаляє студента з прізвищем Taylor
print(gr)  # Виводить інформацію про групу після видалення студента

gr.delete_student('Taylor')  # Спроба видалити студента, якого вже немає в групі - не повинно бути помилки
