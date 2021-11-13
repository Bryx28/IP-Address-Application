from ip_add_json import Own_IP_Address
from ip_add_json2 import Search_IP_Address

def own_ip():
    while True:
        #Main Menu of the Application
        print(">>>>>>>>>>>>>> IP Address Application <<<<<<<<<<<<<<")
        print("-------------- Self Public IP Address --------------")
        home_device = Own_IP_Address()
        print("1 - IP Address Information")
        print("2 - Geological Information")
        print("3 - ISP Information")
        print("4 - Quit")
        choice = input("Enter your option: ")
        print("----------------------------------------------------")

        #Choices of the application
        if choice == "1":
            home_device.get_ip()    #User IP address info
        elif choice == "2":
            home_device.get_geological_info()   #User IP address location
        elif choice == "3":
            home_device.get_isp_info()      #User ISP and ASN
        elif choice == "4":
            #Main Menu
            break
        else:
            print("Invalid Option!")
        print("\n\n")

def specific_ip():
    while True:
        #Main Menu of the Application
        print(">>>>>>>>>>>>>> IP Address Application <<<<<<<<<<<<<<")
        print("-------------- Find Public IP Address --------------")
        ip_add = input("Enter Public IP Address: ")
        target_device = Search_IP_Address(ip_add)
        if ip_add == "q" or ip_add == "quit":
            break
        if target_device.confirmation == "Undefined" or target_device.confirmation == "None":
            print("Invalid Public IP Address! Try Again!")
            print("\n\n")
        
        else:
            while True:
                print("----------------------------------------------------")
                print("1 - Geological Information")
                print("2 - ISP Information")
                print("3 - Quit")
                choice = input("Enter your option: ")
                print("----------------------------------------------------")

                #Choices of the application
                if choice == "1":
                    target_device.get_geological_info()   #User IP address location
                elif choice == "2":
                    target_device.get_isp_info()      #User ISP and ASN
                elif choice == "3":
                    #Main Menu
                    break
                else:
                    print("Invalid Option!")
                print("\n\n")

def main_menu():
    while True:
        #Main Menu of the Application
        print(">>>>>>>>>>>>>> IP Address Application <<<<<<<<<<<<<<")
        print("1 - Self Public IP Address")
        print("2 - Find Public IP Address")
        print("3 - Quit")
        choice = input("Enter your option: ")
        print("----------------------------------------------------")

        #Choices of the application
        if choice == "1":
            own_ip()   #User Public IP address info
        elif choice == "2":
            specific_ip()  #Specific Public IP address info
        elif choice == "3":
            #Main Menu
            print("Thank you for using the Application!")
            break
        else:
            print("Invalid Option!")
        print("\n\n")

if __name__ == "__main__":
    main_menu()