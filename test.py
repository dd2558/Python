def say_hello():
  print("Hi guys")
  
def say_bye():
  print("Bye guys")
  
def my_name():
  print("My name is 동원")  
  
def double_func():
  print("One")
  print("Two")  

a=2
b=5

def cal(a,b):
  print(a+b)
  
def cal2(a,b):
  a=5
  b=10
  print(a+b)  
  

say_hello()
say_bye()
my_name()
double_func()
cal(a,b)
cal2(a,b)


#def 를 통한 function을 정의, Java와 차이점은 {}가 들어가지 않고 : 와 띄어쓰기 두칸으로 정의
#매개변수값을 호출시에 넣어주고 전역변수를 호출 or 지역변수를 선언 후 선언 가능