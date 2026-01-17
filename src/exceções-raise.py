from math import sqrt

class NumberNegativeError(Exception):
    def __init__(self):
        pass

if __name__ == '__main__':
    while True:
        try:
            num = int(input("Input a number positive: "))
            if(num < 0):
                raise NumberNegativeError
            
        except NumberNegativeError:
            print(f"Was provided a number negative!")
            continue
        else:
            print(f"A sqrt of {num} is {round(sqrt(num),2)}")
            print("\nEnd od calculation")
            break
        
            