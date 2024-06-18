#if
# if 10 > 5:
#   print("True")

#비밀번호 확인 로직
password = 2345

def check_password(password):
  if password == 1234:
    return True

answer = check_password(password)
if answer ==True:
  print("환영합니다")
else:
  print("비밀번호가 일치하지 않습니다")
check_password(password)

#if else X elif O
winner = 10

if winner > 10:
  print("winner is greater than 10")
elif winner < 10:
  print("winner is less than 10")
else:
  print("winner is 10")    
  
#input
age = int(input("당신의 나이는 몇살입니까?"))
print("입력받은 나이", age)
if age >19:
  print("한잔해")
elif age <19 and age>0:
  print("으디 으린노무 자식이 술을")
elif age > 100:
  print("이제 그만 드세요")
elif age<0:
  print("0이상의 나이를 입력하세요")  