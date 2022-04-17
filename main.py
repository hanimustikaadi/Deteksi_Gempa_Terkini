"""
aplikasi deteksi gempa terkini
modularisasii  dengan function
"""
from gempa_terkini import ekstraksi_data, tampilkan_data

if __name__ == '__main__':
    print('aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)