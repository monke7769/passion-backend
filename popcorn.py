def table(number, limit):
    
    
    for i in range(1, limit + 1):
        result = number * i
        print(number,'X',i,'=', result)

# Usage
table(1, 7)