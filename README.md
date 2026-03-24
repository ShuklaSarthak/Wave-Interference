# 📊 Computational Modeling of Multi-Frequency Wave Interference

## 📌 Overview
This project presents a *computational simulation of wave interference* using Python. It demonstrates how two sinusoidal waves with different frequencies, amplitudes, and phase shifts combine to form a complex waveform through the *principle of superposition*.

The simulation provides a clear visualization of how simple harmonic waves interact, making it easier to understand important concepts in *physics, signal processing, and engineering*.

---
## 🎯 Objectives
- To understand the concept of *wave interference*
- To simulate sinusoidal waves using Python
- To visualize *constructive and destructive interference*
- To analyze the effect of *frequency, amplitude, and phase*
- To connect theory with *real-world applications*

---

## ⚙️ Tools & Technologies
- *Python 3.x*
- *NumPy* → Efficient numerical computation
- *Matplotlib* → Data visualization and plotting

---

## 🧠 Concepts Covered
- Simple Harmonic Motion (SHM)
- Sine wave modeling
- Superposition principle
- Constructive interference
- Destructive interference
- Phase shift and its effects
- Harmonic relationships
- Signal representation

---

## 📐 Mathematical Model

### 🔹 Sine Wave Equation
y(t) = A sin(2πft + φ)
Where:
- *A* → Amplitude (maximum displacement)
- *f* → Frequency (Hz)
- *t* → Time (seconds)
- *φ* → Phase shift (radians)

---

### 🔹 Superposition Principle
intf(t) = w1(t) + w2(t)
This means the resulting wave at any time is the *sum of the individual waves*.

---

## 📊 Wave Parameters Used

| Parameter | Wave 1 | Wave 2 |
|----------|--------|--------|
| Frequency | 5 Hz | 10 Hz |
| Amplitude | 1.0 | 0.8 |
| Phase | 0 | π/4 |

---

## 💻 Code Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

# Time array (0 to 3 seconds)
time = np.linspace(0, 3, 1000)

# Wave parameters
f1, f2 = 5, 10
amp1, amp2 = 1, 0.8
phase1, phase2 = 0, np.pi/4

# Generate sine waves
w1 = amp1 * np.sin(2 * np.pi * f1 * time + phase1)
w2 = amp2 * np.sin(2 * np.pi * f2 * time + phase2)

# Superposition (Interference)
intf = w1 + w2

# Plot results
plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(time, w1)
plt.title("Wave 1 (5 Hz)")

plt.subplot(3,1,2)
plt.plot(time, w2)
plt.title("Wave 2 (10 Hz)")

plt.subplot(3,1,3)
plt.plot(time, intf)
plt.title("Interference Pattern")

plt.tight_layout()
plt.show()
