import json, requests, subprocess, os 

#Enter your local directory for your api program
localPath = r'C:\Users\thinh'

#Open api process in the local directory
api = subprocess.Popen(['node', fr'{localPath}\it3038c-scripts\node\api.js'])

#Connect to localhost
r = requests.get('http://localhost:3000')
data = r.json()

#Print data
for num in range(0,4):
    print(data[num]['name'] + " is " + data[num]['color'] + ".")

#Close API
api.terminate()
