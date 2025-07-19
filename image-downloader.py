import requests

img_url = "https://www.autodesk.com/blogs/autocad/wp-content/uploads/sites/35/2020/08/How-to-create-a-block-in-AutoCAD-1536x830-1-scaled.jpg"

r = requests.get(img_url)

with open("downloaded-image.jpg", "wb") as f:
    f.write(r.content)
