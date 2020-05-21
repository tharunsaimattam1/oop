class Animal:
    sound = ''
    increase_the_food_in_kgs = 0
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self._breed = breed
        if age_in_months != 1:
            raise ValueError(f'Invalid value for field age_in_months: {age_in_months}')
        self._age_in_months = age_in_months
        if required_food_in_kgs <= 0:
            raise ValueError(f'Invalid value for field required_food_in_kgs: {required_food_in_kgs}')
        self._required_food_in_kgs = required_food_in_kgs
    
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    
    def grow(self):
        self._required_food_in_kgs += self.increase_the_food_in_kgs
        self._age_in_months += 1

class LandAnimals:
    
    animal_breathe = "Breathe in air"
    @classmethod
    def breathe(cls):
        print(cls.animal_breathe)

class WaterAnimals:
    
    animal_breathe = "Breathe oxygen from water"
    
    @classmethod
    def breathe(cls):
        print(cls.animal_breathe)

class HuntingAnimals:
    animal_list = 'Deer'
    def hunt(self, animal):
        for i in animal._animals:
            if type(i) == self.animal_list:
                animal._count -= 1
            else:
                print(f'No {self.animal_list}')
                

class Deer(Animal, LandAnimals):
    sound = "Buck Buck"
    increase_the_food_in_kgs = 2

class Lion(Animal, LandAnimals):
    sound = "Roar Roar"
    increase_the_food_in_kgs = 4
    
    def hunt(self, zoo):
        for i in  zoo._animals:
            if i.sound == 'Buck Buck':
                zoo._count -= 1
            else:
                print("No deers to hunt")

class GoldFish(Animal, WaterAnimals):
    sound = "Hum Hum"
    increase_the_food_in_kgs = 0.2
    
class Shark(Animal, WaterAnimals):
    sound = "Shark Sound"
    increase_the_food_in_kgs = 8
    def hunt(self, zoo):
        for i in  zoo._animals:
            if i.sound == 'Hum Hum':
                zoo._count -= 1
            else:
                print("No GoldFish to hunt")

    
class Snake(Animal, LandAnimals):
    sound = "Hiss Hiss"
    increase_the_food_in_kgs = 0.5
    
    def hunt(self, zoo):
        for i in  zoo._animals:
            if i.sound == 'Buck Buck':
                zoo._count -= 1
            else:
                print("No deers to hunt")

 
class Zoo:
    _reserved_food_in_kgs = 0
    _count = 0
    all_animals = 0
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self._count = 0
        self._animals = []
    
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    def add_food_to_reserve(self, food_quantity):
        self._reserved_food_in_kgs += food_quantity
        
    def feed(self, animal):
        if self._reserved_food_in_kgs <= 0:
            self._reserved_food_in_kgs = 0
        else:
            self._reserved_food_in_kgs -= animal.required_food_in_kgs
            animal.grow()
    
    def add_animal(self, animal):
        self._animals.append(animal)
        self.__class__.all_animals += 1
        self._count += 1
        
    def count_animals(self):
        return self._count
    
    @classmethod
    def count_animals_in_all_zoos(cls):
        return cls.all_animals
    
    @staticmethod
    def count_animals_in_given_zoos(zoo):
        count_of_given_zoos = 0
        for i in zoo:
            count_of_given_zoos += i.count_animals()
        return count_of_given_zoos

  

# class Zoo:
#     _reserved_food_in_kgs = 0
#     _count = 0
#     def __init__(self):
#         self._reserved_food_in_kgs = 0
#         self._animals_in_zoo = []
#         self.count = 0
    
#     @property
#     def reserved_food_in_kgs(self):
#         return self._reserved_food_in_kgs
        
#     def add_food_to_reserve(self, food_qunatity):
#         self._reserved_food_in_kgs += food_qunatity
        
#     def feed(self, animal):
#         if self._reserved_food_in_kgs <= 0:
#             self._reserved_food_in_kgs = 0
#         else:
#             self._reserved_food_in_kgs -= animal.required_food_in_kgs
#             animal.grow()
    
#     def add_animals(self, animal):
#         self._animals_in_zoo.append(animal)
#         self.__class__._count += 1
#         #self.__class__.all_animals += 1
#         self.count += 1
    
#     def count_animals(self):
#         return self.count
    
#     @classmethod
#     def count_animals_in_all_zoos(cls):
#         return cls._count
    
#     @staticmethod
#     def count_animals_in_given_zoos(zoo):
#         count = 0
#         for i in zoo:
#             count += i.count_animals()
#         return  count
        