from strictly_positive_decorator import Positive

class Planet:

  def __init__(self, name, radius_meters, mass_kg, orbital_presiod_sec, surface_temp_kel):
    self.name = name
    #radius_meters now is an instance on a Positive descriptor, so this will call Positive.__get__
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

  # bindng an instance of the Positive descriptor to the class attribute named 'radius_meters'
  radius_meters = Positive()
  mass_kg = Positive()
  orbital_presiod_sec = Positive()
  surface_temp_kel = Positive()

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
