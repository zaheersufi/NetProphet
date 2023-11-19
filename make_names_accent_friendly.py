# take name such as "Peja Stojakovi\u0107" and convert to "Peja Stojaković"

def convert_name(name):
    while "\\" in name:
        index = name.index("\\")
        hexadecimal = name[index + 2:index + 6]
        char = int(hexadecimal, 16)
        name = name[:index] + chr(char) + name[index + 6:]
    return name


print(convert_name("Peja Stojakovi\\u0107"))
