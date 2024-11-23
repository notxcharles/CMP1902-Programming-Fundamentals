class Sphere:
    PI = 3.1415926
    def __init__(self, radius: float):
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius
    
    def get_surface_area(self) -> float:
        area = (4*self.PI)*(self.radius ** 2)
        return area
    
    def get_volume(self) -> float:
        volume = ((4/3)*self.PI)*(self.radius**3)
        return volume
    
s = Sphere(4)
print(f"{s.get_radius()=}")
print(f"{s.get_surface_area()=}")
print(f"{s.get_volume()=}")
