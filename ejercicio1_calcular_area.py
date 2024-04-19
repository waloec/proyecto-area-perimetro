# Calcular area LxL

lado1 = float(input("ingrese un lado:  "))
lado2 = float(input("ingrese el otro lado :"))

def calcular_area (lado1,lado2):
    return ( lado1 * lado2)

print (calcular_area(lado1,lado2)) 


# Calcular el perimetro = L+L+L+L

def calcualar_perimetro(lado1, lado2):
    resultado = (lado1*2 +lado2*2)
    return  resultado
resul=calcualar_perimetro(lado1,lado2)

print(f"el perimetro es {resul}")
