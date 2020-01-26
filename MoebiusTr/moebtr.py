"""Required data structures for Moebius transformation, homogeneous complex 2D coordinates and more."""

import numpy as np

class MoebTr:

    def __init__(self, a, b, c, d):
        self._mat = np.array([[complex(a), complex(b)],
                              [complex(c), complex(d)]])

    def __add__(self, othertr):
        return self._mat + othertr._mat

    def __sub__(self, othertr):
        return self._mat - othertr._mat

    def __mul__(self, othertr):
        return self._mat.dot(othertr._mat)

    def __getitem__(self, key):
        return self._mat[key]

    def __repr__(self):
        return f'MoebTr({self._mat[0][0]}, {self._mat[0][1]}, {self._mat[1][0]}, {self._mat[1][1]})'

    @classmethod
    def fromTo(cls, α, β, γ, x, y, z):
        """Creates the Moebius transformation mapping 3 complex numbers (α, β, γ) to (x, y, z)

        Note:
            Is a class method, which can be called using: MoebTr.fromTo(...)

        Args:
            α, β, γ: The 3 points from the domain.
            x, y, z: The 3 points in the image on which to map α, β, γ, respectively.

        Returns:
            The Moebius Transformation to map points (α, β, γ) to (x, y, z).
        """

        # if isinstance(pt, HComplex):
        # VÉRIFIER si les points sont complexes ou HComplexes

        Mabc = MoebTr._toRef(α, β, γ)
        Mxyz = MoebTr._toRef(x, y, z)

        tr = MoebTr(1, 0, 0, 1)
        tr._mat = np.linalg.inv(Mxyz).dot(Mabc)
        return tr

    @classmethod
    def _toRef(cls, α, β, γ):
        """ Returns a numpy 2x2 array for the Moebius transformation \
        between complex numbers (α, β, γ) and (0, 1, ∞)"""
        return np.array([[β - γ, -1 * α * (β - γ)],
                         [β - α, -1 * γ * (β - α)]])

    def dot(self, z):
        """Apply the Moebius transform to a point, in homogeneous coordinates.

        Args:
            z: A HComplex point or complex number.

        Returns:
            The resulting HComplex number from the product: M.z, where M is the Moebius \
            transformation encoded in this object.
        """
        if isinstance(z, complex) or isinstance(z, float) or isinstance(z, int):
            z = HComplex(z)

        mult = self._mat.dot(z[:])

        res = HComplex(mult[0], mult[1])

        return res


class HComplex:

    def __init__(self, z, w=1):
        self._vector = np.array([complex(0), complex(1)])
        self._vector[1] = complex(w)

        if w == 0:
            self._vector[0] = complex(1)
        else:
            self._vector[0] = complex(z)

    def __add__(self, otherhc):
        res = self._vector[0] + self._vector[1] * otherhc._vector[0] / otherhc._vector[1]
        return HComplex(res, self._vector[1])

    def __sub__(self, otherhc):
        res = self._vector[0] - self._vector[1] * otherhc._vector[0] / otherhc._vector[1]
        return HComplex(res, self._vector[1])

    def __mul__(self, otherhc):
        res = self._vector * otherhc._vector
        return HComplex(res[0], res[1])

    def __str__(self):
        if self._vector[1] == 0:
            return "∞"
        else:
            return str(self._vector[0] / self._vector[1])

    def __getitem__(self, key):
        return self._vector[key]

    def __repr__(self):
        return f'HComplex({self._vector[0]}, {self._vector[1]})'

    def __bool__(self):
        return self._vector[0] == 0

    def homogenize(self):
        if self._vector[1] == 0:
            self._vector[0] = 1
        else:
            self._vector[0] = self._vector[0] / self._vector[1]
            self._vector[1] = 1


# TODO - La classe Circle devrait être développé en prenant en compte l'affichage.
class Circle:
    pass

if __name__ == "__main__":
    print("Coming soon.")
