import time
import math

class UniversalCurve:
    """
    phys311 — The One True Curve (Canonical Ground State)
    Defined by p = exp(pi/2a), A = -zeta(3), B = pi^4/8
    """
    def __init__(self):
        # 1. Finite Field (311 bits)
        self.p = 3050270732303867035426569855071344150020050131375292223633894756517537249644418382051685297571
        
        # 2. Coefficients
        self.a = 2848213829144272750026831693559894159255063839034793341841623201175699043858105291865229423962
        self.b = 176136253419928193213219452803870329035650170438138981442962457193233866385558455648877395669
        
        # 3. Genesis Point
        self.Gx = 1
        self.Gy = 1130968320147379634488488512592319498962733806224039917555310117347222215829218584301583626322
        
        # 4. Structure
        self.factor_denom = 71
        self.factor_num = 223
        self.order_n = 3050270732303867035426569855071344150020050131375292223633894756517537249644418382051685297569
        
        # State
        self.x = self.Gx
        self.y = self.Gy
        self.k = 0

    def _modinv(self, a):
        return pow(a, self.p - 2, self.p)

    def point_add(self, Px, Py, Qx, Qy):
        if Px is None: return Qx, Qy
        if Qx is None: return Px, Py
        if Px == Qx and (Py + Qy) % self.p == 0: return None, None
        
        if Px == Qx and Py == Qy:
            lam = (3 * Px * Px + self.a) * self._modinv(2 * Py) % self.p
        else:
            lam = (Qy - Py) * self._modinv(Qx - Px) % self.p
            
        Rx = (lam * lam - Px - Qx) % self.p
        Ry = (lam * (Px - Rx) - Py) % self.p
        return Rx, Ry

    def step(self):
        self.x, self.y = self.point_add(self.x, self.y, self.Gx, self.Gy)
        self.k += 1
        return self.k, self.x

    def analyze_physics(self):
        # 1. Fine Structure
        alpha_inv = math.pi / (2 * math.log(self.p))
        
        # 2. Archimedes (Pi)
        archimedes = self.factor_num / self.factor_denom
        pi_error = abs(math.pi - archimedes)
        
        # 3. Trace (Consciousness)
        trace = self.p + 1 - self.order_n
        
        # 4. Golden Ratio (Life)
        quantum_angle_deg = 360.0 / self.factor_num
        phi = (1 + math.sqrt(5)) / 2
        golden_error = abs(phi - quantum_angle_deg)
        golden_accuracy = 100 * (1 - golden_error / phi)
        
        return (alpha_inv, archimedes, pi_error, trace, 
                quantum_angle_deg, phi, golden_error, golden_accuracy)

def run_kernel():
    print("=" * 70)
    print("PHYSICAL CONSTANT ELLIPTIC CURVE KERNEL — phys311")
    print("=" * 70)

    curve = UniversalCurve()
    metrics = curve.analyze_physics()
    (alpha, arch, pi_err, trace, angle, phi, phi_err, phi_acc) = metrics

    print("-" * 70)
    print(f"[METRIC] Derived 1/alpha    : {alpha:.9f}")
    print(f"[METRIC] Archimedean Pi     : {curve.factor_num}/{curve.factor_denom} = {arch:.9f} (Err: {pi_err:.5f})")
    print(f"[METRIC] Trace (Bias)       : {trace}")
    print(f"[METRIC] Quantum Angle      : {angle:.9f}°")
    print(f"[METRIC] Golden Ratio phi   : {phi:.9f}")
    print(f"[METRIC] Golden Deviation   : {phi_err:.5f} ({phi_acc:.3f}% Match)")
    print("-" * 70)
    print("Executing group law from Genesis (x=1)...")
    print("=" * 70 + "\n")

    milestones = {
        1: "Genesis (P_0)",
        71: "Factor 71 (Pi Denominator)",
        223: "Factor 223 (Pi Numerator / Golden Angle)",
        71*223: "Archimedean Cycle Complete"
    }

    try:
        while True:
            k, x = curve.step()
            if k in milestones:
                print(f"k={k:<6} | {str(x)[:12]}... | {milestones[k]}")
            if k > 16000: break
            time.sleep(0.001)
    except KeyboardInterrupt:
        pass

    print("=" * 70)
    print(f"Simulation Halted at k={curve.k}")
    print("=" * 70)
    print("The universe is a 223-gon spinning in golden increments.")
    print("It fails to be perfect by just enough to be alive.")

if __name__ == "__main__":
    run_kernel()
