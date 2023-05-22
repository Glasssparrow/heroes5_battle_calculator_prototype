

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        raise Exception("Такого не должно быть")


atk1 = 31
def1 = 31
min_damage1 = 50
max_damage1 = 50
hp1 = 220

atk2 = 32
def2 = 36
min_damage2 = 36
max_damage2 = 66
hp2 = 199

damage = min_damage1*(1+0.05*abs(atk1-def2))**sign(atk1-def2)
print(1+0.05*(atk1-def2))
print(damage)
print((1+0.05*abs(atk1-def2))**sign(atk1-def2))
