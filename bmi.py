height = input("Enter your height(Example: if you're 5'5'' enter 5 5): ")
weight = input("Enter your weight in lbs: ")

def converter(height_convert):
    height = height_convert[0]
    inch_index_1 = int(height) * 12

    if len(height_convert) > 1:
        inch_index_2 = height_convert[2:]
        total = int(inch_index_1 + int(inch_index_2))
    else:
        total = int(inch_index_1)

    return total

h = converter(height) * .0254
w = round(int(weight) / 2.205, 2)

bmi = w / h ** 2 
bmir = round(bmi, 2)
print(f"Your BMI is {bmir}.")

if bmi < 18.5:
    print("You are underweight.")
elif bmi > 18.5 and bmi < 25:
    print("You are the proper weight.")
elif bmi > 25 and bmi < 30:
    print("You're overweight.")
elif bmi > 30:
    print("You're obese.")


