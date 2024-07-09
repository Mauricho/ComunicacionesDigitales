clear all, close all, clc;

% Se definen características de la modulación
SF = 8;
BW = 1000;
Fs = 1000;
s = 189;
SNR = -10;

% Número de muestras
num_samples = (2^SF)*Fs/BW;
k = s;
lora_symbol = zeros(1,num_samples);

% Se obtiene la señal modulada para el símbolo dado s
for n=1:num_samples

   if k >= (2^SF)
     k = k-2^SF;
   endif

   k = k +1;
   lora_symbol(n) = (1/(sqrt(2^SF)))*exp(1i*2*pi*k*(k/(2^SF*2)))

endfor

for j = 1:100

%Agrega ruido
lora_symbol_noisy = awgn(lora_symbol,SNR, 'measured');

%Transmite y se genera el chirp para demodular
base_down_chirp = zeros(1, num_samples);
k = 0;
for n=1:num_samples
  if k>=(2^SF)
    k = k - 2^SF;
  endif
  k = k + 1
  base_down_chirp(n) = (1/(sqrt(2^SF)))*exp(-1i*2*pi*k*(k/(2^SF*2)))
endfor

%Demodulación
dechirped = lora_symbol_noisy.*(base_down_chirp);

%Transformada rápida de Fourier- correlación
corrs = (abs(fft(dechirped)).^2);

%Figura 1
figure(1)
plot(corrs)
titleText = "Espectro de frecuencias para símbolo " + s + ", factor de dispersión " + SF + " y SNR de " + SNR + " dB"
title(titleText)

[~,ind] = max(corrs);
ind2(j) = ind;
pause(0.01)

endfor

%Figure 2
figure(2)
histogram(ind2, 2^SF)

%Error de correlación
symbol_error_rate = sum(ind2 ~=s+1)/j

