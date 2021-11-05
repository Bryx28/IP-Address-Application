from requests import get

main_url = 'https://ipapi.co/'
ip_add = input("Enter your public ip address: ")
url = main_url + ip_add + "/latitude/"
lat = get(url).text

print(lat)