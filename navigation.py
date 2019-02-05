-*- coding: utf-8 -*-

"""
Created on  May 5 21:38:24 2018
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
  print ("Расстояние определить невозможно из-за отсутствия сигнала")
else:
  print ("Расстояние до маячка " + str(dictance) + " метров")


def key_generation():

""" Генерирует ключ, испускаемый beacon-маяком """

preamble = '4c000215'
uuid_key = (str(uuid.uuid4())).replace('-','')
major = digits[0:4]
minor = digits[0:4]

tx_power_etalon = ascii_lowercase[0:2]
beacon_key = preamble+uuid_key+major+minor+tx_power_etalon
return beacon_key, tx_power_etalon

def get_rssi(tx_power_etalon):
return int(('0x'+tx_power_etalon),16)

def get_distance(rssi,tx_power):

"""Определяет расстояние объекта до beacon-маяка"""

tx_power = int(tx_power, 16)

if rssi == 0:
  return -1 #расстояние не определить из-за отсутсвия мощности сигнала/

ratio = rssi/tx_power

if ratio < 1:
  return math.pow(ratio, 10)
else:
  return 0.89976*math.pow(ratio, 7.7095)+0.111
