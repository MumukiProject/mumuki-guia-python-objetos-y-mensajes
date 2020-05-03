¡Así es! Puede haber más de un objeto que entienda el mismo mensaje. Notá que sin embargo no todos los objetos están obligados a reaccionar de igual forma ante el mismo mensaje: 

```ruby
Pepita.cantar!
=> "pri pri pri"

Norita.cantar!
=> "priiiip priiiip"

Mercedes.cantar!
=> "♪ una voz antigua de viento y de sal ♫"
```

Esto significa que dos o más objetos pueden entender un mismo mensaje, pero pueden **comportarse** de formas diferentes. Ya hablaremos más de esto en próximas lecciones.