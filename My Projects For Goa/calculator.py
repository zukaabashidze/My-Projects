num1 = int(input("Enter your first number: "))
nishani = input("Enter + - / * ......")
num2 = int(input("Enter your second number: "))

if nishani == "+":

   საბოლოოდ = num1 + num2

elif nishani == "-":



    საბოლოოდ = num1 - num2

elif nishani == "":

    საბოლოოდ = num1 num2

elif nishani == "/":

    if num2 == 0:

        საბოლოოდ = "ნულზე არ იყოფა არაფერი"
    else:

        საბოლოოდ = num1 / num2



print(საბოლოოდ)