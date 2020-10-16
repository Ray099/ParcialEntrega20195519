import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
def suma(num1,num2):
    return num1 + num2


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros pares del 1 al 1000
"""


# start-->
def sumaPares():
    pairList = []
    sumaNumeros = 0
    n = 0
    while n < 1000:
        n += 1
        if (n % 2 == 0):
            pairList.append(n)
    
    for numeros in pairList:
        sumaNumeros += numeros

    result = sumaNumeros
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area total de superficie de un cilindro
radio = 5 m
altura = 7 m
area lateral: 2*pi*r*a
area circulo: 2*pi*r^2
area total: area lateral + area circulo
"""


# start-->

def areaTotalCilindro(radio,altura):   
    

    result = areaLateral(radio,altura) + areaCirculo(radio)
    return (round(result,2))


def areaLateral(radio,altura):
   
    intmath1 = radio*altura
    floatmath1 =math.pi*2
    result = floatmath1*intmath1
    return result


def areaCirculo(radio):
    
    intmath2 = radio**2
    floatmath2 =math.pi*2
    result = floatmath2*intmath2
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cilindro:
    
    def __init__(self):
        radio = ()
        altura = ()
        

    def areaTotalCilindro (self,radio,altura):
        return round(areaLateral(radio,altura) + areaCirculo(radio),2)
    
    def areaLateral(self,radio,altura):
            
        intmath1 = radio*altura
        floatmath1 =math.pi*2
        result = floatmath1*intmath1
        return result


    def areaCirculo(self,radio):
        intmath2 = radio**2
        floatmath2 =math.pi*2
        result = floatmath2*intmath2
        return result

"""
***************************************************************
@@ ejercicio 5 @@
restaurante de pizzas
pizza
    nombre
    lugar
    costo
    conDescuento
    descuento
"""


class Restaurante:
    def __init__ (self):

        def ordenar(self,nombre,lugar,costo,conDescuento,descuento):
            pass

        def costoTotal(self):
            return 0

        def costoTotalConDescuento(self):
            return 0


class Pizza:
    def __init__(self):
        pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/Ray099/ParcialEntrega20195519.git"
