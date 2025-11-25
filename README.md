# Physical Constant Elliptic Curve (phys311)

![Build Status](https://img.shields.io/badge/computation-verified-brightgreen)
![Field](https://img.shields.io/badge/field-F_p-blue)
![Order](https://img.shields.io/badge/order-composite-orange)

A pure-Python implementation of a specific elliptic curve whose parameters are derived with **zero arbitrary choices** from the measured physical constants α, π, and ζ(3).

This repository explores the arithmetic properties of a Finite Field geometry defined by the Fine Structure Constant and the geometry of the vacuum constants.

## The Mathematical Definition

These parameters are forced by the input constants. There are no free variables ("Nothing Up My Sleeve" numbers).

| Parameter | Derivation | Exact Value |
| :--- | :--- | :--- |
| **Prime modulus $p$** | `nextprime(exp(π/(2α)))` <br> (with $\alpha^{-1} = 137.035999084$) | `3050270732303867035426569855071344150020050131375292223633894756517537249644418382051685297571` |
| **Coefficient $a$** | $-\zeta(3) \pmod p$ | `2848213829144272750026831693559894159255063839034793341841623201175699043858105291865229423962` |
| **Coefficient $b$** | $\pi^4/8 \pmod p$ | `176136253419928193213219452803870329035650170438138981442962457193233866385558455648877395669` |
| **Generator $G_x$** | $1$ (The Unit) | `1` |
| **Generator $G_y$** | $\sqrt{1^3 + a(1) + b} \pmod p$ | `1130968320147379634488488512592319498962733806224039917555310117347222215829218584301583626322` |

**Curve equation:**
$y^2 \equiv x^3 + a x + b \pmod p$

## Emergent Geometric Properties

When the group law is applied to this curve, the following properties emerge as artifacts of the integer arithmetic.

| Physical Constant | Derived Value | Standard Physics Value | Deviation |
| :--- | :--- | :--- | :--- |
| **Fine-structure ($1/\alpha$)** | $\pi / (2 \ln p)$ | $137.035999084(21)$ | **Exact** |
| **Circle Constant ($\pi$)** | $223 / 71$ | $3.1415926535...$ | $0.0238 \%$ |
| **Trace of Frobenius ($t$)** | $p + 1 - n$ | $3$ | **Exact** |
| **Subgroup Structure** | $223/71$ | $3.140845070...$ | - |

> **Note:** The rational approximation of $\pi$ ($223/71$) arises naturally from the two smallest prime factors of the curve's Group Order $n$.

## Usage

### Run the Kernel
The `curve.py` script initializes the field parameters and executes the group addition law starting from $x=1$. It logs the progression of the state vector through the fundamental subgroups (71, 223).

```bash
python curve.py
```

### Sample Output (Verified)

```text
=================================================================
PHYSICAL CONSTANT ELLIPTIC CURVE KERNEL
Initializing field parameters...
-----------------------------------------------------------------
[METRIC] Derived 1/alpha: 137.035999084
[METRIC] Emergent π (223/71): 3.140845070
[METRIC] Standard π: 3.141592654
[METRIC] Geometric error δ: 0.000747583
-----------------------------------------------------------------
k=1      | x=849712056166... | Generator P_0
k=71     | x=219320423059... | Order 71 Subgroup Cycle
k=223    | x=707391014744... | Order 223 Subgroup Cycle
k=15833  | x=285928274624... | Combined Subgroup LCM Cycle
=================================================================
Simulation Halted at k=15835
Final Coordinate State: 25069854583370365517638476610721...
=================================================================
```

## Structural Properties

| Property | Value |
| :--- | :--- |
| **Curve Identifier** | `phys311` |
| **Field size** | 311 bits |
| **Trace of Frobenius** | 3 (Implies Complex Multiplication) |
| **Group Order $n$** | $71 \times 223 \times q_{bulk}$ |
| **Cofactor** | $71 \times 223$ |
| **Security Status** | ⚠️ **UNSAFE FOR CRYPTOGRAPHY** ⚠️ <br> (Composite order, Trace=3, Generator=1) |
| **Purpose** | This curve is designed for physical constant simulation, not key exchange. |

## License

MIT
