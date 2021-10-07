tem = input("Enter the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(tem[:-1])
i_conv = tem[-1]

if i_conv.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_conv.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")
