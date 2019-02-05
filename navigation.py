# -*- coding: utf-8 -*-

"""
Created on Mon Mar 5 21:38:24 2018
@author: anastasiia brikun

"""

import iBeacon_navigation as ibng
import time

key,tx_power = ibng.key_generation()
print("Найден beacon-маячок:\n " + key)
print ("Вычисляем расстояние до маячка...")

time.sleep(3)

rssi = ibng.get_rssi(tx_power)

dictance = ibng.get_distance(rssi,tx_power)

if dictance == -1:
  print ("""Расстояние определить невозможно из-за отсутствия сигнала""")
else:
  print ("Расстояние до маячка " + str(dictance) + " метров")
