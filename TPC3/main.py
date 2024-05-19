from sys import stdin

adding = 0
added = 0
for line in stdin:
  for word in line.split():    
    if word.lower() == 'on':
        adding = 1
    if word.lower() == 'off':
        adding = 0
    if word.lower()== '=':
        print(added)
    try:
        added += adding*int(word)
    except: pass
regex = r"on.*?([-+]?\d+?).*?off"
