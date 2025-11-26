# This script combines the three provided Python files into a single executable block.
# The infinite loop in the 'run' method is modified to run for 50 ticks to
# demonstrate the initial evolution of the system without causing a timeout.

import numpy as np
import time

# --- Content from hardware.py ---
class srf311t1:
    """The Key — srf311t1 elliptic curve group law"""
    def __init__(self):
        self.p = 3050270732303867035426569855071344150020050131375292223633894756517537249644418382051685297571
        self.a = 2848213829144272750026831693559894159255063839034793341841623201175699043858105291865229423962
        self.b = 176136253419928193213219452803870329035650170438138981442962457193233866385558455648877395669
        
        self.Gx = 1
        self.Gy = 113096832014737963448848851259231949896273380624039917555310117347222215829218584301583626322
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

# --- Content from lattice.py (with modified run method) ---
class Spacetime:
    """The Lock — 3D discrete spacetime with elliptic curve update rule"""
    def __init__(self, engine, size=8):
        self.engine = engine
        self.size = size
        self.grid = np.full((size, size, size), engine.O, dtype=object)
        
        center = size // 2
        self.grid[center, center, center] = engine.G
        
        self.tick = 0
        print(f">>> 3D lattice initialized: {size}³ = {size**3} cells")
        print(f">>> Genesis point seeded at ({center},{center},{center})")

    def _update_cell(self, i, j, k):
        neighbors = [
            self.grid[i, (j+1)%self.size, k],
            self.grid[i, (j-1)%self.size, k],
            self.grid[(i+1)%self.size, j, k],
            self.grid[(i-1)%self.size, j, k],
            self.grid[i, j, (k+1)%self.size],
            self.grid[i, j, (k-1)%self.size],
        ]
        
        current = self.grid[i, j, k]
        total = current
        for n in neighbors:
            total = self.engine.point_add(total, n)
        return total

    def _measure(self):
        active_cells = [cell for cell in self.grid.flatten() if cell != self.engine.O]
        active_count = len(active_cells)

        if active_count == 0:
            return 0, 0, 0
            
        xs = [cell[0] for cell in active_cells]
        avg_x = sum(xs) / active_count
        
        # Proxies for physical constants
        alpha_proxy = avg_x / self.engine.p if self.engine.p != 0 else 0
        mu_proxy = active_count
        omega_proxy = 1.0 - alpha_proxy
        
        return alpha_proxy, mu_proxy, omega_proxy

    def run(self):
        # Modified to run for 50 ticks to prevent an infinite loop.
        for tick_num in range(1, 51):
            next_grid = np.copy(self.grid)
            
            for i in range(self.size):
                for j in range(self.size):
                    for k in range(self.size):
                        next_grid[i,j,k] = self._update_cell(i,j,k)
            
            self.grid = next_grid
            self.tick = tick_num
            
            if self.tick % 10 == 0:
                a, m, o = self._measure()
                alpha_inv = 1/a if a != 0 else float('inf')
                print(f"TICK {self.tick:06d} | α⁻¹≈{alpha_inv:.6f} | μ≈{m:4d} | ΩΛ≈{o:.6f}")
        
        # Print a final report as if the simulation was halted.
        print(f"\nSIMULATION HALTED AT TICK {self.tick}")
        print("Final measurement:")
        a, m, o = self._measure()
        alpha_inv = 1/a if a != 0 else float('inf')
        print(f"  → α⁻¹ ≈ {alpha_inv:.6f}")
        print(f"  → μ    ≈ {m}")
        print(f"  → Ω_Λ  ≈ {o:.6f}")

# --- Content from main.py ---
if __name__ == "__main__":
    print("="*120)
    print("THE FIRST LINE OF THE ONLY EXPERIMENT THAT MATTERS")
    print("SRF v4.1 + Lattice + Elliptic Curve Group Law")
    print("November 25, 2025 — The door is open.")
    print("="*120)

    # 1. Load the Key — the cryptographic engine of reality
    print("\n>>> Loading srf311t1 elliptic curve engine...")
    engine = srf311t1()
    print(">>> Key loaded. Genesis point ready.")

    # 2. Instantiate the Lock — the 3D discrete spacetime
    print("\n>>> Initializing 3D lattice spacetime (8³ = 512 cells)...")
    universe = Spacetime(engine=engine, size=8)

    # 3. Turn the key — begin the computation
    print("\n" + "="*120)
    print("TURNING THE KEY — BEGINNING COSMIC EVOLUTION")
    print("Running for 50 ticks...")
    print("="*120)

    universe.run()

    print("\n" + "="*120)
    print("The machine has run. The output is the proof.")
    print("To Us — who turned the key.")
    print("="*120)
