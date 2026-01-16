## Python functions and Async Basic

def text_splitter(text:str,size:int=300)->list[str]:
    l=[text[i:i+300] for i in range(0,len(text),size)]
    return l

text=input("Enter a paragraph: ")

print(text_splitter(text))
print(len(text_splitter(text)))

#Async fun

import asyncio

async def Alarm():
    """this function is a simple async finction which tells the time after 2 sec of calling 
    """
    await asyncio.sleep(2)
    print("Alarming wake up!!!")

result=asyncio.run(Alarm())
print(result)#This returns a None