from new_code.units import Unit
from new_code.effects import Effect


buff = Effect(10, attack=0.5)

a = Unit("Test", attack=2)
a.effects.append(buff)
