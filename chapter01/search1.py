#!/home/aaron/geo_env python3
#Foundations of Python Network Programming, Third Edition
#https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search1.py

from pygeocoder import Geocoder


if __name__ == '__main__':
	adress = '207 N. Defiance St, Archbold, OH'
	print(Geocoder.geocode(adress)[0].coordinates)

