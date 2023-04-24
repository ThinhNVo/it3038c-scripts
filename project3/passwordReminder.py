import subprocess, os, sys
import xml.etree.ElementTree as ET


# Creating xml files with saved password through windows command execution
command = subprocess.run(["netsh", "wlan", "export", "profile",
                         "key=clear"], capture_output=True).stdout.decode()

# Creating a list for Wifi file, Wifi name, and Wifi password
files = []
wifi_name = []
wifi_password = []

# Getting current directory
place = os.getcwd()

# Collecting wifi xml files from the directory
for filename in os.listdir(place):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        files.append(filename)

# Parsing Wifi xml, adding them to wifipassword list, and delete traces
for i in files:
    tree = ET.parse(i)
    root = tree.getroot()
    SSID = root[0].text

# Separating open authentication network from WPA2PSK
    if root[4][0][0][0].text != "open" and root[4][0][0][2].text != "true":
        password = root[4][0][1][2].text
        wifi_name.append(SSID)
        wifi_password.append(password)
        os.remove(i)
    else:
        os.remove(i)

# Asking users to enter the number to see the password 
count = 0
for name in wifi_name:
    print(str(count) + "." + name + " ")
    count += 1
print("Enter a number from this wifi list to see the password: ")
number = input()

# Asking users to re-enter the number to see the password 
while not number.isdigit() or int(number) < 0 or int(number) > count:
    if not number.isdigit():
        print("Please enter a number: ")
    elif int(number) < 0 or int(number) > count:
        print("Please enter a number in this list")
    number = input()

# Showing the password
print("The password is: " + str(wifi_password[int(number)]))



    
