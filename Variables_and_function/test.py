def say_hello():
  print("Hi guys")
  
def say_bye():
  print("Bye guys")
  
def my_name():
  print("My name is Dong")  
  
def double_func():
  print("One")
  print("Two")  

a=2
b=5

def cal(a=1,b=2):
  print(a+b)

def cal2(a,b):
  a=5
  b=10
  print(a+b)  

def cal3(a,b):
  print(a*b)

def about_me(user_name="누구?",user_age=19):
  print("Hello my name is",user_name,"and i'm",user_age,"years old")

say_hello()
say_bye()
my_name()
double_func()

cal(a,b)
cal(10,15)
cal()
cal2(a,b)
cal3(10,10)

about_me("Dong",26)
about_me()

#변수 정의는 Java와 다르게 타입을 선언하지 않아도 자동으로 타입이 맞춰짐

#def 를 통한 function을 정의, Java와 차이점은 {}가 들어가지 않고 : 와 띄어쓰기 두칸으로 정의

#매개변수값을 호출시에 넣어주고 전역변수를 호출 or 지역변수를 선언 후 선언 가능

#function()으로 매게변수값을 비워두고 def를 통해 선언한 function의 매개변수값에 = 를 통해 매개변수가 없을 시 출력할 임의의 예외처리 가능

#수수료 계산기 만들기
def per_cal(sell_money=20000):
  return sell_money * 0.25
#Return을 이용해서 값 저장하기
def pay_cal(charge=5000):
  print("당신이 낸 수수료는 = ",charge,"원 입니다.")

to_pay = per_cal(20000)
to_pay = per_cal()
pay_cal(to_pay)
pay_cal()  

My_name = "dongdong"

#변수명을 넣어서 출력하고싶을때는 f""안에 EL표기볍처럼 사용하면됨
print(
  f"Hello I'm {My_name}"
)
