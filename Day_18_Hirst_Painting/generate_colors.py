import colorgram

colors = colorgram.extract('image.jpeg', 6)

list_of_colors = []
for color in colors:
    rgb = color.rgb.r,color.rgb.g,color.rgb.b
    list_of_colors.append(rgb)

print(list_of_colors)

list_of_colors = [(235, 233, 229), (231, 168, 65), (51, 110, 156), (247, 226, 238), (235, 239, 246), (210, 124, 163), (0, 255, 0), (138, 43, 226), (255, 255, 0), (255, 20, 147)]
