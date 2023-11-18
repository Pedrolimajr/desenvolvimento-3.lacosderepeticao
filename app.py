#Escreva um código que imprima todos os números exceto o número 13,  Imprima eles em ordem decrescente.
andar = 21 
for i in range(20):
    andar = andar - 1
    if(andar == 13):
        continue
    if(andar == 21):
        break
    print("Este é o andar nº" , andar)

    
#Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.
andar = 21
print("Inicio do código while")
while(andar > 1):
    andar = andar - 1
    if(andar == 13):
        continue
    if(andar == 21):
        break
    print("Este é o andar nº", andar)
    


