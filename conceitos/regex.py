import re

names = [
    'Brian Daugette',
    'Veronica Supersonica',
    'Tony Gasparovic',
    'Patrick Germann',
    'm!sha']

regex = '[a-z]+'
for name in names:
    matches = re.findall(regex, name)
    if matches:
        print(matches)
