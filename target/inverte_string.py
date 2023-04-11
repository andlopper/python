def inverte(string):

    invertidos = []    
    
    for i in range(len(string)-1, -1, -1): # Percorre a string do fim ao início, adicionando cada caractere à lista
        invertidos.append(string[i])
    
    string_invertida = ''
    for caractere in invertidos:
        string_invertida += caractere #Adiciona os caracteres na string
        
    return string_invertida

inverte('socorram me subi no onibus em marrocos')
