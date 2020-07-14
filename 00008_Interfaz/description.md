Como vimos, un objeto puede entender múltiples mensajes; a este conjunto de mensajes que podemos enviarle lo denominamos **interfaz**. Por ejemplo, la interfaz de `Pepita` es:

* `energia`: nos dice cuanta energía tiene (un número);
* `cantar()`: **hace** que cante;
* `comer_lombriz()`: **hace** que coma una lombriz;
* `volar_en_circulos()`: **hace** que vuele en circulos.

<!--
self.startuml
interface Pepita {
   energia
   cantar()
   comer_lombriz()
   volar_en_circulos()
}
self.enduml
-->

Lo cual también se puede graficar de la siguiente forma:

![interfaz](http://www.plantuml.com/plantuml/png/9Son3G9134JHVAjm25rS2NImCik0B7bjDESZ0D4x1sHVB_ZBMihQfZUB0gyw82VShLHUJKGGuCtqcqEZb8VZhtE2tNEUQSy_FTAL7T67SMoUwyxljY0k-_q3)

> ¡Un momento! ¿Por qué algunos mensajes terminan en `()` y otros no?
> Enviá nuevamente esos mensajes. Fijate qué devuelve cada uno (lo que está a la derecha del `=>`) y tratá de descubrir el patrón.
