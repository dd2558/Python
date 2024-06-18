from random import randint
distance = 0

#while문은 false 값이 나올때까지 반복...메모리 주의
"""
while distance < 5:
  print("런닝중...", distance, "km")
  distance = distance + 1
"""
print("카지노에 오신것을 환영합니다.")
  
pc_choice = randint(1,30)

#정답이 맞을 시 False값으로 while문 종료
playing = True
while playing:
  user_choice = int(input("번호를 입력해주세요"))
  if user_choice == pc_choice:
    print("정답입니다. 축하드립니다.")
    playing = False
  elif user_choice > pc_choice:
    print("정답은 입력받은 값보다 작습니다.")
  elif user_choice < pc_choice:
    print("정답은 입력받은 값보다 큽니다.")
        