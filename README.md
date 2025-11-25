# Universal Constant Elliptic Curve (srf311t1)

![Build Status](https://img.shields.io/badge/computation-verified-brightgreen)
![Field](https://img.shields.io/badge/field-F_p-blue)
![Order](https://img.shields.io/badge/order-composite-orange)

A Python implementation of the elliptic curve $E(\mathbb{F}_p)$ derived rigidly from the fundamental physical constants $\alpha$, $\pi$, and $\zeta(3)$.

This repository explores the arithmetic properties of a Finite Field geometry where the modulus $p$ is determined by the Fine Structure Constant and the curve coefficients are determined by the geometry of the vacuum.

## The Mathematical Definition

The curve parameters are strictly derived with no arbitrary choices ("Nothing Up My Sleeve" numbers):

1.  **The Prime Modulus ($p$):** Derived from the CODATA 2022 value of $\alpha^{-1} \approx 137.035999084$.
    $$ p \approx \exp\left( \frac{\pi}{2\alpha} \right) \approx 3.05 \times 10^{93} $$
2.  **The Coefficients:**
    $$ y^2 = x^3 - \zeta(3)x + \frac{\pi^4}{8} $$
3.  **The Generator:**
    $$ G_x = 1 $$

## The Computational Result

When the group law is applied to these parameters, the following metric properties emerge from the integer arithmetic:

| Metric | Derived Value | Standard Physics Value | Deviation |
| :--- | :--- | :--- | :--- |
| **Field Resolution ($2\ln p / \pi$)** | `137.035999084` | $1/\alpha \approx 137.035999084$ | **Exact** |
| **Emergent Geometry ($223/71$)** | `3.140845070` | $\pi \approx 3.141592654$ | **0.02%** |

*Note: The emergent geometry ratio ($223/71$) arises from the two smallest prime factors of the curve's Group Order $n$.*

## Usage

### Run the Kernel
The `curve.py` script initializes the field parameters and executes the group addition law starting from $x=1$. It logs the progression of the state vector through the fundamental subgroups (71, 223).

```bash
python curve.py
```

### Sample Output
```text
=================================================================
PHYSICAL CONSTANT ELLIPTIC CURVE KERNEL
Initializing field parameters...
-----------------------------------------------------------------
[METRIC] Derived 1/alpha:    137.035999084
[METRIC] Subgroup Ratio:     223 / 71 = 3.140845070
[METRIC] Standard Pi:        3.141592654
-----------------------------------------------------------------
k=1      | x=849712056166... | Generator P_0
k=71     | x=219320423059... | Order 71 Subgroup Cycle
k=223    | x=707391014744... | Order 223 Subgroup Cycle
k=15833  | x=285928274624... | Combined Subgroup LCM Cycle
```

## Structural Properties
*   **Curve:** `srf311t1`
*   **Trace of Frobenius:** $t=3$ (Implies Complex Multiplication with discriminant $D \approx -12 \cdot 10^{93}$)
*   **Group Structure:** Cyclic, Composite Order $n = 71 \times 223 \times q_{bulk}$
*   **Security:** **UNSAFE.** This curve is designed for physical simulation, not cryptography. The composite order allows for small-subgroup attacks.

## License
MIT
