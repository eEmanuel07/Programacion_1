palab_o_frase = input("Ingrese un apalabra o frase: ").lower()

ultima_letra = palab_o_frase [-1]

if ultima_letra == "a" or  ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u" :
    print (f"{palab_o_frase}!")

else:
    print (f"{palab_o_frase}")