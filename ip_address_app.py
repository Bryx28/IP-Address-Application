from ip_add_json import Own_IP_Address

while True:
    #Main Menu of the Application
    print(">>>>>>>>>>>>>> IP Address Application <<<<<<<<<<<<<<")
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
        #Exit the application
        print("Thank You for using the Application!")
        break
    else:
        print("Invalid Option!")
    print("\n\n\n")