import requests
import json


def solve():
    r1 = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=10.8063192,106.6935294&radius=2000&type=restaurant&key=AIzaSyAc1hZ0RXEimEUUVUCH8HqYb8DKh7rWsdc', timeout=5)
    f1 = json.loads(r1.text)
    a = None
    k1 = []
    for i in f1['results']:
        a = [('type','Feature'),
              ('geometry',dict([('type', 'Point'), ('coordinates', [i['geometry']['location']['lng'], i['geometry']['location']['lat']])])),
              ('properties', dict([('Address', i['vicinity']),('name', i['name'])]))
              ]
        k1.append(a)
    r2 = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken=ATtYBwLonb9kCBr6GBWHeAZ05Zroo-miHj3qycuiG_ZL59BtUAFV-eOcFX_KBStdlqoHLZj0Sy8Vb6IbRiAg4HXgTAWMD6awXALCp6HkS72BjemhR-PFSEU8-ZUKMZaIAl2WPkVQJ5FkIyLO73WWRvVaPGpIdQRvgq4u4Wtn7fmL4FU2zezpNh4u7pbjG53mHCCMRUbHfW8K-0sfZLY5mDKXHNRsSrJd4rtpPTop3ofyrKSFvFEw_oiPmd4NMywCNsbB4XzaFBeWQH1Uv3ZqYXEC3ruTFjyGMxCDIQWxCHloUDl4-kOByuJhsYmTn4acsEn7Wfu86757MJr214FA2KFbdJSKhww8RvMgjcOHtsXPDEwEhlRPI05idQ1nExLLsJKScN8K3iQPIOjL57-K0p0eGnhpBYHhPft_nGjOIG39I-VOOyMis-rqQVY7Xb3l&key=AIzaSyAc1hZ0RXEimEUUVUCH8HqYb8DKh7rWsdc', timeout=5)
    f2 = json.loads(r2.text)
    b = None
    k2 = []
    for i2 in f2['results']:
        b = [('type','Feature'),
             ('geometry',dict([('type', 'Point'), ('coordinates', [i2['geometry']['location']['lng'], i2['geometry']['location']['lat']])])),
             ('properties', dict([('Address', i2['vicinity']), ('name', i2['name'])]))
             ]
        k2.append(b) 
    r3 = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken=ATtYBwItrGSCFv6_towNdWehRftbSxVOceFh5e5YWHG8oFhDK7QQNc2gBBMu0hWIC6ZcIurRehKS7VLyE4SZNIBzLXpAbFukzzh7nVwmBi0ywxCr_c-bUWfpUyWL6u57YNUKZ49vo9TDuZCQXIFHzrpwtpAxdpkBxd75e-1TG6c4_7AWJNTa7o1AtHUzpjX2Z1TIafsvLjG2koH9dF5mEP5Zf1ehrLAi_gcGMLo2g4r0GkMKOzIWmWEVvNBJXf8b7kVoxyYbYIh1oMq1bVPpYo-jVEui__ywEp183wVD0SrU6pGgczVTd3HnkES6CCBLg1FUz_nofrbYkxz_vAZJOlgowmsQ1Sa5ddsek0TP6TZ59AiQtFl1SK-a3y-QrK1P6b45NFc8D0yAdaf45rHKenD18bPe0IZwYkTsbA1DYIU138lQ5kXMcBk3aOyrduItu-Aec0ovUYj3H3wcrXUvJDH3ZMR2iFr0fJO_eUflqCPzubYSldiXmV6-V6d-H-IhMcCRxJQe0oawtnxcCtGuDL5xKyElNuHZOp4ynPj1vF6K2lrl9opkg46P7gA1A48M6JtWVaS3qo5Cwj01z7WuNHDOvHIwNWp_AAQ1iOd8XI22tsGwajAVdhE9DYB_NruGK7uZ9Z8_FwKjJGFxf-RDFg&key=AIzaSyAc1hZ0RXEimEUUVUCH8HqYb8DKh7rWsdc', timeout=5)
    f3 = json.loads(r3.text)
    c = None
    k3 = []
    for i3 in f3['results']:
        c = [('type','Feature'),
             ('geometry',dict([('type', 'Point'),('coordinates', [i3['geometry']['location']['lng'], i3['geometry']['location']['lat']])])),
             ('properties', dict([('Address', i3['vicinity']), ('name', i3['name'])]))
             ]
        k3.append(c)
    k = k1 + k2 + k3
    h = k[:50]
    li = []
    for j in h:
        li.append(dict(j))
    res = {'type':'FeatureCollection', 'features': li}
    s = json.dumps(res, indent=4)
    f0 = open('pymi_res8.geojson', 'wt')
    f0.write(s)
    f0.close()


def main():
    solve()


if __name__ == "__main__":
    main()
