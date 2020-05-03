Cualquier envío de mensajes que devuelva algo es una expresión válida, y puede ser usada en cualquier lugar en que se espera un objeto. Por ejemplo, las siguientes colaboraciones son válidas:

```ruby
ム Fitito.cargar_nafta!(120 * 4)
ム Fitito.cargar_nafta!(Fitito.capacidad_tanque_nafta - Fitito.nafta_disponible) #Carga al Fitito lo necesario para completar su tanque. Para ello le pregunta al Fitito su capacidad y la nafta que tiene en este momento. 
```