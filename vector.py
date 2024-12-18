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

    def __init__(self, x: float | None = 0 , y: float | None = 0, z: float | None = 0):
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
        """Overloads the '+' operator for two vectors."""
        if isinstance(other, vector):
            return vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError(f'Unsupported operand type(s) for : {type(self)} and {type(other)}')

    def __sub__(self, other):
        """Overloads the '-' operator for two vectors."""
        if isinstance(other, vector):
            return vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError(f'Unsupported operand type(s) for : {type(self)} and {type(other)}')

    def __mul__(self, other):
        """Overloads the '*' operator for a vector and a scalar for scalar multiplication."""
        if isinstance(other, (int, float)):
            return vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, vector):
            raise TypeError(f'Unsupported operand type(s) for : {type(self)} and {type(other)}; try vector.dot() or vector.cross()')
        else:
            raise TypeError(f'Unsupported operand type(s) for : {type(self)} and {type(other)}')
    
    def __eq__(self, other):
        """Overrides == operator for vectors. A vector is equal to another vector if all their components are equal."""
        if isinstance(other, vector):
            return bool(self.x == other.x and self.y == other.y and self.z == other.z)
        else:
            raise TypeError(f'Unsupported operand type(s) for : {type(self)} and {type(other)}')

    def __ne__(self, other):
        """Overrides != operator for vectors. A vector is equal to another vector if all their components are equal."""
        if isinstance(other, vector):
            return (not self==other)
        else:
            raise TypeError(f'Unsupported operand type(s) for : {type(self)} and {type(other)}')

    def __lt__(self, other):
        """Overrides < operator for vectors. A vector is less than another vector if its magnitude is less than that of other."""
        if isinstance(other, vector):
            return (self.mag < other.mag)
        else:
            raise TypeError(f'Unsupported operand type(s) for : {type(self)} and {type(other)}')

    def __gt__(self, other):
        """Overrides > operator for vectors. A vector is more than another vector if its magnitude is more than that of other."""
        if isinstance(other, vector):
            return (self.mag > other.mag)
        else:
            raise TypeError(f'Unsupported operand type(s) for : {type(self)} and {type(other)}')

    def __le__(self, other):
        """Overrides <= operator for vectors. A vector is less than another vector if its magnitude is more than that of other."""
        if isinstance(other, vector):
            return (self.mag < other.mag) or (self == other)
        else:
            raise TypeError(f'Unsupported operand type(s) for : {type(self)} and {type(other)}')

    def __ge__(self, other):
        """Overrides >= operator for vectors. A vector is less than another vector if its magnitude is more than that of other."""
        if isinstance(other, vector):
            return (self.mag >= other.mag) or (self == other)
        else:
            raise TypeError(f'Unsupported operand type(s) for : {type(self)} and {type(other)}')

    def normalized(self):
        """Returns a normalized vector."""
        return vector(self.x / self.mag, self.y / self.mag, self.z / self.mag)

    def dir_degrees(self):
        """Returns a tuple with the direction of the vector with angles in degrees."""
        return (math.degrees(self.dir[0]), math.degrees(self.dir[1]), math.degrees(self.dir[2]))

    def dot(self, other):
        if isinstance(other, vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError(f'Unsupported operand type(s) for : {type(self)} and {type(other)}')
        
    def cross(self, other):
        if isinstance(other, vector):
            return vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
        else:
            raise TypeError(f'Unsupported operand type(s) for : {type(self)} and {type(other)}')