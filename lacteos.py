import matplotlib.animation as animation
from gpiozero import DistanceSensor
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
from time import sleep
import datetime as dt
import csv


#Pins for motor Driver inputs (MX1508 | Chimalli's MotorB) BAND
MotorBandA = 23
MotorBandB = 24
#Pins for motor Driver inputs (MX1508 | Chimalli's MotorB) BAND
MotorValveA = 27
MotorValveB = 22

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(MotorBandA,GPIO.OUT)
    GPIO.setup(MotorBandB,GPIO.OUT)
    GPIO.setup(MotorValveA,GPIO.OUT)
    GPIO.setup(MotorValveB,GPIO.OUT)
    fig=plt.figure('Gráfica de llenado de envase')
    ax=fig.add_subplot(111)
    
def moveBand(): #Sucess
    GPIO.output(MotorBandA,GPIO.LOW)
    GPIO.output(MotorBandB,GPIO.HIGH)
    
def stopBand(): #Sucess
    GPIO.output(MotorBandA,GPIO.LOW)
    GPIO.output(MotorBandB,GPIO.LOW)

def openValve(): #Sucess
    GPIO.output(MotorValveA,GPIO.LOW)
    GPIO.output(MotorValveB,GPIO.HIGH)

def closeValve(): #Sucess
    GPIO.output(MotorValveA,GPIO.HIGH)
    GPIO.output(MotorValveB,GPIO.LOW)
    
    
def distance1(): #Sucess
    bandSensor = DistanceSensor(16,12)
    distance1 = bandSensor.distance
    return distance1*100

def distance2():
    valveSensor = DistanceSensor(7,13)#Change pines
    distance2 = valveSensor.distance
    return distance2*100

def objectCounter(counter):
    counterl = [counter]
    print(counterl)
    with open('objectCounter.csv', mode='a' , newline='') as registerObject:
        register_object = csv.writer(registerObject, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        register_object.writerow(counterl)

def sucessCounter():
    scounter+=1
    scounter = [scounter]
    #print(temperatura)
    with open('sucessCounter.csv', mode='a' , newline='') as registerSucess:
        register_sucess = csv.writer(registerSucess, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        register_sucess.writerow(scounter)
        
def errorCounter():
    ecounter+=1
    ecounter = [ecounter]
    #print(temperatura)
    with open('errorCounter.csv', mode='a' , newline='') as registerError:
        register_error = csv.writer(registerError, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        register_error.writerow(ecounter)
        
    
def regHeight(distance2):
    height = [distance2]
    with open('height.csv', mode='a' , newline='') as registerHeight:
        register_height = csv.writer(registerObject, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        register_height.writerow(height)
def anima_regHeight():
    ani=animation.FuncAnimation(fig,actualizar,interval=1)
    plt.show()
    
def actualizar(i):
    ax.clear()
    distance2()
    ax.plot(i,distance2)
    ax.bar(1,distance2,width=0.5,align='center')
    plt.ylim(0,1.5)
    plt.ylabel('Altura del líquido (cm)')
    plt.xlim(0,2)
    return i

if __name__== '__main__':
    setup()
    counter = 0
    scounter = 0
    ecounter = 0
    flag = False
    while True:
        distance1r = distance1() #El sensor 1 mide la distancia
        if distance1r <= 10 and flag == False: #Si hay un objeto
            flag = True
            stopBand() #Se detiene la banda
            counter+=1 #Se incrementa el contador
            objectCounter(counter) #Contador de objetos que llegaron a la electroválvula | Registro en un .CSV
            
        elif distance1r > 10:
            moveBand()
            flag = False
    '''if distance1r <= 10: #Si hay un objeto
        stopBand() #Se detiene la banda
        objectCounter(counter) #Contador de objetos que llegaron a la electroválvula | Registro en un .CSV
        distance2() #Se mide la distancia para verificar si está vacío
        if distance2 >= 10: #Si está vacío
            openValve() #Se abre la válvula
            distance2() #Se verifica el nivel de llenado
            #regHeight(distance2) # Registro de la altura en un .CSV
            ani_regHeight() #Animación de la altura de cada envase llenándose y Registro de la altura en un .CSV
            if distance2 <= 4: #Si el envase ya llegó al límite
                closeValve() #Se cierra la electroválcula
                sucessCounter() #Contador de envases llenado de manera exitosa | Registro en un .CSV
                moveBand() #Avanza la banda
            else:
                moveBand() #Avanza la banda
        else:
            errorCounter() #Contador de envases inútiles | Registro en un .CSV
            moveBand() #Avanza la banda
    else:
        moveBand() #Avanza la banda'''