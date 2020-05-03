Para hacer las cosas más interesantes, vamos a necesitar mensajes más complejos. :no_mouth:

Por ejemplo, si queremos que `Pepita` coma una cierta cantidad de alpiste que no sea siempre la misma, necesitamos de alguna manera indicar cuál es esa cantidad. Esto podemos escribirlo de la siguiente forma: 

```ruby
Pepita.comer_alpiste!(40)
```

Allí, `40` es un _argumento_ del mensaje, representa en este caso que vamos a alimentar a pepita con 40 gramos de alpiste. Un mensaje podría tomar más de un argumento, separados por coma.

> Probá enviar los siguientes mensajes:
> 
```ruby
ム Pepita.volar_hacia!(Iruya)
ム Pepita.comer_alpiste!(39)
ム Pepita.comer_alpiste!(6, Norita)
```