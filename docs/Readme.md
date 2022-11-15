# **Prueba de validación UD1 Programación multiproceso**
## Ejercicio 1

Este programa python se encarga de crear 10 procesos hijos realizando los siguientes pasos:
    
1. Crea los procesos hijos con ***os.fork()***.

2. El proceso padre mostrará el pid del hijo correspondiente, junto a la hora, minutos y segundos a los que se inició.

3. Una vez iniciados, el proceso hijo muestra un mensaje indicándolo.

4. Pasados tres segundos desde el inicio de su ejecución, el proceso hijo se terminará mostrando un mensaje.

**El programa esperará 10 segundos desde que empezó el primer hijo para crear el siguiente**

> **AVISO:** *Este programa sólo es compatible con sistemas **Linux** o **MacOS***