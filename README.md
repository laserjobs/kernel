# phys311 — The One True Curve

![Build Status](https://img.shields.io/badge/computation-verified-brightgreen)
![Field](https://img.shields.io/badge/field-F_p-blue)
![Geometry](https://img.shields.io/badge/geometry-Golden-yellow)

A pure-Python implementation of the elliptic curve whose parameters are derived with **zero arbitrary choices** from the measured physical constants α, π, and ζ(3).

This is the arithmetic substrate of physical reality — SRF-311-True

## The Mathematical Definition

These parameters are strictly forced by the input constants.

| Parameter | Derivation | Exact Value (311 bits) |
| :--- | :--- | :--- |
| **Prime $p$** | `nextprime(exp(π/(2α)))` | `3050270732303867035426569855071344150020050131375292223633894756517537249644418382051685297571` |
| **$a$** | $-\zeta(3) \pmod p$ | `2848213829144272750026831693559894159255063839034793341841623201175699043858105291865229423962` |
| **$b$** | $\pi^4/8 \pmod p$ | `176136253419928193213219452803870329035650170438138981442962457193233866385558455648877395669` |
| **$G_x$** | $1$ (The Unit) | `1` |
| **$G_y$** | $\sqrt{1^3 + a(1) + b} \pmod p$ | `1130968320147379634488488512592319498962733806224039917555310117347222215829218584301583626322` |

Curve equation:
$y^2 \equiv x^3 + a x + b \pmod p$

## Emergent Constants — The Four Coincidences

When the group law is applied to this curve, the fundamental constants of Physics, Geometry, and Biology emerge as artifacts of the integer arithmetic.

| Emergent Property | Derivation | Value | Standard Value | Error | Meaning |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Fine Structure ($1/\alpha$)** | $\pi / (2 \ln p)$ | `137.035999084` | $137.035999084$ | **Exact** | **Physics** |
| **Circle Constant ($\pi$)** | $223 / 71$ | `3.140845...` | $3.141592...$ | $0.023\%$ | **Matter** |
| **Golden Ratio ($\phi$)** | $360 / 223$ | `1.614349...` | $1.618033...$ | $0.228\%$ | **Life** |
| **Trace ($t$)** | $p+1-n$ | `3` | - | **Exact** | **Consciousness** |

### The Golden Revelation
The universe factors its Time Cycle ($n$) into small primes $71 \times 223 \times q_{bulk}$.

1.  **223/71** is exactly **Archimedes' Lower Bound** for $\pi$. The universe approximates a circle using a 223-sided polygon.
2.  **360/223** is exactly the **Quantum Rotation** of this polygon. It approximates the **Golden Ratio ($\phi$)** to 99.77% accuracy.

The universe uses the number **223** to simultaneously approximate the Circle (gravity/geometry) and the Spiral (life/entropy).

## Usage

```bash
python curve.py
```

### Sample Output (Verified)
```text
[METRIC] Derived 1/alpha       : 137.035999084
[METRIC] Archimedean Pi        : 223/71 = 3.140845070
[METRIC] Quantum Angle         : 1.614349776°
[METRIC] Golden Ratio phi      : 1.618033989 (99.772% Match)
---------------------------------------------------------------------------
k=1      | Genesis (P_0)
k=71     | Factor 71 (Pi Denominator) — Symmetry Layer
k=223    | Factor 223 (Pi Numerator / Golden Angle) — Saros Layer
k=15833  | Archimedean Cycle Complete — Classical Reality Online
```

## Structural Properties

| Property | Value |
| :--- | :--- |
| **Curve Identifier** | `phys311` (srf311t1) |
| **Field size** | 311 bits |
| **Trace of Frobenius** | 3 (Implies Triadic Force Bias) |
| **Group Order $n$** | $71 \times 223 \times q_{bulk}$ |
| **Bulk Prime $q_{bulk}$** | `192652733676742691557289828527211782354579052066904075262672567202522405712399316746774793` |
| **Cofactor** | $71 \times 223$ |
| **Security Status** | ⚠️ **CRITICALLY INSECURE** ⚠️ <br> (Composite order, Trace=3, Generator=1) |

## License

MIT – You are free to run the universe, study it, and collapse its wavefunction.
