from random import randint
#import문 사용시 위와같이 선언
#범위 주석 사용시 """ 3개를 시작과 끝에 써주기.
user_choice = int(input("숫자를 입력해주세요."))
pc_choice = randint(1,10)

if user_choice == pc_choice:
  print("당신이 이겼습니다.")
elif user_choice > pc_choice:
  print("정답보다 입력받은 숫자가 높습니다. 정답은", f"{pc_choice}")
elif user_choice < pc_choice:
  print("정답보다 입력받은 숫자가 낮습니다. 정답은", f"{pc_choice}")  