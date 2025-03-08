import numpy as np
import matplotlib.pyplot as plt

def generar_symb(num_samples, s, SF, BW, Ts, Fs):
    symb_f = np.zeros(num_samples, dtype=np.float64)
    symb_t = np.zeros(num_samples, dtype=np.complex128)

    for n in range(num_samples):
        t = n / Fs  # Tiempo actual [S]

        # Calculamos la frecuencia instantánea desplazada por el símbolo 's'
        # La frecuencia instantánea varía linealmente con el tiempo, desplazada por el símbolo 's'
        symb_f[n] = ((BW / Ts) * t + (s * BW / 2**SF)) % BW

        # Calculamos la fase acumulada para el chirp
        # La fase es la integral de la frecuencia instantánea con respecto al tiempo
        fase = 2 * np.pi * ((BW / Ts) * (t**2 / 2) + (s * BW / 2**SF) * t)
        
        # Generamos el chirp en el dominio del tiempo basado en la fase acumulada
        symb_t[n] = (1 / np.sqrt(2**SF)) * np.exp(1j * fase)
    
    return symb_t, symb_f

def agregar_ruido(signal, SNR, ruido, mu_re=0, mu_im=0):
    if ruido == 0:  # Sin ruido - canal ideal
        return signal
    
    else:  # Ruido AWGN   
        # Cálculo de potencia de la señal
        potencia_signal = np.mean(np.abs(signal)**2)         # Varianza de la señal (asumiendo media cero)
        potencia_signal_db = 10 * np.log10(potencia_signal)  # Conversión a decibelios

        # Cálculo de la potencia del ruido
        potencia_ruido_db = potencia_signal_db - SNR
        potencia_ruido = 10 ** (potencia_ruido_db / 10)

        # Ajuste de la desviación estándar del ruido según la potencia deseada
        desviacion_standard_ruido = np.sqrt(potencia_ruido / 2)

        # Generación de ruido blanco complejo
        ruido_real = np.random.normal(mu_re, desviacion_standard_ruido, len(signal))
        ruido_imag = np.random.normal(mu_im, desviacion_standard_ruido, len(signal))
        ruido = ruido_real + 1j * ruido_imag

        # Añadir ruido a la señal original
        signal_con_ruido = signal + ruido

        return signal_con_ruido
    
    def calcular_base_down_chirp(num_samples, SF, BW, Ts, Fs):
    symb_f = np.zeros(num_samples, dtype=np.float64)
    symb_t = np.zeros(num_samples, dtype=np.complex128)
    
    for n in range(num_samples):
        t = n / Fs  # Tiempo actual [s]

        # Calculamos la frecuencia instantánea para un down-chirp
        # La frecuencia instantánea disminuye linealmente con el tiempo
        symb_f[n] = BW * (1 - t / Ts)
        
        # Calculamos la fase acumulada para el down-chirp
        # La fase acumulada es la integral de la frecuencia instantánea
        fase = 2 * np.pi * BW * (t - (t**2 / (2*Ts)))

        # Generamos el down-chirp en el dominio del tiempo basado en la fase acumulada
        symb_t[n] = (1 / np.sqrt(2**SF)) * np.exp(-1j * fase)
        
    return symb_t, symb_f


s = 10                  # Símbolo a representar
SF = 7                  # Spreading Factor [7,8,9,10,11,12]
BW = 1000               # Ancho de banda
Fs = 1000000            # Frecuencia de muestreo [Hz]

Ts = (2**SF) / BW       # Periodo de cada símbolo [S]
num_samples = int(Ts * Fs) # Número de muestras

[signal_t, signal_f] = generar_symb(num_samples, s, SF, BW, Ts, Fs)

time_axis = np.arange(num_samples) * 1000 / Fs     # Vector tiempo [mS]
cant_simb = 2**SF                                  # Cantidad de símbolos

[base_down_chirp_t, base_down_chirp_f] = calcular_base_down_chirp(num_samples, SF, BW, Ts, Fs)

# Asegúrate de que signal_con_ruido sea el resultado de añadir ruido a la señal
dechirped = signal_t * np.conj(base_down_chirp_t)

dechirped_fft = np.fft.fft(dechirped)

# Normalización de la potencia
power = np.abs(dechirped_fft[:num_samples // 2])**2 / num_samples
# Si usas `num_samples // 2`, esto considera solo la mitad positiva del espectro

# Encontramos el índice de la frecuencia con la máxima potencia
max_index = np.argmax(power)
# Determinamos el símbolo transmitido basado en el índice de frecuencia
symbol_detected = max_index % (2**SF)
print(f"Símbolo detectado: {symbol_detected}")

# Ajustar el vector de símbolos y la potencia
symbols = np.arange(cant_simb)  # Crear un vector que vaya de 0 a 2^SF - 1
power_symbols = np.zeros(cant_simb)
# Solo considerar el rango de frecuencias relevantes
for i in range(cant_simb):
    if i < len(power):
        power_symbols[i] = power[i]

# Gráficas
plt.figure(figsize=(10, 12))

# Subplot 5: Potencia de cada símbolo
plt.subplot(5, 1, 1)
plt.plot(symbols, power_symbols, marker='o')

plt.title(f"Potencia de los símbolos demodulados con un factor de dispersión {SF}")
plt.xlabel("Símbolos")
plt.ylabel("Potencia [W]")
plt.grid()

plt.tight_layout()
plt.show()
