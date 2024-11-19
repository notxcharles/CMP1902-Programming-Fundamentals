class Cube():
    PI = 3.1415926
    def __init__(self, side_length):
        self.side_length = side_length

    def get_side_length(self) -> float:
        return self.side_length
    
    def get_surface_area(self) -> float:
        area = 6*(self.side_length**2)
        return area
    
    def get_volume(self) -> float:
        volume = self.side_length**3
        return volume
    
c = Cube(4)
print(f"{c.get_side_length()=}")
print(f"{c.get_surface_area()=}")
print(f"{c.get_volume()=}")
