import math

# coffee
spring = {
    "bluejazz" : 4,
    "clauliflower" : 2,
    "garlic" : 9,
    "parsnip" : 9,
    "potato" : 5,
    "tulip" : 5,
    "kale" : 5,
    "greenbean" : 7,
    "rhubarb" : 2,
    "strawberry" : 6,
    "coffeebean" : 40
}

# coffee, corn , sunflower, wheat
summer = {
    "blueberry" : 15,
    "hops" : 19,
    "hotpepper" : 8,
    "melon" : 2,
    "poppy" : 4,
    "radish" : 5,
    "redcabbage" : 3,
    "starfruit" : 2,
    "summerspangle" : 3,
    "tomato" : 5,
    "coffeebean" : 14,
    "corn" : 4,
    "sunflower" : 3,
    "wheat" : 9
}

# corn, sunflower, wheat
fall = {
    "corn" : 7,
    "sunflower" : 4,
    "wheat" : 9,
    "amaranth" : 4,
    "artichoke" : 3,
    "beet" : 5,
    "bokchoy" : 9,
    "cranberries" : 10,
    "eggplant" : 5, 
    "fairyrose" : 2,
    "grape" : 7,
    "pumpkin" : 2,
    "sweetgemberry" : 1,
    "yam" : 3
}

tiles = int(input("Number of tiles? "))
season = input("Season? ").lower().strip()

if season == "spring":
    season = spring
    printseason = "SPRING"
elif season == "summer":
    season = summer
    printseason = "SUMMER"
else:
    season = fall
    printseason = "FALL"

# calculate total tiles

max = ("default",0)
min_tiles = dict()
for crop, yield_per_tile in season.items():
    min_tiles[crop] = 0
    if yield_per_tile > max[1]:
        max = (crop, yield_per_tile)

max_yield_crop = max[0]
min_yield = max[1]

min_tiles[max_yield_crop] = 1

for crop, yield_per_tile in season.items():
    if crop != max_yield_crop:
        min_tiles[crop] = math.floor(min_yield / yield_per_tile)


sum_tiles = sum(min_tiles.values())

times = math.floor(tiles / sum_tiles)

total_tiles_per_crop = dict()
for crop, yield_per_tile in season.items():
    total_tiles_per_crop[crop] = min_tiles[crop] * times

total_yield_per_crop = dict()
for crop, yield_per_tile in season.items():
    total_yield_per_crop[crop] = total_tiles_per_crop[crop] * yield_per_tile

total_yield = sum(total_yield_per_crop.values())

total_tiles = sum(total_tiles_per_crop.values())

rest = tiles - total_tiles

num_crops = len(season.keys())

extra = math.floor(rest / num_crops)
for crop in total_tiles_per_crop.keys():
    total_tiles_per_crop[crop] += extra

total_tiles = sum(total_tiles_per_crop.values())
rest = tiles - total_tiles

print(printseason, "\n", "-"*10)
print(" "*5, "CROP", " "*3, "TILES")
for crop, qt in season.items():
    length = 12 - len(crop)
    print(" "*length, crop," ", total_tiles_per_crop[crop])

print("-"*10, "\n" + "TOTAL YIELD", " "*3, total_yield, "\n" + "-"*10)
print("TOTAL TILES", " "*3, total_tiles, "(" + str(rest) + " left)", "\n" + "-"*10)