#
# extra.py: traido de la guia XXX (link al repo+commit)
#

class ciudadClass:
  def __init__(self,kilometros):
    self._kilometros=kilometros

  @property
  def kilometros(self):
    #validacion
    return self._kilometros

  def distancia(self, una_ciudad):
    #   def self.distancia(self, una_ciudad):
    #     (self.ciudad.kilometro - una_ciudad.kilometro).abs
    return abs(self.kilometros - una_ciudad.kilometros)


Ushuaia = ciudadClass(0) # cercana al centro geográfico de Argentina según https://www.ign.gob.ar/gallery-app/mapas-escolares/medium/argentina_bicontinental_fisico.jpg

BuenosAires = ciudadClass(2360) #CABA está lejos de muuchas ciudades, incluyendo al centro geográfico de Argentina: https://es.wikipedia.org/wiki/Ushuaia

# module Iruya
#   def self.kilometr(self):
#     1710
Iruya=ciudadClass(kilometros=4070) #mantinene distancia con BuenosAires, pero no respeta https://es.wikipedia.org/wiki/Ushuaia

# module Obera
#   def self.kilometr(self):
#     1040
Obera=ciudadClass(kilometros=3400) #mantinene distancia con BuenosAires según https://es.wikipedia.org/wiki/Ushuaia



class pajaritoClass():
  pio='priiiip priiiip'

  def __init__(self,nombre="Pajarito"):
    self.nombre=nombre
    self._energia=0

  def cantar(self):
    print(pajaritoClass.pio)
    return None

  def __repr__(self):
    pio=pajaritoClass.pio
    return pio+" soy "+self.nombre

  @property
  def energia(self):
    return self._energia

  @energia.setter
  def energia(self,ahora_vale):
    #energia.setter
    #
    #   def self.energia=(self, una_energia):
    #     self.energia = una_energia
    #   def self.energi(self):
    #     self.energia
    self._energia=ahora_vale     #validacion?


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
    print('pri pri pri')
    return None

  def comer_lombriz(self):
    #   def self.comer_lombriz!
    #     self.energia += 20
    #     return
    self.energia += 20
    return self.energia

  def comer_alpiste(self,energia_adicional):
    #   def self.comer_alpiste!(self, una_energia):
    #     self.energia += una_energia * 15
    #     return
    self.energia += energia_adicional * 15
    return self.energia

  def volar_en_circulos(self):
    #   def self.volar_en_circulos!
    #     self.energia -= 10
    #     return
    self.energia -= 10
    return self.energia

  def volar_hacia(self, ciudad_destino):
    #   def self.volar_hacia!(self, una_ciudad):
    #     self.energia -= self.distancia(una_ciudad) * 3
    #     self.ciudad = una_ciudad
    #     return
    self.energia -= self.ciudad.distancia(ciudad_destino) * 3
    self.ciudad = ciudad_destino
    return

#   def self.distancia(self, una_ciudad): #pasado a ciudadCls

Pepita = pajaritoClass(nombre="Pepita")
# module Pepita
#   self.energia = 100
#   self.ciudad = Obera
Pepita.energia = 100
Pepita.ciudad = Obera

Norita = pajaritoClass(nombre="Norita")
Mercedes  = pajaritoClass(nombre="Mercedes")
Pajarito = pajaritoClass()

def mercedes_cantar():
  # module Mercedes
  #   def self.cantar!
  #     "♪ una voz antigua de viento y de sal ♫"
  print("♪ una voz antigua de viento y de sal ♫")

Mercedes.cantar=mercedes_cantar #TODO: extender la clase?
