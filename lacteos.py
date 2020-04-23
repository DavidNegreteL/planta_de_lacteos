from gpiozero import MCP3008
from gpiozero import DistanceSensor
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.animation as animation
from time import sleep
import RPi.GPIO as GPIO
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
        
if _name== 'main_':
    while True:
        grafica()
        print('Distancia {} m'.format (sensor2.distance))
        sleep(1)
        
        if sensor2.distance < 0.5:
            print('Desactivar banda')
            GPIO.output(Motor, False)
        else:
            print('Activar banda')
            GPIO.output(Motor, True)