n = int(input())

for i in range(n):
    num = float(input())

    # float or int
    if int(num) == num:
        num_type = "integer"

    # positive or negative
    num_sign = "positive"
    if num < 0:
        num_sign = "negative"
    info = f"{num_type}, {num_sign}"

    if num_type == "integer":
        even_odd = "odd"
        if num % 2 == 2:
            even_odd = "even"
    info = f"{info}, {even_odd}"

print(f"The value {num} is {info}.")