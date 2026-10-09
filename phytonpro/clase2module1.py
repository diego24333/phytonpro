#clase2-modulo1
import random
characters="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long=int(input("pon la longitud"))
contraseña=""
for i in range(long):
    contraseña += random.choice(characters)
print(contraseña)
