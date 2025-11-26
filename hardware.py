# hardware.py
# The Key — srf311t1 elliptic curve group law

class srf311t1:
    def __init__(self):
        self.p = 3050270732303867035426569855071344150020050131375292223633894756517537249644418382051685297571
        self.a = 2848213829144272750026831693559894159255063839034793341841623201175699043858105291865229423962
        self.b = 176136253419928193213219452803870329035650170438138981442962457193233866385558455648877395669
        
        self.Gx = 1
        self.Gy = 1130968320147379634488488512592319498962733806224039917555310117347222215829218584301583626322
        self.G = (self.Gx, self.Gy)
        self.O = None  # Point at infinity

    def _modinv(self, a):
        return pow(a, -1, self.p) if a % self.p != 0 else 0

    def point_add(self, P, Q):
        if P == self.O: return Q
        if Q == self.O: return P
        
        Px, Py = P
        Qx, Qy = Q

        if (Px % self.p) == (Qx % self.p) and (Py % self.p) == (self.p - Qy % self.p):
            return self.O

        if Px == Qx and Py == Qy:
            if Py == 0: return self.O
            lam = (3 * Px * Px + self.a) * self._modinv(2 * Py) % self.p
        else:
            if Px == Qx: return self.O
            lam = (Qy - Py) * self._modinv(Qx - Px) % self.p

        Rx = (lam * lam - Px - Qx) % self.p
        Ry = (lam * (Px - Rx) - Py) % self.p
        return (Rx, Ry)
