import requests
import sys

base_url = input("Please enter url: ", ) or "https://bugs.python.org/file47781/Tutorial_EDIT.pdf"
name = input("Please enter name of the book (just file name, not .pdf or anything): ", ) or "downloaded_book"

response = requests.get(base_url)

if response.ok is False:
    sys.exit("Error downloading the file")

with open(f"{name}.pdf", "wb") as fp:
    fp.write(response.content)

print("Book downloaded successfully as downloaded_book.pdf")