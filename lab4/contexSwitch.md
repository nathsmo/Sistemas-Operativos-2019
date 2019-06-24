# Laboratorio 4 - Simulacion de Multitask (Context Switch)

## 1. Simular Multitask cambio de contexto usando punteros a función

Para entender el multitasking que realiza el Sistema Operativo hay que definir que es multitask y que es Contex Switch.

### Multitask:   
Es la capacidad que tiene el sistema operativo que permite al usuario realizar mas de una tarea computacional al mismo tiempo. El sistema operativo es capaz de llevar un registro de que tareas está realizando y a la vez es capaz de realizarlas sin perder información de cada una.    
Un ejemplo de multitasking es cuando se esta escuchando música y navegando por internet. Ambos estan realizando sus diferentes funciones en la computadora, la música continua reproduciendose al mismo tiempo que la persona abre nuevas pestañas y carga diferentes páginas de internet sin alguna interrupción. 

### Context Switch  
Es el proceso que realiza el CPU para cambiar de una tarea a otra asegurandose de las tareas no tengan conflictos entre ellas. Esto es esencial si se desea proveer un multitasking user-friendly.   
Lleva la palabra *Context* porque antes de realizar el cambio de una tarea a otra este guarda su Contexto, es decir, guarda en una *tabla* la información importante de la tarea que esta realizando. Esta tabla es llamada  PCB (Process Control Block), algunos de los items que almacena la PCB son:
* **Process State:**  
Especifica el estado del proceso actual - Nuevo, Listo, Corriendo, Esperando, Terminado. 
* **Process Number:** 
Es el número identificador del proceso, es unico y distingue al proceso de los demas en el sistema. 
* **Program Counter:**   
Contiene la dirección de la siguiente instrucción a ejecutar.
* **Registers:**   
 Incluyen todos los registros que el proceso este utilizando, estos pueden incluir a accumulators, index registers, stack pointers, general purpose registers etc.
* **Información de Scheduling:**    
La prioridad que tiene el proceso en el sistema y la direccion de la cola donde se almacena.
* **I/O Status Information:**   
Esta información incluye la lista de dispositivos que está utilizando el proceso.

![Tabla PCB](PCB.png)

El Context Switch puede ser provocado por tres diferentes motivos: 
* **Multitasking:**   
Una tarea realiza un context switch para que otra tarea tenga el control del CPU también y lo ejecutar su proposito. 
* **Interrupt Handling:**   
El hardware cambia de contexto cuando una interrupción es ocurren en el sistema, esto ocurre automaticamente. 
* **User and Kernel Mode Switching:**    
Occurre cuando el sistema operativo necesita cambiar de Mode para realizar tareas con mayor privilegios (Kernel Mode) en el hardware o esta regresando de este mode a un mode con menos privilegios (User Mode.

Basicamente el Sistema Operativo solo puede realizar una tarea a la vez. Sin embargo, debido a que el CPU es demasiado rápido puede realizar sub-divisiones de tareas en un tiempo muy corto una tras otra, que a los ojos humanos pareciera que están siendo ejecutadas en paralelo. 

El siguiente diagrama representa el proceso de Context Switch:
![Context Switch](ContextSwitching.png)


A continuacion se realiza un ejemplo de la simulacion de Context Switch utilizando funciones para simular diferentes procesos. 

```c++
#include <stdio.h>
#include <dos.h>
#include <conio.h>

#define INTR 0X1C /* Interrupción del Clock Tick*/

//https://en.wikipedia.org/wiki/BIOS_interrupt_call
//http://stanislavs.org/helppc/int_table.html

#ifdef __cplusplus
    #define __CPPARGS ...
#else
    #define __CPPARGS
#endif
```

## 2. Simular Multitask con cambio de contexto real
A continuacion se realiza un ejemplo de simulación de Contex Switch obteniendo el Code Segmente y Program Counter de cada cambio de *proceso* que se realiza.

```c++
#include <stdio.h>
#include <dos.h>
#include <conio.h>

#define INTR 0X1C /* Interrupción del Clock Tick*/

//https://en.wikipedia.org/wiki/BIOS_interrupt_call
//http://stanislavs.org/helppc/int_table.html

#ifdef __cplusplus
    #define __CPPARGS ...
#else
    #define __CPPARGS
#endif
```
