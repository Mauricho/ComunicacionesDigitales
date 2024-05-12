import numpy as np

def raiz_coseno_realzado(simbolos, beta, T, tt):
    # Parámetros de la función raíz de coseno realzado
    alpha = 0.5  # Factor de decaimiento del coseno
    oversampling_factor = 4  # Factor de sobremuestreo
    
    # Cantidad de muestras por símbolo
    N = int(oversampling_factor * len(tt))
    
    # Crear la forma de onda de la raíz del coseno realzado
    t = np.arange(-N/2, N/2) * T / oversampling_factor
    h = np.sinc(t / T) * np.cos(np.pi * alpha * t / T) / (1 - (2 * alpha * t / T) ** 2)
    h /= np.sqrt(np.sum(h ** 2))  # Normalización de la forma de onda
    
    # Generar la señal transmitida para cada símbolo
    signal = []
    for s in simbolos:
        # Señal para el símbolo actual
        s_wave = np.zeros_like(tt)
        s_wave[::oversampling_factor] = s  # Muestreo del símbolo
        
        # Conformado de la señal con la forma de onda raíz del coseno realzado
        signal.append(np.convolve(s_wave, h, mode='same'))
    
    signal_added = np.sum(signal, axis=0)  # Suma de todas las señales
    
    return signal_added, signal

# Ejemplo de uso
simbolos = [1, -1, 1, 1, -1]  # Lista de símbolos
Beta = 0.5  # Exceso de ancho de banda
T = 1  # Periodo de símbolo
tt = np.linspace(0, 5, 1000)  # Intervalo de tiempo

signal_added, signal = raiz_coseno_realzado(simbolos, Beta, T, tt)