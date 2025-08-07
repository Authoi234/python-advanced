# import re

# s = "Saudi Arabia, Iran, Iraq, Palestine, Yemen, Russia, China, Greenland, Pakistan, Bangladesh, United Arab Amirates, United States of America, United Kingdom, Afganistan, Turkmenistan, Kazakhstan ,Kyrgyzstan, Mongolia , Tajikistan, Uzbekistan, Turkey, France, Iceland, Swizerland, Sweden, Thailand, New Zealand, Netherlands,Finland, Ireland, Poland, Wakanda"

# contries = s.split(",")
# li = [item for item in contries if item.endswith("land") or item.endswith("lands")]
#print(li)

# liv2=re.findall(r'(\w+lands*)', s)
#print(liv2)

#match = re.search("Bangla", "Bangladesh")
#print(match.group())

# s="Bangladesh is our homeland"
#match = re.search("B.+?h", s)
#match = re.search("B.\w+h", s)
#print(match.group())

# text = "multiiple phone numbers, 01734567434, 01634567434, 01934567434, 00000000000, 01919191910, 01212121212, 123-123"
# result = re.findall(r'01[56789]\s*\d{8}', text)
# print(result)

# s="Bangla, English, Bangla"
# print(re.findall(r'bangla$', s, re.IGNORECASE))

# with open("file.txt", "r") as f:
#     text=f.read()

# print(text)

# print(re.findall(r'^.*?$', text, re.MULTILINE))

# s = "<li>Tamim</li><li>Sakib</li><li>Mahmudullah</li><li>Mominul</li>"
# result = re.findall(r'<li>(.*?)</li>', s)
# print(result)

# text = "This is line 1. Date is 2025/07/28 . And there is another date : 2025-07-28 . The third and the final date is 2025.07.30 ."

# pat = re.compile(r'(\d{4})[-/.](\d{1,2})[-/.](\d{1,2})')
# result = pat.findall(text)
# print(result)
