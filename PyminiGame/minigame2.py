import turtle as t
import random
import time

# 클릭한 좌표값과 어떤 turtles이 가까이에 있는지 
def find_card(x, y):
    min_idx = 0
    min_dis = 100
    
    for i in range(16):
        distance = turtles[i].distance(x, y)
        if distance < min_dis:
            min_dis = distance
            min_idx = i
        #print(min_idx)
    return min_idx
        
#
def score_update(m):
    score_pen.clear()
    score_pen.write(f"{m} {score}점/{attempt}번 시도", False, "center", ("", 15))

def result(m):
    t.goto(0, -60)
    t.write(m, False, "center", ("", 30, "bold"))


# 마우스를 클릭한 순간 x,y좌표 얻을 수 있음. why? onscreenclick 때문에
def play(x, y):
    #print(x)
    #print(y)
    global click_num
    global first_pick
    global second_pick
    global attempt
    global score

    if attempt == 12:
        result("게임 오버")
    elif score == 8:
        result("성공")
    else:
        click_num += 1
        # 클릭한 이미지의 idx 찾기
        card_idx = find_card(x, y)
        turtles[card_idx].shape(img_list[card_idx])

        # click_num이 2일 때 정답체크
        if click_num == 1:
            first_pick = card_idx
        elif click_num == 2:
            second_pick = card_idx
            click_num = 0
            attempt += 1

            # 비교해서 정답인지 확인
            if img_list[first_pick] == img_list[second_pick] :
                score += 1
                score_update("정답")
                #if score == 8:
                #    result("성공")
            else:
                score_update("오답")
                turtles[first_pick].shape(default_img)
                turtles[second_pick].shape(default_img)
                    

t.bgcolor("pink")
t.setup(700, 700)
t.up()
t.ht()
t.goto(0, 280)
t.write("카드 매칭 게임", False, "center", ("", 30, "bold"))

# 점수 펜 객체 생성
score_pen = t.Turtle()
score_pen.up()
score_pen.ht()
score_pen.goto(0, 230)


# 터틀 객체들 생성
# 터틀 위치는 좌표값을 통해 지정.(x, y좌표 교차점에 터틀 위치)
turtles = []
pos_x = [-210, -70, 70, 210] 
pos_y = [-250, -110, 30, 170] 

for x in range(4):
    for y in range(4):
        new_turtle = t.Turtle()
        new_turtle.up()
        new_turtle.color("pink")
        new_turtle.speed(0)
        new_turtle.goto(pos_x[x], pos_y[y])
        turtles.append(new_turtle)

default_img = "images/default_img.gif"
#.addshape(image) : 이미지추가
t.addshape(default_img)

img_list = []
for i in range(8):
    img = f"images/img{i}.gif"
    t.addshape(img)
    # 같은 사진 2번씩 저장할거임
    img_list.append(img)
    img_list.append(img)

random.shuffle(img_list)
for i in range(16):
    #turtles 배열 위치에 이미지 하나씩 넣기
    turtles[i].shape(img_list[i])

# 이미지 숨기는 시간
time.sleep(3)

# 숨김이미지
for i in range(16):
    turtles[i].shape(default_img)


# 첫 번째 클릭한 이미지,두 번째 클릭한 이미지 구분을 위한 변수-클릭 횟수(매 2회 클릭마다 정답체크)
click_num = 0
# 점수
score = 0
# 시도한 횟수
attempt = 0
# 첫번째 클릭, 두번째 클릭한 이미지 이름
first_pick = ""
second_pick = ""

# onscreenclick(함수) : 마우스를 클릭했을 때에 ()안의 함수를 실행
t.onscreenclick(play)


t.done()


