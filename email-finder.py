import re

text="To ask about books, please email at, book at sovietbooks [dot] com . Please email here for any support, support (at) sovietbooks dot com . For any problem plase email at, help.support@sovietbooks.com"

text = re.sub(r'\s+[\(\[]*\s*at\s*[\)\]]*\s+', "@", text, flags=re.I)

text = re.sub(r'\s*[\(\[]*\s*dot\s*[\)\]]*\s*', ".", text, flags=re.I)

print(text)