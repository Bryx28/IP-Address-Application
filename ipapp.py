import requests
from flask import Flask
from flask import request
from flask import render_template

ip_app = Flask(__name__)

@ip_app.route("/")
def main():
    return render_template("index.html")

@ip_app.route("/own_ip")
def self_ip():
    home_device = Own_IP_Address()
    
    #IP Address
    ip_info = home_device.get_ip()
    ip_add = ip_info[0]
    ip_ver = ip_info[1]

    #Location
    location_ip = home_device.get_geological_info()
    c_code = location_ip[0]
    country = location_ip[1]
    region = location_ip[2]
    lat = location_ip[3]
    long = location_ip[4]
        
    #ISP and ASN
    isp_info = home_device.get_isp_info()
    isp = isp_info[0]
    asn = isp_info[1]
    return render_template("own_ip.html",
                                 ip_add = ip_add,
                                 ip_ver = ip_ver,
                                 c_code = c_code,
                                 country = country,
                                 region = region,
                                 lat = lat,
                                 long = long,
                                 isp = isp,
                                 asn = asn)

@ip_app.route("/specific_ip")
def specific_ip():
    return render_template("specific.html")

@ip_app.route("/specific_output", methods=['GET'])
def specific_output():
    ip_add = request.args['ip_add']
    
    #If input is blank, return  loopback  address.
    if ip_add == "":
        ip_add = "127.0.0.1"

    #Initialize the Search Object
    target_device = Search_IP_Address(ip_add)
    
    #Check if the  Public IP Address is okay or invalid.
    if target_device.confirmation == "Undefined" or target_device.confirmation == "None":
        return render_template("invalid_ip.html")
    else:
        #IP Address
        ip_info = target_device.get_ip()
        ip_address = ip_info[0]
        ip_ver = ip_info[1]

        #Location 
        location_ip = target_device.get_geological_info()
        c_code = location_ip[0]
        country = location_ip[1]
        region = location_ip[2]
        lat = location_ip[3]
        long = location_ip[4]
        
        #ISP and ASN
        isp_info = target_device.get_isp_info()
        isp = isp_info[0]
        asn = isp_info[1]
        return render_template("specific_output.html",
                                        ip_add = ip_address,
                                        ip_ver = ip_ver,
                                        c_code = c_code,
                                        country = country,
                                        region = region,
                                        lat = lat,
                                        long = long,
                                        isp = isp,
                                        asn = asn)

#Class for Getting the IP Address Information of the User
class Own_IP_Address:

    #Initialization of API to get Public IP Address of the User
    def __init__(self):
        self.main_url = 'https://ipapi.co/json/'
        self.loc = requests.get(self.main_url)
        self.ip_info = self.loc.json()

    #Get the Public IP Address of the User
    def get_ip(self):

        #Getting the IP Address and it's version
        self.public_ip = self.ip_info['ip']
        self.public_ip_type = self.ip_info['version']

        #Display of IP Address Information
        return (self.public_ip, self.public_ip_type)

    #Get the Geological Location of the User
    def get_geological_info(self):

        #Getting the Information of the Location
        self.ip_loc_country_code = self.ip_info['country_code']
        self.ip_loc_country = self.ip_info['country_name']
        self.ip_loc_region = self.ip_info['region']
        self.ip_loc_latitute = self.ip_info['latitude']
        self.ip_loc_longitude = self.ip_info['longitude']

        return (self.ip_loc_country_code,
                self.ip_loc_country,
                self.ip_loc_region,
                self.ip_loc_latitute,
                self.ip_loc_longitude)
    
    #Getting the ISP and ASN of the User IP Address
    def get_isp_info(self):
        #Getting the ISP and ASN
        self.ip_isp = self.ip_info['org']
        self.ip_asn = self.ip_info['asn']

        return (self.ip_isp, self.ip_asn)

class Search_IP_Address:

    #Initialization of API to get Public IP Address of the User
    def __init__(self, ip_add):
        self.main_url = f'https://ipapi.co/{ip_add}/json/'
        self.confirmation = requests.get(f'https://ipapi.co/{ip_add}/latitude/').text
        self.loc = requests.get(self.main_url)
        self.ip_info = self.loc.json()

    #Get the Public IP Address of the User
    def get_ip(self):

        #Getting the IP Address and it's version
        self.public_ip = self.ip_info['ip']
        self.public_ip_type = self.ip_info['version']

        #Display of IP Address Information
        return (self.public_ip, self.public_ip_type)
    
    #Get the Geological Location of a Specific User
    def get_geological_info(self):

        #Getting the Information of the Location
        self.ip_loc_country_code = self.ip_info['country_code']
        self.ip_loc_country = self.ip_info['country_name']
        self.ip_loc_region = self.ip_info['region']
        self.ip_loc_latitute = self.ip_info['latitude']
        self.ip_loc_longitude = self.ip_info['longitude']

        return (self.ip_loc_country_code,
                self.ip_loc_country,
                self.ip_loc_region,
                self.ip_loc_latitute,
                self.ip_loc_longitude)
    
    #Getting the ISP and ASN of a Specific User IP Address
    def get_isp_info(self):
        #Getting the ISP and ASN
        self.ip_isp = self.ip_info['org']
        self.ip_asn = self.ip_info['asn']

        return (self.ip_isp, self.ip_asn)

if __name__ == "__main__":
    ip_app.run(host="0.0.0.0", port=8080)