try:
    a = int(input("Digite "))
    b = int(input("Valor "))
    r = a / b

except (ValueError, TypeError):
    print(f"Tivemos um problema com os tipos de dados que você digitou")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados")
except Exception as erro:
    print(f"Problema encontrado foi {erro.__class__}")
else:
    print(r)  # Zero division error
finally:
    print("Volte sempre, muito obrigado!")

#  TypeError; ValueError; NameError; KeyError; NotFound -> Excessões
