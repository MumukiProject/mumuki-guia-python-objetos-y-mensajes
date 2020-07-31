

> Para calcular el 20%  que buscamos, podemos usar la Regla de 3:
>
> 100% <----> total   
>  20% <----> ?????   
> 
> resultado:  total * 20% / 100%    
> resultado:  total * 0.20    

Como usamos esa cuenta en nuestro programa?    
Veamos, cualquier envío de mensajes que devuelva algo es una expresión válida, y puede ser usada en cualquier lugar en que se espera un objeto. Por ejemplo, las siguientes colaboraciones son válidas:

```python
ム Fitito.cargar_combustible(36) #Carga 36 Litros
ム Fitito.cargar_combustible(12 * 3) #Carga 36 Litros
ム Fitito.cargar_combustible(Fitito.capacidad_tanque_combustible - Fitito.combustible_disponible) #Carga  lo necesario para completar
```

Qué pasó recién?? vamos por línea por línea:

* línea1: el método `cargar_combustible` recibe como parámetro el número que tipeamos, el `36`
 
* línea2: el método `cargar_combustible` recibe como parámetro el número 36 pero antes hay dos pasos:
    1. Python aplica el operador `*` al objeto `12`  (si! en :snake: *todo* lo que vemos es un objeto!). 
    1. envía el mensaje `cargar_combustible(36)` con el resultado
     
* línea3: parecido a la línea2, pero ahora :snake:  hace cuatro pasos:
    1. busca el valor `capacidad_tanque_combustible` 
    1. busca el valor `combustible_disponible` 
    1. aplica el operador `-` al primer valor, supongamos que resulte `36`
    1. envía el mensaje `cargar_combustible(36)` 


Como vimos, también se pueden escribir como mensajes de palabra clave (aunque no parece buena idea escribir 1.==(2) en vez de 1 == 2 :stuck_out_tongue:).