#Java의 for문과 형식이 다름... for(int i=0; i<websites.length; i++)를
# for website in websites :
# print("머시기") 를 실행시키면 각각의 item들이 실행될때마다 for문의 코드가 실행됨
# 보통은 복수형으로 튜플이나 리스트를 선언 후 거기서 s를 빼고 for문에 넣음

"""
websites = (
  "google.com",
  "airbnb.com",
  "twitter.com",
  "facebook.com",
  "tiktok.com"
)

for website in websites:
  print("hello", website)
  

foods = [
  "김치",
  "쌀밥",
  "제육볶음",
  "샐러드"
]

for food in foods:
  print("냉장고안에는",food,"(이)가 있습니다")
  print("냉장고안에는",f"{food}","(이)가 있습니다")
"""

websites = (
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com"
)

for website in websites:
  if website.startswith("https://"):
    print("접속 가능")
  else:
    print("접속 불가능")
    
for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  print("최종 URL",website)
print("URL =" ,website)      