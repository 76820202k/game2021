
#리스트 사용
start = ['발포', '오른쪽 이동', '왼쪽 이동']

#딕셔너리 사용
tatus = {'발포':'적에게 폭탄을 던졌습니다', '오른쪽 이동':'우측으로 계속 이동합니다····', '왼쪽 이동':'좌측으로 계속 이동합니다····'}

for i in range(3):
    print("******* 갤러그 *******")
    print("적 비행기 출몰")
    print("1. 발포 2. 오른쪽 이동 3. 왼쪽 이동")
    number  = int(input("숫자를 입력하세요: "))

#1번 누를 시 총알 발사
    if number == 1:
        print("--------------")
        print(start[0])
        print(tatus.get('발포'))
        print("--------------")

#2번 누를 시 오른쪽 이동
    if number == 2:
        print("--------------")
        print(start[1])
        print(tatus.get('오른쪽 이동'))
        print("--------------")

#3번 누를 시 왼쪽 이동
    if number == 3:
        print("--------------")
        print(start[2])
        print(tatus.get('왼쪽 이동'))
        print("--------------")