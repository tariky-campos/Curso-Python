var_global = str(input("Input your name: "))

def escreve_texto():
    i = 0
    i = int(input("Do you agree to change your name: (1-Yes, 0-No)"))
    if( i != 0):
        global var_global       
        var_global = str(input("Input your new name: "))  
        

if __name__ == '__main__':
    escreve_texto()
    print(var_global)
    
    