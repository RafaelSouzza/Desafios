palavra = str(input("Digite uma palavra: "))
palavraInvertida = ""
index = int(len(palavra)) - 1 
while (index >= 0):
    palavraInvertida += palavra[index]
    index -= 1
    
print("Se invertermos {} ficará {}".format(palavra, palavraInvertida))