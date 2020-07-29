En un mundo de objetos, todo lo que manejamos son **objetos** y **mensajes**. Los mensajes pueden aludir a algo que *tiene* el objeto (llamado técnicamente *atributo*) o algo que el objeto *hace* (llamado técnicamente *método* ) A estos últimos, podemos distinguirlos según la forma en que se escriben:

ム **Mensajes con paréntesis**. Su nombre está compuesto por una palabra o varias palabras (siempre unidas_por_espacios_subrayados o indicadasPorMayusculasEnCamello), **no puede** terminar con un signo de exclamación `!` o de pregunta `?`, y se indica el objecto  mediante un punto. Además,

* pueden tomar uno o más argumentos, separados por coma: 
    * `San_Martin.cruzar_donde_como(losAndes, Mula)`
    * `SanMartin.cruzarDondeComo(los_Andes, Mula)`
* pueden no tomar argumentos, 
    * como `San_Martin.pensar_algo()`
    * como `SanMartin.pensarAlgo()`

ム **Operadores**. Son todos aquellos cuyo "nombre" es un símbolo (a veces, mas de uno como == , !=, <>), y se envían simplemente escribiendo dichos símbolos. En cuanto a los argumentos,

* Los operadores pueden tomar un argumento, como el operador  `==` en la sentencia  `Orson.energia == Garfield.energia` o el operador `+` en la sentencia `objeto.energia + 80`.
* pueden no tomar ninguno, como la negación `!CaraMoneda`;


Como vimos, también se pueden escribir como mensajes de palabra clave (aunque no parece buena idea escribir `1.==(2)` en vez de `1 == 2` :stuck_out_tongue:).

> Vamos a enviar algunos mensajes para terminar de cerrar la idea. Te toca escribir un programa que haga que Pepita:
>
> 1. Coma 90 gramos de alpiste. :rice:
> 1. Vuele a Iruya. :earth_americas:
> 1. Allí, coma tantos gramos de alpiste como el 10% de la energía que le haya quedado.  :rice:
> 1. Finalmente, Vuele al centro geográfico de Argentina (Ishuaia). :earth_americas:
>
> Este programa tiene cumplir el enunciado sin importar con cuanta energía arranque `Pepita`.
