import requests
import sys

img_url = sys.argv[1]
file_name = sys.argv[2]
r = requests.get(img_url).content

with open(file_name, "wb") as f:
    f.write(r)
print(f"Image downloaded and saved as {file_name}")