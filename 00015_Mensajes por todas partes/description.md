Es fácil ver que en `Pepita.volar_hacia(Barreal)` el objeto receptor es `Pepita`, el mensaje `volar_hacia()` y el argumento [`Barreal`](https://es.wikipedia.org/wiki/Barreal); pero ¿dónde queda eso de objeto y mensaje cuando hacemos, por ejemplo, `0.75 + 0.25`?

Como ya dijimos, todas nuestras interacciones en un ambiente de objetos ocurren enviando mensajes y las operaciones aritméticas **no son la excepción** a esta regla.

En el caso de `0.75 + 0.25` podemos hacer el mismo análisis:

* el objeto receptor es `0.75`;
* el mensaje es `+`;
* el argumento es `0.25`.

Y de hecho, ¡también podemos escribirlo como un envío de mensajes convencional!

> Probá en la consola los siguientes envíos de mensajes:
>
```python
ム 0.75.__add__(0.25)
ム 1.5.__gt__(1)
ム 1.5.__gt__(100)
ム Pepita.__eq__(Norita)
ム Pepita.__eq__(Pepita)
```
