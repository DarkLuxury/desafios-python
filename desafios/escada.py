print("Qual o material quer você quer construir a sua escada?")
material = input("")
print("Quantos degraus você quer na sua escada?")
degraus = int(input())
i=0
mat = material

while i < degraus:
    i = i+1
    print(material)
    material = mat + material