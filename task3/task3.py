community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]
result_list = []

for member in community_members:
    if "a" in member:
        result_list.append(member)

print('Number of members with the letter a:', len(result_list))
