num1  = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número:\n"))
operation = input("Digite a operação a ser realizada: (+ - * /)\n")

if operation == "+":
  result = num1 + num2
elif operation == "-":
  result = num1 - num2
elif operation == "*":
  result = num1 * num2
elif operation == "/":
  if num2 != 0:
    result =  num1 / num2
  else:
    print("Erro: Divisão por Zero")
    result = 0
else:
  print("Operação inválida")

print(f"REsultado da operação é {result:.2f}")

