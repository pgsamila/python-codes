# An array of color names.
colors = ["blue", "lavender", "red", "yellow"]

# Sort colors by length, in reverse (descending) order.
for color in sorted(colors, key=lambda color: len(color), reverse=True):
    print(color)
