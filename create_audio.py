import numpy as np
from scipy.io.wavfile import write

sr = 22050  

# Gunshot (short burst)
gunshot = np.random.uniform(-1, 1, sr//10)
write("gunshot.wav", sr, gunshot.astype(np.float32))

# Chainsaw (continuous noise)
chainsaw = np.random.uniform(-0.5, 0.5, sr*2)
write("chainsaw.wav", sr, chainsaw.astype(np.float32))

# Safe (smooth sound)
t = np.linspace(0, 2, sr*2)
safe = 0.1 * np.sin(2 * np.pi * 220 * t)
write("safe.wav", sr, safe.astype(np.float32))

print("Audio files created!")