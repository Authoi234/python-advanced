import requests, os, webbrowser as wb

url = input("Please enter url ", ) or "https://www.jhankarmahbub.com/"
name = input("Please enter file name (with .html) ", ) or "jhankar-mahbub-clone.html"

response = requests.get(url)

with open(name, "w", encoding=response.encoding) as f:
    f.write(response.text)

file_path = os.path.realpath(name)
print(file_path)
wb.open("file://"+file_path)