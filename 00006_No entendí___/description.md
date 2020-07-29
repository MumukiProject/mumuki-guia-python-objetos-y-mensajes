¡Buu! `Pepita` no sabía `bailar()` :cry:

En el mundo de los objetos, sólo tiene sentido enviarle un mensaje a un objeto si lo entiende, es decir, si sabe hacer algo como reacción a ese mensaje. De lo contrario, se lanzará un error un poco feo (y en inglés :pensive:) como el siguiente:

```
AttributeError: 'pajaritoClass' object has no attribute 'bailar'
```

> Descubramos qué otras cosas sabe hacer `Pepita`. Probá enviarle los siguientes mensajes y fijate cuáles entiende y cuales no ¡y anotalos! :memo:
Este conocimiento nos servirá en breve.
>

```python
ム Pepita.pasear()
ム Pepita.energia
ム Pepita.comer_lombriz()
ム Pepita.volar_en_circulos()
ム Pepita.se_la_banca?
```

Viste el **espacio subrayado ___** que forma parte de algunos mensajes como `volar_en_circulos()` ? 
claro, ver un espacio sería difícil si no lo subrayamos! :grinning: pero eso no es lo central. Usamos el carácter "espacio subrayado"  para que el *intérprete de Python* entienda varas palabras como si fueran una sola (en ambos tipos de mensaje), por ejemplo:

* energia_necesaria_para_llegar
* comer_lombriz()
* volar_en_circulos()

notar que hay **un  mensaje** en cada línea, y que quien programa lo piensa como una frase, pero el intérprete de Python lo trata como una sola palabra  