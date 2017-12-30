formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        "Wish you were here",
        "Coming back to life",
        "High Hopes",
        "Shine on your crazy diamond", 
        "Take it back"
                             ))