
class Humanity:
    def __init__(self, population, era):
        self.population = population 
        self.era = era              
        self._language = "Українською"

    def evolve(self):
        return f"Людство розвивається в епоху: {self.era}."

    def communicate(self):
   
        return f"Люди спілкуються мовою: {self._language}."


class man(Humanity):
    def __init__(self, name, major, population, era):
     
        super().__init__(population, era)
        self.__name = name 
        self.major = major

 
    def communicate(self):
        return f"чоловік{self.__name} грає в {self.major} і спілкується {self._language}"

    def get_name(self):
        return self.__name


if __name__ == "__main__":

    general_humanity = Humanity(8000000000, "Цифрова")
    
  
    my_human = man("Аркаша", "Доту", 8000000000, "Цифрова")

    print(general_humanity.evolve())
    print(general_humanity.communicate())
    print("-" * 30)
    print(my_human.communicate())     
    print(f"Ім'я через геттер: {my_human.get_name()}")
