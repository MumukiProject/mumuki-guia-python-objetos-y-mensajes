Como vimos, un objeto puede entender múltiples mensajes; a este conjunto de mensajes que podemos enviarle lo denominamos **interfaz**. Por ejemplo, la interfaz de `Pepita` es: 

* `energia`: nos dice cuanta energía tiene (un número);
* `cantar!`: hace que cante;
* `comer_lombriz!`: hace que coma una lombriz;
* `volar_en_circulos!`: hace que vuele en circulos.

<!--
@startuml
interface Pepita {
   energia
   cantar!
   comer_lombriz!
   volar_en_circulos!
}
@enduml
-->

Lo cual también se puede graficar de la siguiente forma:

![interfaz](http://www.plantuml.com/plantuml/png/7SZ12O0m30NGUwT8DtA34aEKG9kKR_MWkBlOs-EP3yN6ehHejy7q929IL-p6FuLzCF9aD4MfqLROFUUAoYZgHGnorZXoUZy0)

> ¡Un momento! ¿Por qué algunos mensajes terminan en `!` y otros no? 
> Enviá nuevamente esos mensajes. Fijate qué devuelve cada uno (lo que está a la derecha del `=>`) y tratá de descubrir el patrón.
