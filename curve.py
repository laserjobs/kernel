import time
import math


class UniversalCurve:
    """phys311 — The One True Curve (Canonical Ground State)"""
    def __init__(self):
        self.p = 3050270732303867035426569855071344150020050131375292223633894756517537249644418382051685297571
        self.a = 2848213829144272750026831693559894159255063839034793341841623201175699043858105291865229423962
        self.b = 176136253419928193213219452803870329035650170438138981442962457193233866385558455648877395669

        self.Gx = 1
        self.Gy = 1130968320147379634488488512592319498962733806224039917555310117347222215829218584301583626322

        self.factor_denom = 71
        self.factor_num   = 223
        self.order_n = 3050270732303867035426569855071344150020050131375292223633894756517537249644418382051685297569

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
        alpha = math.pi / (2 * math.log(self.p))
        archimedes = self.factor_num / self.factor_denom
        pi_error = abs(math.pi - archimedes)
        trace = self.p + 1 - self.order_n
        vacuum_bias = trace / self.p
        return alpha, archimedes, pi_error, trace, vacuum_bias


def run_kernel():
    print("=" * 70)
    print("PHYSICAL CONSTANT ELLIPTIC CURVE KERNEL — phys311")
    print("The One True Curve — Canonical Ground State")
    print("=" * 70)

    curve = UniversalCurve()
    alpha, arch, error, trace, vac = curve.analyze_physics()

    print("-" * 70)
    print(f"[METRIC] Derived 1/α          : {alpha:.9f}")
    print(f"[METRIC] Archimedes' Ratio    : {curve.factor_num}/{curve.factor_denom} = {arch:.12f}")
    print(f"[METRIC] Standard π          : {math.pi:.12f}")
    print(f"[METRIC] Geometric Error δ   : {error:.12f}")
    print(f"[METRIC] Trace of Frobenius  : {trace} (Exact)")
    print(f"[METRIC] Vacuum Bias (Λ proxy): {vac:.3e}")
    print("-" * 70)
    print("Executing group law from Genesis (x=1)...")
    print("=" * 70 + "\n")

    milestones = {
        1: "Genesis — The First Distinction",
        curve.factor_denom: f"Factor {curve.factor_denom} — Denominator Cycle",
        curve.factor_num: f"Factor {curve.factor_num} — Numerator Cycle",
        curve.factor_denom * curve.factor_num: "Archimedean Cycle Complete — Classical Reality Online"
    }

    try:
        while True:
            k, x = curve.step()
            if k in milestones:
                print(f"k={k:<6} → {milestones[k]}")
                print(f"        x = {x}\n")
            if k > curve.factor_denom * curve.factor_num + 10:
                break
            time.sleep(0.001)
    except KeyboardInterrupt:
        pass

    print("=" * 70)
    print(f"Current cosmic tick: k = {curve.k}")
    print(f"Current coordinate x = {curve.x}")
    print("=" * 70)
    print("The universe is a 223-gon with triadic bias.")
    print("And it is perfect, watching itself approximate π.")
    print("To Us.")


if __name__ == "__main__":
    run_kernel()
