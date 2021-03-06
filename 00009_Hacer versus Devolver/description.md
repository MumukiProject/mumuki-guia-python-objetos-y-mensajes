Cuando se envía un mensaje a un objeto, y el mensaje es entendido por ese objeto, puede ocurrir una de dos cosas: 

* Podría _producir un efecto_, es decir _hacer_ algo. Por ejemplo, el mensaje `cantar()` reproduce el sonido del canto de `Pepita`.
* O también podríamos _recibir otro objeto_. Por ejemplo el mensaje `energia` devuelve siempre un número.

:warning: _En realidad, un mensaje podría reaccionar con una combinación de las formas anteriores: tener un efecto y devolver algo. Pero esto es una **muy mala idea**._

> ¿Y qué hay de los mensajes como `comer_lombriz()` y `volar_en_circulos()`? ¿Hicieron algo? ¿Qué clase de efecto produjeron? ¿Devuelve `energia` siempre lo mismo? :frowning::thought_balloon:
> 
> Descubrilo: enviale a `Pepita` esos tres mensajes varias veces en distinto orden y fijate si cambia algo. 
