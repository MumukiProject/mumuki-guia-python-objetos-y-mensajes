#
# extra.py: traido de la guia XXX (link al repo+commit)
#
import collections

ciudad_anterior = collections.namedtuple("ciudad_anterior", "nombre energia_partida")

class ciudadClass:
  def __init__(self,nombre="Estación Espacial Internacional",kilometros=36000):
    self._nombre=nombre
    self._kilometros=kilometros

  @property
  def nombre(self):
    return self._nombre

  @nombre.setter
  def nombre(self,ahora_vale):
    raise ValueError("'nombre' vale '{}', se fijó durante su  creación y no se puede cambiar".format(self.nombre))
    return None

  @property
  def kilometros(self):
    return self._kilometros

  def distancia_con(self, una_ciudad):
    #   def self.distancia(self, una_ciudad):
    #     (self.ciudad.kilometro - una_ciudad.kilometro).abs
    return abs(self.kilometros - una_ciudad.kilometros)

  def __repr__(self):
    return self.nombre

Ushuaia = ciudadClass("Ushuaia",0) # cercana al centro geográfico de Argentina según https://www.ign.gob.ar/gallery-app/mapas-escolares/medium/argentina_bicontinental_fisico.jpg

BuenosAires = ciudadClass("BuenosAires",2360) #CABA está lejos de muuchas ciudades, incluyendo al centro geográfico de Argentina: https://es.wikipedia.org/wiki/Ushuaia
Buenos_Aires = BuenosAires

# module Iruya
#   def self.kilometr(self):
#     1710
Iruya=ciudadClass(nombre="Iruya", kilometros=4070) #mantinene distancia con BuenosAires, pero no respeta https://es.wikipedia.org/wiki/Ushuaia

# module Oberá
#   def self.kilometr(self):
#     1040
Oberá=ciudadClass(nombre="Oberá", kilometros=3400) #mantinene distancia con BuenosAires según https://es.wikipedia.org/wiki/Ushuaia
Obera=Oberá


class pajaritoClass():
  pio='priiiip priiiip'

  def __init__(self,nombre="Pajarito"):
    self.nombre=nombre
    self._ciudad=None
    self._energia=100 #ej10
    self.ciudades_anteriores=list()


  def __eq__(self,other):
    # necesario para 00003_El derecho a la Identidad
    # TODO: obj1==obj2 no funciona en el runner
    result = (id(self)==id(other))
    return result

  def cantar(self):
    result = type(self).pio
    return result

  def __repr__(self):
    result=type(self).pio+" soy "+self.nombre
    return result

  @property
  def energia(self):
    if self.nombre=="Norita":
      raise ValueError("mensaje invalido: 'energia'")
    return self._energia

  @energia.setter
  def energia(self,ahora_vale):
    #energia.setter
    #
    #   def self.energia=(self, una_energia):
    #     self.energia = una_energia
    #   def self.energi(self):
    #     self.energia
    if self.nombre=="Norita":
      raise ValueError("mensaje invalido: 'energia'")
    self._energia=ahora_vale


  @property
  def ciudad(self):
    return self._ciudad

  @ciudad.setter
  def ciudad(self,ahora_es):
    #ciudad.setter: validacion? TODO: usar volar_hacia() ?
    self._ciudad=ahora_es

  def cantar(self):
    #   def self.cantar!
    #     'pri pri pri'
    return type(self).pio

  def comer_lombriz(self):
    #   def self.comer_lombriz!
    #     self.energia += 20
    #     return
    self.energia += 20 #ej10
    return self.energia

  def comer_alpiste(self,energia_adicional):
    #   def self.comer_alpiste!(self, una_energia):
    #     self.energia += una_energia * 15
    #     return
    self.energia += energia_adicional * 15 #TODO: validar entrada
    # no seria mejor asi:
    #def comer_alpiste(self, gramos):
    # energia_adicional = gramos * 15
    # self.energia += energia_adicional
    return self.energia

  def volar_en_circulos(self):
    #   def self.volar_en_circulos!
    #     self.energia -= 10
    #     return
    self.energia -= 10 #ej10
    return self.energia

  def volar_hacia(self, ciudad_destino):
    #   def self.volar_hacia!(self, una_ciudad):
    #     self.energia -= self.distancia(una_ciudad) * 3
    #     self.ciudad = una_ciudad
    #     return

    if self.ciudad is None:
      nombre_desde = None
    else:
      nombre_desde = self.ciudad.nombre
    volar_desde=ciudad_anterior(nombre=nombre_desde, energia_partida=self.energia)
    if True:# TODO: validar energia necesaria, energia actual, destino
      self.ciudades_anteriores.append(volar_desde)
      if self.ciudad is not None:
        self.energia -= self.ciudad.distancia_con(ciudad_destino) * 3
      self.ciudad = ciudad_destino
    else:
      pass
    return self.ciudad

#   def self.distancia(self, una_ciudad): #pasado a ciudadCls

Pepita = pajaritoClass(nombre="Pepita")
# module Pepita
#   self.energia = 100
#   self.ciudad = Oberá
Pepita.energia = 100
Pepita.ciudad = Oberá

Norita = pajaritoClass(nombre="Norita")
Mercedes  = pajaritoClass(nombre="Mercedes")

def mercedes_cantar():
  # module Mercedes
  #   def self.cantar!
  #     "♪ una voz antigua de viento y de sal ♫"
  result = "♪ una voz antigua de viento y de sal ♫"
  return result

Mercedes.cantar=mercedes_cantar #TODO: extender la clase?
