# -*- coding: utf-8 -*-
"""Alexandra Gónzalez de la Fuente - computacion_tarea7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RxjFmXJuChaO9HQLUYjhp6C-me9YbWsX

# Tarea 7: Revisión de los conceptos básicos de Python
### Computación - 8108
#### Facultad de Ciencias - UNAM
#### Profesores: C. Fís. Omar Trejo, C. Fís. Iván Jiménez, Pedro Flores-Silva

Instrucciones: Este notebook contiene una serie de ejercicios que deben ser resueltos. Cada ejercicio se encuentra en una celda, ya sea de código o Markdown. Debes crear una o dos *celdas debajo de cada ejercicio* con tu(s) respectiva(s) respuestas. No modifiques las celdas originales.
Recuerda que para ejecutar el código de una celda, presionar `Ctlr + Enter` o bien el boton de `play` en el editor Jupyter notebook.

Cada ejercicio tendrá diferente valor, y se indicará en la celda de éste. La calificación final será la suma de los puntos obtenidos en cada ejercicio. Se calificará considerando la calidad de la respuesta, la claridad de la explicación y la correctitud del código. Por ejemplo, si el código no ejecuta la respuesta correcta pero se da una idea textual, se demuestra que hay comprensión del problema y el código hace sentido para el revisor, se otorgará una calificación parcial. Esto es, las respuestas no solo se evaluarán como bien o mal, sino que se considerará el esfuerzo. 

El codigo que realices debes comentarlo donde creas necesario, no vale no hacer ningún comentario. Recuerda que los comentarios son importantes para que el código sea legible y entendible, éstos se agregan con el símbolo # .

### Ejercicio 1 (1 punto):
En una celda Markdown contesta: ¿Qué es un nombre reservado en python? Enlista 5 ejemplos de nombres reservados en python y describe su función (aquí debes investigar su función si es que aún no hemos tratado dicho nombre reservado).

##Respuesta:

Como su nombre lo indican, son palabras/nombres a las cuales el lenguaje de programación ya ha asignado una tarea específica. Por lo que nosotros no podemos nombrar una variables con el mismo nombre que una palabra reservaba.
Algunos ejemplos son:

* None – Representa a un valor nulo
* Await – Proporcionada por la biblioteca ‘asyncio’ en Python. Se utiliza para escribir código concurrente en Python
* Class – Se usa para definir una nueva clase definida por el usuario
* Continue – Se utiliza en el interior de los bucles for y while para alterar su comportamiento normal
* Finally – Su uso garantiza que el bloque de código dentro de él se ejecute incluso si hay una excepción no controlada

### Ejercicio 2 (1 punto):
En una celda Markdown: Coloca tres ejemplos de nombres de variables que no son válidos en python. Explica por qué no son válidos.

##Respuesta:

* "False" no se le puede saignar ninun valor pues es una palabra reservada
* "True" al ser una palabra reservada tampoco podemos asignarle ninún valor
* "None" tampoco podemos asignarle un valor pues arrojaría Syntaxerror ya que es una palabra reservada

### Ejercicio 3 (3 puntos):
Considera el siguiente polinomio: $f(x) = 10x^2 - 2x$. 

En una celda Markdown escribe:
* Los pasos para encontrar sus raíces a través del método del despeje.
* Los pasos para encontrar sus raíces a través del método de la chicharronera.

En una celda de código, escribe un programa que compruebe que las raíces del polinomio $f(x) = 10x^2 - 2x$ que tu encontraste son correctas. El programa debe imprimir las raíces en la pantalla. (Debes usar la ecuación que obtuviste al depejar el polinomio).

En otra celda de código, escribe un programa que encuentre las raíces del polinomio $f(x) = 10x^2 - 2x$ a través del método de la chicharronera. El programa debe imprimir las raíces en la pantalla. (Debes usar la chicharronera).

Considera los signos de la chicharronera como dos operaciones diferentes: $(-)$ y $(+)$.

##Respuesta:

1.   Encontrar raíces despejando 

*   Simplificamos y obtenemos factor común

  $10x^2-2x=0$

  $5x^2-x=0$

  $x(5x-1)=0$

*   Sacamos obtenemos nuestra sietma de ecuaciones y lo resolvemos 

 $5x-1=0$

 $x=1/5$ 
 y
 $x=0$ 


2.   Encontrar raíces con la fórmula general


*   Simplificamos el polinomio 

 $10x^2-2x=0$

  $5x^2-x=0$



*   Sustituimos lo valores en la fórmula

  $x=\frac{-(-1)±(\sqrt{-1^2-4(5)(0)}}{2(5)}$
  
  $x=\frac{-(-1)±(\sqrt{(1-0)}}{10}$

   $x=\frac{1±1}{10}$

* Obtenemos las posibles x por signos

 $x(+)=\frac{1+1}{10}$  $x=0$

 $x(-)=\frac{1-1}{10}$ $x=\frac{1}{5}$
"""

### Ahora escribiremos el programa que nos dirá, si las ecuaciones encontradas son correctas:
###POR DESPEJE:
#Empexamos defininedo nuestra variable d que será igual a 0, pues es al valor que queremos llegar para comprobar si es o no raíz 
d=0

def Despeje(valor):
    x = valor
    #Introducimos nuestra operación obtenida al sacar factor común
    y = x*(5*(x)-1)
    if (y==a):
        print (x, "Es raíz") #Esto quiere decir que si el valor obtenido de y coincide con d que es 0, entonces si es raíz
    else:
        print (x, "No es raíz") #En el caso de que y no coincida con 0, enconces no será raíz 
      #Al poner print se mostrará si es o no ráiz

#Ahora veremos si lo que obtenemos coincide con nuestros resultados anterioreses
Despeje(0)
Despeje(1/5)

###POR FÓRMULA GENERAL:

def General(a,b,c):
    suma = (-b+((b**2-(4*a*c))**(1/2)))/(2*a) #Debemos de poner meter la frómula 2 veces, pues podemos obtener 2 resultados diferentes.
   
    resta = (-b-((b**2-(4*a*c))**(1/2)))/(2*a)
    #Las 2 opciones donde una es la suma y la otra es resta
    print("Las raicez son: {} y {}".format(suma,resta)) #Con esto se imprimiran las 2 raíces obtenidas en la suma y resta.

#Da como resultado
General(10,-2,0)

"""### Ejercicio 4 (3 puntos):
Caida libre: El gran Galileo Galilei subió la torre de Pisa para determinar el tiempo que tarda un objeto en caer desde una altura $H$ al suelo. Para ello, colocó un objeto de masa $m=100$ kg en la torre y lo dejó caer. El tiempo que tardó en caer fue $t=0.05616667$ minutos.

Considerando que la aceleración de la gravedad es $g=9.8$ $\frac{m}{s^2}$, escribe un programa que determine la altura de la torre de Pisa. El programa debe imprimir la altura en la pantalla.

Recuerda que el movimiento de caída libre simplificado cumple la ecuación: $y(t) = H + vt - \frac{1}{2}gt^2$.

"""

###Respuesta:

def MUA(t,v,y):
    g = 9.8 #Introducimos el valor de la gravedad
    H = y-(v*t)+((1/2)*g*(t**2)) #Una vez desoejada la fórmula para la altura, la introducimos 

    print ("La altura es", H, "metros") #Con esto imprimimos el H

tm = 0.05616667
s = tm*60 #Ahora solo falta pasar el tiempo a segundos
MUA(s,0,0)

"""### Ejercicio 5 (2 puntos):
Considera una lista de números enteros del 0 al 99 : `lista = [0,1, 2, 3, 4, ... , 95, 96, 97, 98, 99]`.
En una celda de código, escribe un programa que imprima en la pantalla una la lista que cumpla con las siguientes condiciones:
* Los ultimos 10 elementos: debe imprimir lo siguiente `[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]`.
* Los primeros 11 elementos: debe imprimir lo siguiente `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.
* La serie de elementos de la lista que están entre 60 y 75: debe imprimir lo siguiente `[60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]`.
* El número 50: debe imprimir lo siguiente `50`.

Debes aplicar el concepto de *slicing* para resolver este ejercicio (notación de puntos `[:]`).

Puntos menos si se crean listas nuevas para cada caso y/o se seleccionan manualmente los valores.

El código de abajo te ayudará a crear la lista del 0 al 99.
"""

lista = list(range(100))

###Respuesta:

#Primero nombramos nuestra lista del 0 al 99
lista = list(range(100))
lista_completa = lista[0:11]+lista[12:51]+lista[51:76]+lista[90:100] #Establecemos nuestra lista con las especificaciones 
print (lista_completa) #Imprimimos nuestra lista completa con las especificaciones

"""### Puntos extras, este ejercicio es opcional (5 puntos):
Replica el código visto en clase para simular los volados. Discute los resultados obtenidos. ¿Qué observas? ¿Qué puedes concluir? ¿Qué pasa cuando la cantidad de volados es muy pequeña? ¿Qué pasa cuando la cantidad de volados es muy grande?

En caso de errores con librerias no encontradas, debes hacer en una celda de código lo siguiente:

`!pip install nombre_de_la_libreria`. Por ejemplo para plotly: `!pip install plotly`.
"""

!pip install plotly