class Pokemon:
    sound = ''
    def __init__(self, name='', level=1):
        if name == '':
            raise ValueError("name cannot be empty")
        if level <= 0:
            raise ValueError("level should be > 0")
        self._name = name
        self._level = level
        self._master = ''
    
    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level
    
    @property
    def master(self):
        if self._master == '':
            print("No Master")
        else:
            return self._master
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    
    def __str__(self):
        return f'{self.name} - Level {self.level}'

class RunningPokemon:
    animal = ''
    value = 10
    level = 0
    @classmethod
    def run(cls):
        print(f'{cls.animal} running...')
    
    def attack(self):
        print(f'Electric attack with {self.value * self.level} damage')

class SwimmingPokemon:
    animal = ''
    value = 9
    level = 0
    @classmethod
    def swim(cls):
        print(f'{cls.animal} swimming...')
    
    def attack(self):
        print(f'Water attack with {self.value * self.level} damage')

class FlyingPokemon:
    animal =''
    value = 5
    level = 0
    @classmethod
    def fly(cls):
        print(f'{cls.animal} flying...')
    
    def attack(self):
        print(f'Air attack with {self.value * self.level} damage')
        
class Pikachu(Pokemon, RunningPokemon):
    animal = 'Pikachu'
    sound = 'Pika Pika'
    value = 10
    
class Squirtle(Pokemon, RunningPokemon, SwimmingPokemon):
    animal = "Squirtle"
    sound = 'Squirtle...Squirtle'
    value = 9
    
    def attack(self):
        SwimmingPokemon.attack(self)
    
class Pidgey(Pokemon, FlyingPokemon):
    animal = "Pidgey"
    sound = 'Pidgey...Pidgey'
    value = 5
   
class Swanna(Pokemon, SwimmingPokemon, FlyingPokemon):
    animal = "Swanna"
    sound = 'Swanna...Swanna'
    value = 9
    
    def attack(self):
        SwimmingPokemon.attack(self)
        self.value = 5
        FlyingPokemon.attack(self)
    
class Zapdos(Pokemon, RunningPokemon, FlyingPokemon):
    animal = "Zapdos"
    sound = 'Zap...Zap'
    value = 10
    
    def attack(self):
        RunningPokemon.attack(self)
        self.value = 5
        FlyingPokemon.attack(self)

class Island:
    islands_count = []
    def __init__(self, name, max_no_of_pokemon, total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.islands_count.append(self)
    
    @property
    def name(self):
        return self._name
    
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def __str__(self):
        return f'{self.name} - {self._pokemon_left_to_catch} pokemon - {self._total_food_available_in_kgs} food'
        
    def add_pokemon(self, pokemon):
        if self._pokemon_left_to_catch < self.max_no_of_pokemon:
            self._pokemon_left_to_catch += 1
        else:
            print("Island at its max pokemon capacity")
            
    @classmethod
    def get_all_islands(cls):
        return cls.islands_count
            
class Trainer:
    def __init__(self, name):
        self._name = name
        self._experience = 100
        self._max_food_in_bag = 10 * self._experience
        self._food_in_bag = 0
        self._current_island = ""
        self.count_pokemon = []
        
    @property
    def name(self):
        return self._name
        
    @property
    def experience(self):
        return self._experience
        
    @property
    def current_island(self):
        if self._current_island == "":
            print("You are not on any island")
        else:
            return self._current_island

    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
        
    @property
    def food_in_bag(self):
        return self._food_in_bag
       
    def move_to_island(self, island):
            self._current_island = island

    def catch(self, pokemon):
        if self.experience >= (100 * pokemon.level):
            self.count_pokemon.append(pokemon)
            pokemon._master = self
            self._experience = self.experience + (pokemon.level * 20)
            print(f'You caught {pokemon.name}')
        else:
            print(f'You need more experience to catch {pokemon.name}')
            
    def collect_food(self):
        if self._current_island == "" or self._current_island._total_food_available_in_kgs == 0:
            print("Move to an island to collect food")
        elif self._current_island._total_food_available_in_kgs < self._max_food_in_bag:
            self._food_in_bag = self._current_island._total_food_available_in_kgs
            self._current_island._total_food_available_in_kgs = 0
        elif self._food_in_bag != self._max_food_in_bag:
            self._current_island._total_food_available_in_kgs -= self.max_food_in_bag#1000
            self._food_in_bag = self.max_food_in_bag
        
    def get_my_pokemon(self):
        return self.count_pokemon




# class Island:
#     pokemon_list =[]
#     islands_list = []
#     def __init__(self, name, max_no_of_pokemon, total_food_available_in_kgs):
#         self._name = name
#         self._max_no_of_pokemon = max_no_of_pokemon
#         self._total_food_available_in_kgs = total_food_available_in_kgs
#         self._pokemon_left_to_catch = 0
#         self.islands_list.append(self)
    
#     @property
#     def name(self):
#         return self._name
#     @property
#     def max_no_of_pokemon(self):
#         return self._max_no_of_pokemon
#     @property
#     def total_food_available_in_kgs(self):
#         return self._total_food_available_in_kgs
#     @property
#     def pokemon_left_to_catch(self):
#         return self._pokemon_left_to_catch
    
#     def add_pokemon(self, pokemon):
#         if self.pokemon_left_to_catch + 1 <= self.max_no_of_pokemon:
#             #self.__class__.pokemon_list.append(pokemon)
#             self._pokemon_left_to_catch += 1
#         else:
#             print('Island at its max pokemon capacity')
#             self._pokemon_left_to_catch = self.max_no_of_pokemon
        
#     def __str__(self):
#         return f'{self.name} - {self.pokemon_left_to_catch} pokemon - {self.total_food_available_in_kgs} food'
        
#         #Island1 - 0 pokemon - 10000 food 
        
#     @classmethod
#     def get_all_islands(cls):
#         return cls.islands_list
    
# class Trainer:
#     count_pokemon = []
#     island_name = ''
#     def __init__(self, name):
#         self._name = name
#         self._experience = 100
#         self._max_food_in_bag = 0
#         self._food_in_bag = 0
#         self._current_in_island = False
        
#     @property
#     def name(self):
#         return self._name
#     @property
#     def experience(self):
#         return self._experience
#     @property 
#     def max_food_in_bag(self):
#         self._max_food_in_bag = self._experience * 10
#         return self._max_food_in_bag
#     @property
#     def food_in_bag(self):
#         return self._food_in_bag
        
        
#     def current_island(self):
#         if self._current_in_island:
#             return self.island_name
#         else:
#             print('You are not on any island')
#         #def __str__(self):
#         #    return f'{self.island_name.name} - {self.island_name.pokemon_left_to_catch} pokemon - {self.island_name.total_food_available_in_kgs} - food'
            
    
#     def move_to_island(self, island):
#         self._current_in_island = island
#         #self.island_name = island

#     def collect_food(self):
#         if self._current_in_island:
#             if self.island_name.total_food_available_in_kgs > self.max_food_in_bag and self.food_in_bag == 0:
#                 self._food_in_bag = self.max_food_in_bag
#                 self.island_name._total_food_available_in_kgs -= self._max_food_in_bag
#             elif self.food_in_bag ==  self.max_food_in_bag:
#                 self._food_in_bag = self.max_food_in_bag
#                 self.island_name._total_food_available_in_kgs = self.island_name.total_food_available_in_kgs
#             else:
#                 self._food_in_bag = self.island_name.total_food_available_in_kgs
#                 self.island_name._total_food_available_in_kgs = 0
#         else:
#             print("Move to an island to collect food")

#     def catch(self, pokemon):
#         self.__class__.pokemons.extend([pokemon])
#         if self.experience >= 100 * pokemon.level:
#             self._experience  += (20 * pokemon.level)
#             pokemon._master = self
#             print(f"You caught {pokemon.name}")
            
#         else:
#             print(f'You need more experience to catch {pokemon.name}')
    
#     @classmethod
#     def get_my_pokemon(cls):
#         return f'{cls.pokemons}'

pokemon = Pikachu(name='Ryan', level = 1)
trainer = Trainer(name='Bot')
#print(pokemon.master)
trainer.catch(pokemon)
pokemon.attack()
print(pokemon.master)
#print(pokemon.master == trainer)