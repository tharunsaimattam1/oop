from car  import Car
import math

class RaceCar(Car):
    
    horn = "Peep Peep\nBeep Beep"
    
    def accelerate(self):
        if self.nitro > 0:
            self._current_speed += math.ceil(self._acceleration * 30 / 100)
            self.nitro -= 10
        super().accelerate()
    
    
    def apply_brakes(self):
        if self._current_speed >= (self._max_speed // 2):
            self.nitro += 10
        super().apply_brakes()