import os
from time import sleep
import time

def padre():
    procesosAEjecutar = 10

    print()

    while procesosAEjecutar > 0:
        newPid = os.fork()
        procesosAEjecutar = procesosAEjecutar - 1
        
        if newPid == 0:
            hijo()
        else:
            print('Iniciando el proceso:', newPid, 'a las', time.strftime('%H:%M:%S', time.localtime()))

        sleep(10)
                
def hijo():
    print('Iniciado el proceso con PID:', os.getpid())
    sleep(3)
    print('Terminando el proceso con PID:', os.getpid())
    os._exit(0)
    
if __name__ == '__main__':
    padre()