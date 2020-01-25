import numpy as np

class MoebTr:

    def __init__(self, a, b, c, d):
        self.mat = np.array([[complex(a), complex(b)],
                             [complex(c), complex(d)]])

    @classmethod
    def fromTo(cls, alpha, beta, gamma, x, y, z):

        Mabc = MoebTr._toRef(alpha, beta, gamma)
        Mxyz = MoebTr._toRef(x, y, z)

        tr = MoebTr(1,0,0,1)
        tr.mat = np.linalg.inv(Mxyz).dot(Mabc)
        return tr

    @classmethod
    def _toRef(self, alpha, beta, gamma):
        return np.array( [[beta - gamma, -1 * alpha * ( beta - gamma)],
                         [beta - alpha, -1 * gamma * (beta - alpha)]] )

class HComplex:

    values = np.array([complex(0, 0), complex(1, 0)]) # [0,1]

    def __init__(self, z, w = 1):
        self.values[0] = complex(z)
        self.values[1] = complex(w)

        if w == 0:
            self.values[0] = complex(1)


if __name__ == "__main__":
    print("Coming soon.")