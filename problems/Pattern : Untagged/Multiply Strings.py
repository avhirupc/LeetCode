def convert_to_number(num1:str)-> int:
    num=0
    l=len(num1)
    num1=num1[::-1]
    for pos,digit in enumerate(num1):
        num+=(int(digit)*(pow(10,pos)))
    return num

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1=convert_to_number(num1)
        num2=convert_to_number(num2)
        return str(num1*num2)
    
    
        