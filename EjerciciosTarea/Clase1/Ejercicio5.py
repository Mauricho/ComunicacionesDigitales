#PROBLEMA 5
#Se lanzan dos dados. El evento A es que la suma sea divisible entre dos.
#El evento B que sea divisible entre 4.
#Se pide P(AB) y P(B|A)
import random
import matplotlib.pyplot as plt

def calcular_probabilidad_dados(num_simulaciones):
    
    contadorA = 0       #Contador para el evento A
    contadorB = 0       #Contador para el evento B
    contadorAB = 0      #Contador para cuando se dan los dos eventos
    contadorC = 0       #Contador para el resto de los casos, n° no divisible por 2 o 4  

    for i in range(num_simulaciones):

        dados1 = random.randint(1, 6) 
        dados2 = random.randint(1, 6)
        
        suma = dados1 + dados2

        if suma %2 == 0:        #Si ocurre el evento A
            contadorA += 1
            if suma %4 == 0:        #Si ocurre el evento B    
                contadorB += 1
                contadorAB += 1
        else:                   #Si ocurre el evento C  
            contadorC += 1

    probA = contadorA / num_simulaciones    #Probabilidad del evento A
    probB = contadorB / num_simulaciones    #Probabilidad del evento B
    probAB = contadorAB / num_simulaciones  #Probabilidad del evento AB = BA 
    
    probBdadoA = probAB / probA             #P(B|A)
    probAdadoB = probAB / probB             #P(A|B)    

    #Datos de la tirada
    etiquetas = ['Evento A','Evento B','Evento C']
    datos = [contadorA,contadorB,contadorC]

    #Crear el histograma con etiquetas
    plt.bar(etiquetas,datos,color=['blue','red','yellow'])

    return (probA, probB, probAB, probAdadoB, probBdadoA)

num_simulaciones = int(input("Ingrese el número de simulaciones: "))

results = calcular_probabilidad_dados(num_simulaciones)

print(f'La probabilidad de los eventos AB: {results[2]} \nLa probabilidad de los eventos B|A son: {results[4]} \nLa probabilidad de los eventos A|B son: {results[3]} ')
print(f'P(A) tiene que ser igual a P(A/B) para que sean sucesos independientes, en este caso P(A) = {results[0]} y P(A/B) = {results[3]}')
print(f'P(B) tiene que ser igual a P(B/A) para que sean sucesos independientes, en este caso P(B) = {results[1]} y P(B/A) = {results[4]}')

#Para ser sucesos independientes:
#Se debe obtener P(A|B)=P(A) y de manera analítica: 1 != 0,5
#Se debe obtener P(B|A)=P(B) y de manera analítica: 0.5 != 0.25 
#Entonces no son sucesos independientes.

plt.title('Histograma de dos dados')
plt.ylabel('Frecuencia')
plt.show()