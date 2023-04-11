def fibonacci(n):

    fib = [0, 1]
    while fib[-1] < n: #Enquanto o último valor da sequência atual for menor que n
        fib.append(fib[-1] + fib[-2]) #Soma os dois últimos valores
    return fib

def pertence(n):
    fib = fibonacci(n)
    if n in fib: #Verifica se o número contém na sequência
        return f"O número {n} pertence à sequência de Fibonacci: {fib}"
    else:
        return f"O número {n} não pertence à sequência de Fibonacci: {fib}"

    
n = int(input("Digite um valor: "))
pertence(n)
