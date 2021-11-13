import requests

#Class for Getting the IP Address Information of a Specific User
class Search_IP_Address:

    #Initialization of API to get Public IP Address of the User
    def __init__(self, ip_add):
        self.main_url = f'https://ipapi.co/{ip_add}/json/'
        self.confirmation = requests.get(f'https://ipapi.co/{ip_add}/latitude/').text
        self.loc = requests.get(self.main_url)
        self.ip_info = self.loc.json()

    #Get the Geological Location of a Specific User
    def get_geological_info(self):

        #Getting the Information of the Location
        self.ip_loc_country_code = self.ip_info['country_code']
        self.ip_loc_country = self.ip_info['country_name']
        self.ip_loc_region = self.ip_info['region']
        self.ip_loc_latitute = self.ip_info['latitude']
        self.ip_loc_longitude = self.ip_info['longitude']

        #Display of a Specific User Location based on IP Address
        print("*------------------ User Location -------------------*")
        print(f"Country Code: {self.ip_loc_country_code}")
        print(f"Country Name: {self.ip_loc_country}")
        print(f"Region: {self.ip_loc_region}")
        print(f"Latitude: {self.ip_loc_latitute}")
        print(f"Longitude: {self.ip_loc_longitude}")
        print("*----------------------------------------------------*")
    
    #Getting the ISP and ASN of a Specific User IP Address
    def get_isp_info(self):
        #Getting the ISP and ASN
        self.ip_isp = self.ip_info['org']
        self.ip_asn = self.ip_info['asn']

        #Display of ISP and ASN of User
        print("*--------------- User ISP Information ---------------*")
        print(f"Internet Service Provider: {self.ip_isp}")
        print(f"Autonomous System Number: {self.ip_asn}")
        print("*----------------------------------------------------*")