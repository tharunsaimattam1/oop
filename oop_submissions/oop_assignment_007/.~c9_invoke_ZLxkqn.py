class Deer:
    sound = 'Buck Buck'
    breathes = "Breathe in air"
    increase_the_food = 2
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        if age_in_months != 1:
            raise ValueError(f'Invalid value for field age_in_months: {age_in_months}')
            
        if required_food_in_kgs <= 0:
            raise ValueError(f'Invalid value for field required_food_in_kgs: {required_food_in_kgs}')
        
        self._age_in_months = age_in_months
        self._breed = breed
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
    def breathe(cls):
        print(cls.breathes)
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    def grow(self):
        self._required_food_in_kgs += self.increase_the_food
        self._age_in_months += 1

class Lion(Deer):
    sound = "Roar R"





































# class Deer:
#     sound = "Buck Buck"
#     breath = "Breathe in air"
#     increase_food_in_kgs = 2
#     hunt_animal = "deers"
#     def __init__(self, age_in_months = 1, breed = "ELK", required_food_in_kgs = 10):
#         if age_in_months != 1:
#             raise ValueError(f'Invalid value for field age_in_months: {age_in_months}')
#         self._age_in_months = age_in_months
#         self._breed = breed
#         if required_food_in_kgs <= 0:
#             raise ValueError(f'Invalid value for field required_food_in_kgs: {required_food_in_kgs}')
#         self._required_food_in_kgs = required_food_in_kgs
        
#     @property
#     def age_in_months(self):
#         return self._age_in_months
        
#     @property
#     def breed(self):
#         return self._breed
        
#     @property
#     def required_food_in_kgs(self):
#         return self._required_food_in_kgs
    
#     @classmethod
#     def make_sound(cls):
#         print(cls.sound)
        
#     @classmethod 
#     def breathe(cls):
#         print(cls.breath)
        
#     def grow(self):
#         self._age_in_months += 1
#         self._required_food_in_kgs += self.increase_food_in_kgs
    
#     @classmethod    
#     def hunt(cls, animal):
#         if not(isinstance(animal, Deer)):
#             print(f"No {cls.hunt_animal} to hunt")
#         if any([isinstance(i,Deer) for i in animal.no_of_animals]):
#             Zoo.reduce_animals(animal)

# class Lion(Deer):
#     sound = "Roar Roar"
#     increase_food_in_kgs = 4
    
# class Shark(Deer):
#     sound = "Shark Sound"
#     increase_food_in_kgs = 8
#     breath = "Breathe oxygen from water"
    
#     def hunt(self, animal):
#         if any([isinstance(i,GoldFish) for i in animal.no_of_animals]):
#             Zoo.reduce_animals(animal)
#         else:
#             print("No GoldFish to hunt")

# class GoldFish(Deer):
#     sound = "Hum Hum"
#     increase_food_in_kgs = 0.2
#     breath = "Breathe oxygen from water"
    
# class Snake(Deer):
#     sound = "Hiss Hiss"
#     increase_food_in_kgs = 0.5
    
# class Zoo:
#     animals_in_zoo = []
#     def __init__(self, reserved_food_in_kgs = 0):
#         self._no_of_animals = []
#         self._reserved_food_in_kgs = reserved_food_in_kgs
        
#     @property
#     def no_of_animals(self):
#         return self._no_of_animals
        
#     @property
#     def reserved_food_in_kgs(self):
#         return self._reserved_food_in_kgs
    
#     def reduce_animals(self):
#         for i in self._no_of_animals:
#             if isinstance(i, Deer):
#                 self._no_of_animals.remove(i)
#                 break
    
#     def add_food_to_reserve(self, food_in_kgs):
#         self._reserved_food_in_kgs += food_in_kgs
        
#     def add_animal(self, added_animal):
#         self.animals_in_zoo.append(added_animal)
#         self._no_of_animals.append(added_animal)
        
#     @classmethod
#     def count_animals_in_all_zoos(cls):
#         return len(cls.animals_in_zoo)
        
#     @staticmethod
#     def count_animals_in_given_zoos(zoo_objects):
#         count = 0
#         for i in zoo_objects:
#             count += len(i.no_of_animals)
#         return count
        
#     def count_animals(self):
#         return len(self._no_of_animals)
        
#     def feed(self, animal):
#         if self._reserved_food_in_kgs >= animal.required_food_in_kgs:
#             self._reserved_food_in_kgs -= animal.required_food_in_kgs
#             animal.grow()
#         else:
#             self._reserved_food_in_kgs = 0




# class Zoo:
#     _reserved_food_in_kgs = 0
#     _count = 0
#     all_animals = 0
#     def __init__(self):
#         self._reserved_food_in_kgs = 0
#         self._count = 0
#         self._animals = []
#     @property
#     def reserved_food_in_kgs(self):
#         return self._reserved_food_in_kgs
        
#     def add_food_to_reserve(self, food_quantity):
#         self._reserved_food_in_kgs += food_quantity
        
#     def feed(self, animal):
#         if self._reserved_food_in_kgs <= 0:
#             self._reserved_food_in_kgs = 0
#         else:
#             self._reserved_food_in_kgs -= animal.required_food_in_kgs
#             animal.grow()
    
#     def add_animal(self, animal):
#         self._animals.append(animal)
#         self.__class__.all_animals += 1
#         self._count += 1
        
    
#     def count_animals(self):
#         return self._count
    
#     @classmethod
#     def count_animals_in_all_zoos(cls):
#         return cls.all_animals
    
#     @staticmethod
#     def count_animals_in_given_zoos(zoo):
#         count_of_given_zoos = 0
#         for i in zoo:
#             #count_of_given_zoos.append(i.count_animals())
#             count_of_given_zoos += i.count_animals()
#         return count_of_given_zoos
            
            
        


# class Deer(Zoo):
    
#     breathes = 'Breathe in air'
#     sound = 'Buck Buck'
#     def __init__(self, age_in_months, breed, required_food_in_kgs):
        
#         if age_in_months != 1:
#             raise ValueError(f'Invalid value for field age_in_months: {age_in_months}')
        
#         if required_food_in_kgs <= 0:
#             raise ValueError(f'Invalid value for field required_food_in_kgs: {required_food_in_kgs}')
        
#         self._age_in_months = age_in_months
#         self._breed = breed
#         self._required_food_in_kgs = required_food_in_kgs
        
#     @property
#     def age_in_months(self):
#         return self._age_in_months
#     @property
#     def breed(self):
#         return self._breed
#     @property
#     def required_food_in_kgs(self):
#         return self._required_food_in_kgs
    
#     @classmethod
#     def breathe(cls):
#         print(cls.breathes)
    
#     @classmethod
#     def make_sound(cls):
#         print(cls.sound)
        
#     def grow(self):
#         self._required_food_in_kgs += 2
#         self._age_in_months += 1

# class Lion(Deer, Zoo):
#     sound = 'Roar Roar'
    
#     def grow(self):
#         self._required_food_in_kgs += 4
#         #self._age_in_months += 1
        
#     def hunt(self, zoo):
#         for i in  zoo._animals:
#             if i.sound == 'Buck Buck':
#                 zoo._count -= 1
#             else:
#                 print("No deers to hunt")
        
# class GoldFish(Lion, Zoo):
#     sound = 'Hum Hum'
#     breathes = "Breathe oxygen from water"
    
#     def grow(self):
#         self._required_food_in_kgs += 0.2
#         #self._age_in_months += 1

# class Shark(GoldFish, Zoo):
#     sound = 'Shark Sound'
#     breathes = "Breathe oxygen from water"
    
#     def grow(self):
#         self._required_food_in_kgs += 8
#         #self._age_in_months += 1
    
#     def hunt(self, zoo):
#         for i in  zoo._animals:
#             if i.sound == 'Hum Hum':
#                 zoo._count -= 1
#                 #print("acheive")
#             else:
#                 print("No GoldFish to hunt")


# class Snake(Lion, Zoo):
#     sound = 'Hiss Hiss'
    
#     def grow(self):
#         self._required_food_in_kgs += 0.5
#         #self._age_in_months += 1


# zoo  = Zoo()
# deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
# deer.make_sound()
# zoo1 = Zoo()
# lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
# lion.make_sound()
# zoo.add_animal(deer)
# zoo1.add_animal(lion)
# zoo1.add_animal(deer)
# zoo.add_animal(lion)
# print(Zoo.count_animals_in_given_zoos([zoo1, zoo]))
# print(Zoo.count_animals_in_all_zoos())
