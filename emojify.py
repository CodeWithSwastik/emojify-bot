from PIL import Image

# Real colors don't work as well I guess
# COLORS = {
#     (49, 55, 61):    "⬛",
#     (85, 172, 238):  "🟦",
#     (221, 46, 68):   "🟥",
#     (253, 203, 88):  "🟨",
#     (193, 105, 79):  "🟫",
#     (244, 144, 12):  "🟧",
#     (170, 142, 214): "🟪",
#     (230, 231, 232): "⬜",
#     (120, 177, 89):  "🟩",
# }

# These colors work a bit better maybe
COLORS = {
    (0, 0, 0): "⬛",
    (0, 0, 255): "🟦",
    (255, 0, 0): "🟥",
    (255, 255, 0): "🟨",
    # (190, 100, 80):  "🟫",
    (255, 165, 0): "🟧",
    # (160, 140, 210): "🟪",
    (255, 255, 255): "⬜",
    (0, 255, 0): "🟩",
}


def distance(c1, c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    d = ((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2) ** 0.5

    return d


def find_closest_emoji(color):
    c = sorted(list(COLORS), key=lambda k: distance(color, k))
    return COLORS[c[0]]


def emojify_image(img, size=14):

    WIDTH, HEIGHT = (size, size)
    small_img = img.resize((WIDTH, HEIGHT), Image.BILINEAR)

    emoji = ""
    small_img = small_img.load()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            emoji += find_closest_emoji(small_img[x, y])
        emoji += "\n"
    return emoji
