text = input()
letters = 0
digits = 0
spaces = 0
marks = 0

for symbol in text:
    if symbol.isalpha():
        letters += 1
    elif symbol.isdigit():
        digits += 1
    elif symbol == " ":
        spaces += 1
    elif symbol in ",.:!'":
        marks += 1

print(f"The text '{text}' contains {letters} letter(s), {digits} number(s), "
      f" {spaces} spaces and {marks} marks.")