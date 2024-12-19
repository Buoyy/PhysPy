import math

class vector:
    """
    A 3D vector class.
    -----------------
    Attributes:
    ----------
    x -- The x component of the vector,
    y -- The y component of the vector,
    z -- The z component of the vector,
    mag -- The magnitude of the vector,
    dir -- A tuple storing the direction cosines of the vector.

    Methods:
    -------
    normalized -- Returns the normalized vector,
    dir_degrees -- Returns a tuple with the direction of the vector with angles in degrees
    """

    def __init__(self, x: float, y: float, z: float):
        """
        Parameters:
        ----------
        x -- The x component of the vector,
        y -- The y component of the vector,
        z -- The z component of the vector
        """
        self.x = x
        self.y = y
        self.z = z
        self.mag = round((x ** 2 + y ** 2 + z ** 2)**(0.5), 2)

        self.dir = (math.acos(x / self.mag), math.acos(y / self.mag),
                    math.acos(z / self.mag))

    def __str__(self):
        """Overloads the 'str' function for a vector."""
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        """Overloads the '+' operator for two vectors such that 3D vectors may be added to both 2D and 3D vectors."""
        if isinstance(other, vector):
            return vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError(f'Unsupported operand type(s) for : vector and {type(other)}')

    def __sub__(self, other):
        """Overloads the '-' operator for two vectors such that 3D vectors may be subtracted from both 2D and 3D vectors."""
        if isinstance(other, vector):
            return vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError(f'Unsupported operand type(s) for : vector and {type(other)}')

    def __eq__(self, other):
        """Overrides == operator for vectors"""
        if isinstance(other, vector):
            return bool(self.x == other.x and self.y == other.y and self.z == other.z)
        else:
            raise NotImplementedError(f'Operation \'==\' is not defined for vector and {type(other)}')
        
    def normalized(self):
        """Returns a normalized vector."""
        return vector(self.x / self.mag, self.y / self.mag, self.z / self.mag)

    def dir_degrees(self):
        """Returns a tuple with the direction of the vector with angles in degrees."""
        return (math.degrees(self.dir[0]), math.degrees(self.dir[1]), math.degrees(self.dir[2]))