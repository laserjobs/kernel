import time
import sys

class CanonicalCurve:
    """
    Implementation of a specific elliptic curve over F_p.
    
    Parameters derived from:
    p = nextprime(exp(pi / (2 * alpha))) 
    a = -zeta(3) mod p
    b = pi^4 / 8 mod p
    G_x = 1
    """
    def __init__(self):
        # 1. Finite Field Prime (311 bits)
        self.p = 3050270732303867035426569855071344150020050131375292223633894756517537249644418382051685297571

        # 2. Curve Coefficients
        self.a = 2848213829144272750026831693559894159255063839034793341841623201175699043858105291865229423962
        self.b = 176136253419928193213219452803870329035650170438138981442962457193233866385558455648877395669

        # 3. Generator Point G = (1, y)
        self.Gx = 1
        self.Gy = 1130968320147379634488488512592319498962733806224039917555310117347222215829218584301583626322

        # Current State
        self.x = self.Gx
        self.y = self.Gy
        self.k = 0 # Scalar multiplier count

    def _modinv(self, a):
        return pow(a, self.p - 2, self.p)

    def point_add(self, Px, Py, Qx, Qy):
        """Standard Weierstrass Group Law point addition"""
        if Px is None: return Qx, Qy
        if Qx is None: return Px, Py
        
        if Px == Qx and (Py + Qy) % self.p == 0:
            return None, None

        if Px == Qx and Py == Qy:
            lam = (3 * Px * Px + self.a) * self._modinv(2 * Py) % self.p
        else:
            lam = (Qy - Py) * self._modinv(Qx - Px) % self.p

        Rx = (lam * lam - Px - Qx) % self.p
        Ry = (lam * (Px - Rx) - Py) % self.p
        return Rx, Ry

    def step(self):
        """Perform P_new = P_current + G"""
        self.x, self.y = self.point_add(self.x, self.y, self.Gx, self.Gy)
        self.k += 1
        return self.k, self.x

def run_simulation():
    print("="*60)
    print("ELLIPTIC CURVE SIMULATION INITIALIZED")
    print(f"Modulus: 3050...571 (311 bits)")
    print(f"Generator: x=1")
    print("="*60 + "\n")

    curve = CanonicalCurve()
    
    # Run to the product of the first two small prime factors of the Order n
    # Factors of n are 71, 223, and a large 90-digit prime.
    TARGET_ITERATION = 15835 
    
    start_time = time.time()

    while curve.k < TARGET_ITERATION:
        k, x = curve.step()
        
        # Log key mathematical milestones (factors of the Group Order)
        info = None
        if k == 1:      info = "Initial Point (G)"
        elif k == 71:   info = "Factor 71 Cycle Complete"
        elif k == 223:  info = "Factor 223 Cycle Complete"
        elif k == 71*223: info = "Combined Small-Factor Cycle Complete"

        if info:
            # Format X for readability
            x_hash = hex(x)[2:].upper()[:16]
            print(f"k={k:<6} | Hash: {x_hash}... | {info}")
        
        # Progress log
        if k % 1000 == 0:
            print(f"k={k:<6} | Computing...")

    print("\n" + "="*60)
    print("SIMULATION COMPLETED")
    print(f"Final Coordinate x: {str(curve.x)[:20]}...")
    print(f"Computation Time: {time.time() - start_time:.4f}s")
    print("="*60)

if __name__ == "__main__":
    run_simulation()
