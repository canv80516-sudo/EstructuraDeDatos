# Estructura De Datos
## Explicación de mi programa de ventas

Mi programa sirve para guardar las ventas de una tienda que tiene tres departamentos (Ropa, Deportes y Juguetería) durante los doce meses del año. En vez de tener doce variables sueltas o algo así, guardo todo en una sola tabla con filas y columnas, donde cada fila es un mes y cada columna es un departamento. Así puedo saber, por ejemplo, cuánto se vendió en Ropa durante Marzo con solo mirar esa casilla.

Además, el programa le pregunta al usuario qué quiere hacer (agregar una venta, buscarla o borrarla) y sigue preguntando una y otra vez hasta que la persona decida salir.

Así funciona cada parte:

**Armar la tabla vacía**
Esta parte del programa simplemente crea la tabla de doce filas por tres columnas y pone un cero en cada casilla, para que al principio no haya ninguna venta registrada. Es como tener una hoja en blanco lista para llenarse.

**Agregar una venta**
Aquí es donde se guarda un número en la tabla. El programa recibe que mes es, que departamento es y cuanto se vendió, y antes de guardar revisa que el mes y el departamento existan de verdad (por ejemplo, que no le pidan guardar algo en un "mes 15" que no existe). Si todo está bien, coloca el número en su casillita correspondiente y lo guardado.

**Buscar una venta**
Esta parte recorre toda la tabla, casilla por casilla, mes por mes y departamento por departamento, buscando si algún número coincide con el que el usuario está buscando. Cada vez que encuentra una coincidencia la va apuntando en una lista, y al final regresa todas las coincidencias que encontró, no solo la primera.

**Borrar una venta**
En lugar de escribir un código nuevo para borrar, esta parte simplemente le pide ayuda a la función de "agregar una venta", pero le dice que el número que va a guardar es un cero. Así, borrar una venta es lo mismo que dejarla en cero.

**Mostrar toda la tabla**
Esta parte no cambia nada, solo recorre la tabla mes por mes y va imprimiendo en pantalla lo que hay guardado en cada uno, para poder ver de un vistazo cómo está toda la información.

**Preguntar el mes y preguntar el departamento**
Estas dos partes existen para que el usuario no tenga que memorizar que "Enero es el 0" o que "Ropa es el 0". El programa le muestra la lista completa de meses (o de departamentos) numerada, y la persona solo tiene que escribir el número que le corresponde a lo que quiere.

**El menú principal**
Esta es la parte que mantiene todo funcionando. Muestra las opciones en pantalla (agregar, buscar, borrar, ver todo o salir), espera a que el usuario escriba un número y según lo que haya escrito, decide a cuál de las partes anteriores mandarlo. Esto se repite una y otra vez hasta que el usuario elige la opción de salir y el programa se termina.
