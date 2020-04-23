import RPi.GPIO as GPIO
from time import sleep

#Pins for motor Driver inputs (MX1508 | Chimalli's MotorB) BAND
MotorBandA = 23
MotorBandB = 24
#Pins for motor Driver inputs (MX1508 | Chimalli's MotorB) BAND
MotorValveA = 27
MotorValveB = 22
def setup():
    GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    GPIO.setup(MotorBandA,GPIO.OUT)
    GPIO.setup(MotorBandB,GPIO.OUT)
    GPIO.setup(MotorValveA,GPIO.OUT)
    GPIO.setup(MotorValveB,GPIO.OUT)
    
def moveBand(): 
    GPIO.output(MotorBandA,GPIO.LOW)
    GPIO.output(MotorBandB,GPIO.HIGH)
    
    
if __name__== '__main__':
    setup()
    moveBand() #Avanza la banda
    distance1() #El sensor 1 mide la distancia
    if distance1 <= 10: #Si hay un objeto
        stopBand() #Se detiene la banda
        objectCounter() #Contador de objetos que llegaron a la electroválvula | Registro en un .CSV
        distance2() #Se mide la distancia para verificar si está vacío
        if distance2 >= 10: #Si está vacío
            openValve() #Se abre la válvula
            distance2() #Se verifica el nivel de llenado
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
        moveBand() #Avanza la banda
                
            
    

'''
from gpiozero import MCP3008
from gpiozero import DistanceSensor
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.animation as animation

global datos = MCP3008(channel=0)


sensor2 = DistanceSensor(27, 22)
Motor = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor,GPIO.OUT)


def read_analog():
    voltage = (datos.value*3.3)*100
    return voltage

def animate(i,xs,ys):
    voltage=round(read_analog(),2)
    xs.append(dt.datetime.now().strftime('%M:%S')) #agregar a la lista hora, minuto, segundo/ registro temporal
    ys.append(voltage) # agregar el voltaje ya procesado
    xs = xs[-20:] #listas que limitan
    ys = ys[-20:] #listas que limitan
    ax.clear() #limpiar la grafica para que no se amontone
    ax.plot(xs,ys,'b.-', label ='xs') #graficar las listas x y y
    plt.xticks(rotation=45,ha='right') # rotar etiqueta para no se amontone e
    plt.subplots_adjust(bottom=0.30) #tamaño de la grafica
    plt.title('Temperatura del sensor respecto al tiempo')
    plt.ylabel('Temperatura')


#SENSOR
def actualizar (i):
    bx.clear()
    sensor=DistanceSensor(23,24)
    distancia=(sensor.distance*100)
    bx.plot(1,100)
    bx.bar(1,distancia,width=1, align= 'center')
    plt.ylim(0,100)
    plt.ylabel('Distancia (cm)')
    plt.xlim(0,1)
    return i

def grafica():
    fig=plt.figure()
    xs=list()
    ys=list()
    bx= fig.add_subplot(2,1,2)
    ax=fig.add_subplot(2,1,1)
    animaDis= animation.FuncAnimation(fig,actualizar,interval=500)
    ani=animation.FuncAnimation(fig,animate,fargs=(xs,ys),interval=500)
    plt.show()
        

    while True:
        grafica()
        print('Distancia {} m'.format (sensor2.distance))
        sleep(1)
        
        if sensor2.distance < 0.5:
            print('Desactivar banda')
            GPIO.output(Motor, False)
        else:
            print('Activar banda')
            GPIO.output(Motor, True)'''