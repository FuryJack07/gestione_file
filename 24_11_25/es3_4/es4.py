import json

with open("goal.json","r") as f:
    aa = json.load(f)
    # aa -> dizionario

print(aa)