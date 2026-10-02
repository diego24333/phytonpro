pesos=int(input("cuantos pesos colombianos tienes"))
cop=3369 
usd=1
def cambio():
    global pesos
    global usd, cop
    result=pesos*usd/cop
    print("son" ,result)
cambio()    
