import requests
import sys

base_url = input("Please enter url: ", ) or "https://bugs.python.org/file47781/Tutorial_EDIT.pdf"

response = requests.get(base_url)

if response.ok is False:
    sys.exit("Error downloading the file")

with open("cpbook.pdf", "wb") as fp:
    fp.write(response.content)

print("Book downloaded successfully as cpbook.pdf")