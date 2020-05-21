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
    hunt_type = "Buck Buck"
    hunt_value = "No deers to hunt"
    @classmethod
    def hunt(cls, zoo_object):
        count = 0
        for animal in zoo_object.no_of_animals:
            if animal.sound == cls.hunt_type:
                count = 1
                zoo_object.no_of_animals.remove(animal)
                break
        if count == 0:
            print(cls.hunt_value)
    
    # animal_list = 'Deer'
    # print_animal = 'deers'
    # flag = 0
    # def hunt(self, animal):
    #     for i in animal._animals:
    #         if type(i) == self.animal_list:
    #             flag  = 1
    #             animal._count -= 1
    #             break
    #         #else:
    #         #    print(f'No {self.print_animal} to hunt')
    #     if flag == 0:
    #         print(f'No {self.print_animal} to hunt')
 
class Deer(Animal, LandAnimals):
    sound = "Buck Buck"
    increase_the_food_in_kgs = 2
       
class Lion(Animal, LandAnimals, HuntingAnimals):
    sound = "Roar Roar"
    increase_the_food_in_kgs = 4
  
class GoldFish(Animal, WaterAnimals):
    sound = "Hum Hum"
    increase_the_food_in_kgs = 0.2
    
class Shark(Animal, WaterAnimals, HuntingAnimals):
    sound = "Shark Sound"
    increase_the_food_in_kgs = 8
    hunt_type = "Hum Hum"
    hunt_value = "No GoldFish to hunt"
    
class Snake(Animal, LandAnimals, HuntingAnimals):
    sound = "Hiss Hiss"
    increase_the_food_in_kgs = 0.5
  
class Zoo:
    all_animals = []
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self.no_of_animals = []
        
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
        self.all_animals.append(animal)
        self.no_of_animals.append(animal)
        
    def count_animals(self):
        return len(self.no_of_animals)
    
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.all_animals)
    
    @staticmethod
    def count_animals_in_given_zoos(zoo):
        count_of_given_zoos = 0
        for i in zoo:
            count_of_given_zoos += i.count_animals()
        return count_of_given_zoos

zoo = Zoo()
lion = Lion(1, 'african', 15)
zoo.add_animal(lion)
lion.hunt(zoo)