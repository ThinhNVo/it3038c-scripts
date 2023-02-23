import subprocess, os, sys
import xml.etree.ElementTree as ET

# Asking users to name the file with password 
print('Name the file and I will create it with your saved password inside!')
name = str(input()) + ".txt"

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
        print('SSID: %s is an open network or have use one x as true ' % i)
        os.remove(i)

# save output to password.txt by creating a new one or replacing the old one and write output to terminal
if name in os.listdir(place):
    r = open(name, "w")
    r.write('')
for x, y in zip(wifi_name, wifi_password):
    f = open(name, "a")
    f.write('SSID: %s Password: %s \n' % (x, y))
