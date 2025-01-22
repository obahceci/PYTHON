import typing
from typing import List,Dict,Set,Optional,Any,Sequence,Callable



#x : str = 1
#hata vermez sadece değişkenin tipinin belirtilen şekilde olması gerektiğini ifade eder

'''
def add(a: int, b: int, c: int) -> int:     #eğer bir şey döndürüyorsa bir değişken tipinde olmalıdır

    return a+b+c

x=add(1,2,3)
print(x)

'''

'''
def add(a: int, b: int, c: int) -> None:        #eğer bir şey döndürmüyorsa None tipinde olur
    print(a+b+c)


add(1,2,3)

'''



# x : List[list[int]] = [[1,2,3],[4,5,6]]


# x: Dict[str,str]={"a":"b"}

# x : Set[str] = {"a","b","c"}

# x: Set[float]={"a","b","c"}      #yine set olsa da float olsa da hata vermez




'''
Vector= List[float]

Vectors=List[Vector]

def foo(v:Vector)->Vector:          #Vector tipinde bir değişken alır ve Vector tipinde bir değişken döndürür
    
    return print(v)
    
def foo2(v:Vectors)->Vectors:      #Vectors tipinde bir değişken alır ve Vectors tipinde bir değişken döndürür  
    return  print(v)


foo([1,2,3])
foo2([[1,2,3],[4,5,6]])

'''




'''
def foo(output:Optional[bool]=False)->bool:          #fonksiyonun parametresi opsiyoneldir paramteresiz de çağırılabilir
    pass


foo()

'''




''' 
def foo(output:Any)->Any:   #Any tipinde bir değişken alır ve Any tipinde bir değişken döndürür
    pass

foo(1)

'''

'''
def foo(output:Sequence[str]):
    print(output)

foo(["a","b","c"])
# foo(1)       #Argument 1 to "foo" has incompatible type "int"; expected "Sequence[str]"  [arg-type]
foo("a")
'''





#callable what you use whern you want to accept a function as an argument
'''
def add(x:int,y:int)->int:
    return x+y

def foo(func: Callable[[int,int],int])->None:
    x=int(input("x:"))
    y=int(input("y:"))
    print(f"{func.__name__} result is {func(x,y)}")



foo(add)

'''

