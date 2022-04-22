import requests
from bs4 import BeautifulSoup




def ekstraksi_data():
    """
    Tanggal :15 Februari 2022,
    Waktu : 16:51:43 WIB
    magnitudo : 3.4
    kedalaman : 10 km
    lokasi  :{LS = 0.72 LS , BT=  131.51 BT}
    Keterangan : Pusat gempa berada di laut 29 km Timur Laut Kota Sorong
    Dirasakan (Skala MMI): II Kota Sorong
    return :
    """
    try:
        content= requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None
    if content.status_code == 200:
        print(content.status_code)
    #soup = BeautifulSoup(content)
    #print(soup.prettify())

        hasil = dict()
        hasil['tanggal'] = '15 Februari 2022'
        hasil['waktu']  = '16:51:43 WIB'
        hasil['magnitudo'] = 3.4
        hasil['kedalaman'] =  10
        hasil['lokasi'] = {'LS' : 0.72  , 'BT':  131.51 }
        hasil['keterangan'] = 'Pusat gempa berada di laut 29 km Timur Laut Kota Sorong'
        hasil['dirasakan']  = 'Dirasakan (Skala MMI): II Kota Sorong'
        return hasil
    else:
        return  None

def tampilkan_data(result):

    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return
    print('Gempa berdasarkan BMKG')
    print(f'tanggal {result["tanggal"]}')
    print(f'magnitudo {result["magnitudo"]}')
    print(f'kedalaman {result["kedalaman"]}')
    print(f'lokasi {result["lokasi"]}')
    print(f'keterangan {result["keterangan"]}')
    print(f'dirasakan {result["dirasakan"]}')

#if __name__ == '__main__':
    #print('ini adalah package gempa terkini')