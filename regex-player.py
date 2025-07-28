import re

with open("cricketers.html", "r") as file:
    html = file.read()

pattern = re.compile(
    r"<li>\s*(.*?)\s*<ol>\s*<li>(.*?)</li>\s*<li>(.*?)</li>\s*</ol>\s*</li>",
    re.IGNORECASE
)

matches = pattern.findall(html)

for country, player1, player2 in matches:
    print(f"{country.strip().capitalize()} - {player1.strip().title()}, {player2.strip().title()}")