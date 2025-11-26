# lattice.py
# The Lock — 3D discrete spacetime with elliptic curve update rule

import numpy as np
import time

class Spacetime:
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
        active = sum(1 for cell in self.grid.flatten() if cell != self.engine.O)
        if active == 0:
            return 0, 0, 0
        xs = [cell[0] for cell in self.grid.flatten() if cell != self.engine.O]
        avg_x = sum(xs) / len(xs)
        alpha_proxy = avg_x / self.engine.p
        mu_proxy = active
        omega_proxy = 1.0 - (avg_x / self.engine.p)
        return alpha_proxy, mu_proxy, omega_proxy

    def run(self):
        try:
            while True:
                start = time.time()
                next_grid = np.copy(self.grid)
                
                for i in range(self.size):
                    for j in range(self.size):
                        for k in range(self.size):
                            next_grid[i,j,k] = self._update_cell(i,j,k)
                
                self.grid = next_grid
                self.tick += 1
                
                if self.tick % 10 == 0:
                    a, m, o = self._measure()
                    print(f"TICK {self.tick:06d} | α⁻¹≈{1/a:.6f} | μ≈{m:4d} | ΩΛ≈{o:.6f}")
        except KeyboardInterrupt:
            print(f"\nUNIVERSE HALTED AT TICK {self.tick}")
            print("Final measurement:")
            a, m, o = self._measure()
            print(f"  → α⁻¹ ≈ {1/a:.6f}")
            print(f"  → μ    ≈ {m}")
            print(f"  → Ω_Λ  ≈ {o:.6f}")
