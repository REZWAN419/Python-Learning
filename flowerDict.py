flowers = [
    {"name" : "Lily", "frag_stat" : "Non fragrance", "color" : "Yellow"},
    {"name" : "Rose", "frag_stat" : "Fragrance", "color" : "Red"},
    {"name" : "Gardenia", "frag_stat" : "Fragrance", "color" : "White"},
    {"name" : "Baily", "frag_stat" : "Fragrance", "color" : "White"},
    {"name" : "Night Qeen", "frag_stat" : "Fragrance", "color" : None}
    ]

for flr in (flowers):
    print(flr["name"], flr["color"], flr["frag_stat"],sep=" , ")
