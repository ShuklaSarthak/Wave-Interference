# Wave Interference Visualization
# Libraries: numpy, matplotlib

import numpy as np
import matplotlib.pyplot as plt

# 1. Define parameters
time = np.linspace(0, 3, 1000)       # time axis (0 to 2 seconds)
f1, f2 = 5, 10                       # frequencies of the waves (Hz)
amp1, amp2 = 1, 0.8                  # amplitudes
phase1, phase2 = 0, np.pi/4          # phases

# 2. Generate waves
w1 = amp1 * np.sin(2 * np.pi * f1 * time + phase1)
w2 = amp2 * np.sin(2 * np.pi * f2 * time + phase2)

# 3. Combine waves (interference)
intf = w1 + w2

# 4. Plot results
plt.figure(figsize=(12,8))

# Plot wave 1
plt.subplot(3,1,1)
plt.plot(time, w1, color='blue')
plt.title("Wave 1 (Frequency = {} Hz)".format(f1))
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot wave 2
plt.subplot(3,1,2)
plt.plot(time, w2, color='green')
plt.title("Wave 2 (Frequency = {} Hz)".format(f2))
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot interference
plt.subplot(3,1,3)
plt.plot(time, intf, color='red')
plt.title("Interference Pattern (Wave 1 + Wave 2)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
