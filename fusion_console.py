import sys

print("initializing....")

words = [
    "blast pumpkin",
    "laser pumpkin",
    "vortex melon",
    "doominator-shroom",
    "oblivion-shroom",
    "obsidian tall-nut",
    "giant chomper",
    "gatling pea turret",
    "armor pumpkin"
]

print("done initializing! please note that an extra letter will not work with this.")

search_for = input("what are you looking for?\n").lower().strip()

match = None

for word in words:
    if search_for == word:
        match = word
        break

if match:
    print("match!")
else:
    print(
        "did not find your searched word....\n"
        "tip:\n"
        "make sure you are not putting extra words. "
        "dont put stuff like '-' or '?'. "
        "also make sure its an odyssey plant."
    )
    sys.exit()

# Notepad++ line numbers
guides = {
    "armor pumpkin": (7, 36),
    "gatling pea turret": (40, 55),
    "giant chomper": (59, 61),
    "obsidian tall-nut": (64, 84),
    "oblivion-shroom": (88, 114),
    "doominator-shroom": (118, 144),
    "vortex melon": (149, 176),
    "laser pumpkin": (179, 207),
    "blast pumpkin": (214, 216)
}

with open("the guide.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

srt, end = guides[match]

# Convert Notepad++ line numbers to Python indexes
srt -= 1
end -= 1

print("\n=============================")
print(match.upper())
print("=============================\n")

for i in range(srt, end + 1):
    print(lines[i], end="")