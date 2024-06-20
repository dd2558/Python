# Dictionary -> 키- 값을 가지는 사전 {} 로 선언 하나의 사전안에 다른 사전을 정의가능
# Java의 Map과 같은 느낌..?
# 정의된 사전안에 타입은 알아서 맞춰짐
# .pop 메서드를 통해 key값을 삭제 가능

player = {
  "name" : 'dong',
  'age' : 26,
  'alive' : True
}


print(player)

print(player.get("age"))