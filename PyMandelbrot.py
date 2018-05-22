'''
Created on 18/05/2018

@author: Jaime Sacramento
'''
#To test the Mandelbrot set, the function time.clock is used, which resides on the time library.
import time;


def mandelbrot (tamano):
    "Mandelbrot block"
    suma = 0
    byte_acc = 0
    num_bit = 0
    y = 0
    ###############Main loop y#################
    while (y < tamano):
        
        ci= (2.0 * y / tamano) - 1.0
        x = 0
        while (x < tamano):
           ###############Loop x #################
            zr = 0.0
            zrzr = 0.0
            zi = 0.0
            zizi = 0.0
            cr = (2.0 * x / tamano) - 1.5
            z = 0
            salir = 1
             
            while (z < 50):
               ###############Loop z#################
                tr = zrzr - zizi + cr 
                ti = 2.0 * zr * zi + ci
                 
                zr = tr
                zi = ti
                 
                # Preserves recalculations
                 
                zrzr = zr * zr
                zizi = zi * zi
                 
                if (zrzr + zizi > 4.0):
                     
                    salir = 0
         
                    break
                z += 1
             ###############End of loop z#################
            byte_acc = (byte_acc << 1 ) | salir
            num_bit += 1
             
             
            if (num_bit == 8):
                suma ^= byte_acc
                byte_acc = 0
                num_bit = 0
            elif (x == tamano - 1):
                byte_acc = 0
                num_bit = 0     
                 
            x += 1
           ###############End of loop x#################      
        y += 1
       ############### End of Main loop y#################
    return suma



def calentar ():
"Block to warm up calculations"
    n = 0
    for n in range(0,10000):
        mandelbrot(10)
    return
 
def muestra():
    "Block to test correct calculations"
    return mandelbrot(750) == 192        
             
######################## Main program ##############

# Block to open a .txt file for data storage on hard drive
archivo = open("Benchmarkpython.csv","w+")
if (muestra() == False): #Check if current calculations are correct
    print("Error during execution!")
    exit()  
print("Succesful")

# Work variables
iteraciones = 100
calentar = 0
problema = 1000


print("Total iterations: %d "  %iteraciones )
print("Warm up iterations: %d" %calentar)
print("Problem size: %d"  %problema )

######## Warm up block
while (calentar > 0):
    mandelbrot(problema)
    calentar = calentar - 1
    
######## Iterations block, 
while (iteraciones > 0):

    inicio = time.clock() 
    mandelbrot(problema)
    tiempo = (time.clock() - inicio) * 1000 # Convert seconds to miliseconds
    iteraciones = iteraciones - 1
    print("Mandelbrot: iteraciones =1 %d ms" %tiempo )
    archivo.write("%d,\n"%tiempo)

archivo.close()

    




    
