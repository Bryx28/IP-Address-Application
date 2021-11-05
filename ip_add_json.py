from requests import get

loc = get('https://ipapi.co/json/')
ip_info = loc.json()

ip_add = ip_info['ip']
ip_loc = ip_info['country_name']
ip_lat = ip_info['latitude']
ip_long = ip_info['longitude']
ip_region = ip_info['region']
ip_asn = ip_info['asn']
ip_cc = ip_info['country_code']

print(ip_add)
print(ip_region)
print(ip_lat)
print(ip_long)
print(ip_loc)
print(ip_cc)
print(ip_asn)