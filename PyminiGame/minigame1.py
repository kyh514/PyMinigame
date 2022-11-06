import turtle as t
import random
import time

def right():
    if player.xcor() < 200:
        player.forward(10)
    
def left():
    if player.xcor() > -200:
        player.backward(10)

t.bgcolor("Lightpink")
t.setup(500, 700)

# 플레이어
# 공 핑퐁하는  직사각형
player = t.Turtle()
player.shape("square")
# 모양 : 가로가 긴 직사각형
player.shapesize(1,5) # 거북이가 보는 방향을 기준으로
# 이 상태에서 이동하면 선을 그리지 않는다.
player.up()
#그려지는 속도???
player.speed(0)
# 위치를 아래로 
player.goto(0, -270)


# 공
ball = t.Turtle()
ball.shape("circle")
ball.shapesize(1,1)
ball.up()
ball.speed(0)
ball.color("white")


# 키보드로 위치 이동
t.listen()
#t.onkeypress(함수명, "키이름")
t.onkeypress(right, "Right")
t.onkeypress(left, "Left")


# 공 이동을 위한 x, y 좌표값 바꾸기
ball_xspeed = 3
ball_yspeed = 3

# 게임 상태
game_on = True

# 생명력 3개 - 3번 놓치면 게임
life = 3

# 점수표시
t.up()
t.ht()
t.goto(0, 300)
t.write(f"Life : {life}", False, "center", ("", 20))


while game_on:
    new_x = ball.xcor() + ball_xspeed
    new_y = ball.ycor() + ball_yspeed
    ball.goto(new_x, new_y)
    if ball.xcor() > 240 or ball.xcor() < -240:
        ball_xspeed *= -1
    if ball.ycor() > 340:
        ball_yspeed *= -1

    # 아래로 가면 볼을 초기화시켜서 처음 위치로..
    if ball.ycor() < -340:

    # 겜 끝남
    # 0.5초 시간 딜레이
        # 실패하면 life 차감
        life += -1
        t.clear()
        t.write(f"Life : {life}", False, "center", ("", 20))
        time.sleep(0.5)
        ball.goto(0, 100)
        ball_xspeed *= -1
        ball_yspeed *= -1

        if life == 0:
            game_on = False
            t.goto(0,0)
            t.write("Game Over", False, "center", ("", 20))
        
    # 헤드감지
    # turtle.distance(a, b) : 현재 위치와 점(a, b)의 거리를 구한다.
    if player.distance(ball) < 50 and -260 < ball.ycor() < -245:
        ball_yspeed *= -1


t.done()




















