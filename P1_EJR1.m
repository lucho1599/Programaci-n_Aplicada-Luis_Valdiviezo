clear all; %borra variables creadas en el workspace
clc; %limpia la ventana
close all;
T=1E-06
fs= 1/T;  %T=1us
t=0:0.001/fs:0.000008; %Vector de tiempo
x=2*(square(2*pi*fs*t)+1); 
plot(t,x); %grafica x,y
axis([0 8E-06 -4.5 4.5]); %visualización de periodos
title('SEÑAL CUADRADA')
ylabel('AMPLITUD')
xlabel('TIEMPO')
