#clase2-modulo1
import random
character="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long=int(input("pon la longitud de la contraseña"))

contraseña=0
for i in range(long):
    print(random.randint(character))
