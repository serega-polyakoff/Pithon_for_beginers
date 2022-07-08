word = input()
symbol = input()
is_found = False
for w in word:
    if w == symbol:
        is_found = True
        break

if is_found:
    print(f"The '{symbol}' character was found in '{word}'.")
else:
    print(f"The '{symbol}' character was not found in '{word}'.")