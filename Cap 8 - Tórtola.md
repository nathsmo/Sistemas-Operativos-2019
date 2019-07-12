## Capítulo 8: Main Memory - Notas de lectura
##### Luis Angel Tórtola

* Podemos suponer que tendremos múltiples procesos utilizando la memoria, y debido a que este es un recurso altamente demandado y limitado, es importante aprender a compartirla adecuadamente
* La memoria no es más que un arreglo de bytes con direcciones asignadas.
* Normalmente al ejecutar instrucciones en el CPU, los operandos son leídos de la memoria y los resultados escritos en ella. 
* La memoria princial y los registros, son los únicos espacios de almacenamiento (general) que el CPU puede acceder directamente. Los datos guardados en otros medios de almacenamiento deben ser primero llevados a memoria para que el CPU pueda leerlos.
* Para un buen funcionamiento al tener procesos concurrentes, cada uno debe tener asignado un espacio de memoria separado al de los demás, determinados por una dirección base y una dirección límite.
* Las direcciones lógicas son las generadas por el CPU, mientras las direcciones físicas son la unidad de memoria en sí. En la etapa de ejecución de instrucciones, las direcciones lógicas son también conocidas como virtuales.
* La carga dinámica de memoria se utiliza para únicamente levantar en memoria el programa principal y luego, dinámicamente, copiar a memoria las rutinas que se vayan necesitando.
* Es un hecho que para que un proceso sea ejecutado este debe estar en memoria, sin embargo no requiere estar en memoria todo el tiempo. Este se puede eliminar temporalmente y luego traer a memoria de nuevo. 
* El swapping hace posible correr procesos que utilizan más memoria que la cantidad de memoria física disponible.
* En las implementaciones más utilizadas,el swapping es desactivado al inicio y únicamente se recurre a él cuando la cantidad de memoria asignada disponible es menor a la cantidad de treshold definida.
* La alocación de memoria contigua es método para asignar memoria eficientemente tanto al sistema operativo como a los procesos de usuarios.
* Dos particiones principales: OS y procesos de usuarios.
* En este método la memoria asignada a cada proceso es asignada en el orden de ejecución de los procesos.
* Para proteger los espacios de memoria asignados, cuando un proceso es seleccionado por el planificador, la base y límite de la memoria es cargada durante el cambio de contexto para restringuir el acceso a memoria por parte de proceso correspondiente.
* Para seleccionar en dónde alocar un nuevo espacio de memoria, existen tres métodos principales: First fit, best fit y worst fit.
* First fit: asigna el primer espacio de memoria lo suficientemente grande que encuentra.
* Best fit: recorre todas las opciones y luego selecciona la más pequeña y suficientemente grande.
* Worst fit: recorre todas las opciones y luego selecciona la de mayor tamaño.
* First fit y best fit provocan fragmentación de la memoria (externa), dejando espacios de memoria disponibles pero tan pequeños que nunca son asignados a ningún proceso y rompen la contingencia de memoria.
* La segmentación es un mecanismo para mapear la memoria observada por el programador y la memoria física.
