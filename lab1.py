# Батьківський клас (описує загальне поняття)
class Humanity:
    def __init__(self, population, era):
        self.population = population  # Публічний атрибут
        self.era = era                # Публічний атрибут
        self._language = "Українською" # Захищений атрибут (інкапсуляція)

    def evolve(self):
        return f"Людство розвивається в епоху: {self.era}."

    def communicate(self):
        # Базова реалізація методу
        return f"Люди спілкуються мовою: {self._language}."

# Дочірній клас (наслідування від Humanity)
class man(Humanity):
    def __init__(self, name, major, population, era):
        # Виклик конструктора батьківського класу
        super().__init__(population, era)
        self.__name = name  # Приватний атрибут (інкапсуляція - доступ тільки всередині класу)
        self.major = major

    # ПОЛІМОРФІЗМ: Перевизначаємо метод батька під конкретну роль
    def communicate(self):
        return f"чоловік{self.__name} грає в {self.major} і спілкується {self._language}"

    # Геттер для доступу до приватного імені (частина інкапсуляції)
    def get_name(self):
        return self.__name

# --- ПЕРЕВІРКА РОБОТИ ---
if __name__ == "__main__":
    # Створюємо об'єкт людства
    general_humanity = Humanity(8000000000, "Цифрова")
    
    # Створюємо об'єкт студента
    my_human = man("Аркаша", "Доту", 8000000000, "Цифрова")

    print(general_humanity.evolve())
    print(general_humanity.communicate()) # Виклик методу батька
    print("-" * 30)
    print(my_human.communicate())      # Виклик перевизначеного методу (поліморфізм)
    print(f"Ім'я через геттер: {my_human.get_name()}")