import requests
import os
import webbrowser as wb

url = "https://www.jhankarmahbub.com/"

response = requests.get(url)

with open("jhankar-mahbub-clone.html", "w", encoding=response.encoding) as f:
    f.write(response.text)

file_path = os.path.realpath("jhankar-mahbub-clone.html")
print(file_path)
wb.open("file://"+file_path)