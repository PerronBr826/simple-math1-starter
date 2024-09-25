# Bryce Perron
# 9/25/2024
# Practice 1

num1 = 6.2
num2 = 10

sum = num1 + num2
difference = num2 - num1
product = num1 * num2
quotient = num2/num1
remainder = num2%num1

print(f"Sum: {sum}, Difference: {difference}, Product: {product},\nQuotient: {quotient:.2f}, Remainder: {remainder}.")

# Practice 2

rect_length = float(input("Input your rectangle's width in feet: "))
rect_height = float(input("Input your rectangle's height in feet: "))

rect_area = rect_height * rect_length

print(f"The area of your room is {rect_area:.2f} square feet.")

# Practice 3

# Part 1

name = "Bryce".title()
age = 16
fav_color = "Blue".title()

message = "My name is {0} and I am {1} years old. {2} is my favorite color.".format(name,age,fav_color)

print(message)

# Part 2

SALES_TAX = 0.06

item1_price = 19.99
item2_price = 9.99
item3_price = 14.99

total = item1_price + item2_price + item3_price
grand_total = total + total * SALES_TAX

txt = "Your total will be ${tl:.2f}. With the state sales tax of 6% your grand total will be ${gt:.2f}"
print(txt.format(tl = total, gt = grand_total))

# Part 3

friend_name = "joe".title()
friend_school = "evil school".title()

print("My friend {0} goes to {1}.".format(friend_name,friend_school))