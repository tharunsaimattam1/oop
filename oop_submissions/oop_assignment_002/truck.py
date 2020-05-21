class Car:
    horn = "Beep Beep"
    
    def __init__(self, color = None, max_speed=0, acceleration=0, tyre_friction=0):
        
        self._color = color
        
        if max_speed > 0:
            self._max_speed = max_speed
        else:
            raise ValueError("Invalid value for max_speed")
            
        if acceleration > 0:
            self._acceleration = acceleration
        else:
            raise ValueError("Invalid value for acceleration")
            
        if tyre_friction > 0:
            self._tyre_friction = tyre_friction
        else:
            raise ValueError("Invalid value for tyre_friction")
        
        self._is_engine_started = False
        self._current_speed = 0
    
    @property
    def max_speed(self):
        return self._max_speed
    
    @property
    def color(self):
        return self._color
        
    @property
    def acceleration(self):
        return self._acceleration
    
    @property
    def tyre_friction(self):
        return self._tyre_friction
    
    @property
    def is_engine_started(self):
        return self._is_engine_started
    
    @property
    def current_speed(self):
        return self._current_speed
    
    def start_engine(self):
        self._is_engine_started = True
        
    def accelerate(self):
        if self._is_engine_started:
            if self._current_speed + self._acceleration <= self._max_speed:
                self._current_speed += self._acceleration
            elif self._current_speed > self._max_speed:
                self._current_speed = self._max_speed
            elif self._current_speed < self._max_speed:
                self._current_speed += (self._max_speed - self._current_speed)
        else:
            print("Start the engine to accelerate")
    
    def apply_brakes(self):
        
        if self._current_speed > self._tyre_friction:
            self._current_speed -= self._tyre_friction
        elif self._current_speed <= self._tyre_friction:
            self._current_speed -=  (self._tyre_friction-(self._tyre_friction - self._current_speed))

    def sound_horn(self):
        if self._is_engine_started:
            print(self.horn)
        else:
            print("Start the engine to sound_horn")
    
    def stop_engine(self):
        if self._is_engine_started:
            self._is_engine_started = False
            
class Truck(Car):
    
    horn = "Honk Honk"
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight=0):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        
        self._max_cargo_weight = max_cargo_weight
        self.current_weight = 0
    
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    
    
    def load(self, cargo_weight):
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")
        elif self._current_speed > 0:
            print("Cannot load cargo during motion")
        elif self.current_weight + cargo_weight <= self._max_cargo_weight:
            self.current_weight += cargo_weight
        else:
            print("Cannot load cargo more than max limit:", self._max_cargo_weight)
    
    def unload(self, cargo_weight):
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")
        elif self.current_speed > 0:
            print("Cannot unload cargo during motion")
        elif cargo_weight > self._max_cargo_weight:
            self.current_weight = 0
        elif self.current_weight - cargo_weight >= 0:
            self.current_weight -= cargo_weight