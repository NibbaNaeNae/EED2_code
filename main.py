import matplotlib.pyplot as plt
import numpy as np

frequency_array_hz = np.array([10,31,100,310,1000,3100,10000,31000,100000,310000,1000000])
output_array = np.array([474,474,474,470,454,350,169,73,38,33,53])
input_array = np.array([117,117,117,117,117,113,113,111,105,104,106])

gain_array = output_array/input_array
gain_array_dbs = 20 * np.log10(gain_array) 

plt.figure()
plt.semilogx(frequency_array_hz, gain_array_dbs, 'o-') # 'o-' for points connected by lines
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.title('Bode Plot (Magnitude) of Active Low Pass Filter')
plt.grid(True, which="both", ls="-") # add grid 

plt.savefig('foo.png')

plt.show()
