# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:43:22 2021

@author: luisv
"""
file=open('devices.txt')

while True:
    n=input('Ingrese un nuevo item: ')
    if n =='exit':
        print('Listo')
        break
    else:
        file.write(n + '\n')
   
        
file.close()

