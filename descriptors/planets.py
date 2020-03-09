class Planet:

  def __init__(self, name, radius_meters, mass_kg, orbital_presiod_sec, surface_temp_kel):
    self.name = name
    self.radius_meters = radius_meters
    self.mass_kg = mass_kg
    self.orbital_presiod_sec = orbital_presiod_sec
    self.surface_temp_kel = surface_temp_kel
  
  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    if not value:
      raise ValueError("Cannot set empty value")
    self._name = value

  @property
  def radius_meters(self):
    return self._radius_meters

  @radius_meters.setter
  def radius_meters(self, value):
    if value <= 0:
      raise ValueError("Value has to be > 0")
    self._radius_meters = value

  @property
  def mass_kg(self):
    return self._mass_kg

  @mass_kg.setter
  def mass_kg(self, value):
    if value <= 0:
      raise ValueError("Value has to be > 0")
    self._mass_kg = value

  @property
  def orbital_presiod_sec(self):
    return self._orbital_presiod_sec

  @orbital_presiod_sec.setter
  def orbital_presiod_sec(self, value):
    if value <= 0:
      raise ValueError("Value has to be > 0")
    self._orbital_presiod_sec = value

  @property
  def surface_temp_kel(self):
    return self._surface_temp_kel

  @surface_temp_kel.setter
  def surface_temp_kel(self, value):
    if value <= 0:
      raise ValueError("Value has to be > 0")
    self._surface_temp_kel = value

##############################################

def main():
  pluto = Planet(
    name='Pluto', 
    radius_meters=1184e3, 
    mass_kg=1.305e22, 
    orbital_presiod_sec=7816012992, 
    surface_temp_kel=55
  )
  print(pluto.radius_meters)

if __name__ == '__main__':
  main()
