# 숫자
# a = 10
# b = 20
# print(a+b)

# 문자
# a = "안녕"
# b = "하세요"
# print(a+b)

# 문자와 숫자의 조합
# a = 10
# b = "문자"
# print(str(a)+b)

# a = "문자"
# b = 10
# print(a+str(b))

# import  turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# #
# # for i in range(4):
# #     t.forward(100)
# #     t.right(360/4)
# # t.penup()
# # t.setposition(-100,100)
# # t.pendown()
# # for i in range(4):
# #     t.forward(100)
# #     t.right(360/4)
# # t.penup()
# # t.setposition(0,100)
# # t.pendown()
# # for i in range(4):
# #     t.forward(100)
# #     t.right(360/4)
# # t.penup()
# # t.setposition(-100,-100)
# # t.pendown()
# # for i in range(4):
# #     t.forward(100)
# #     t.left(360/4)
#
# # t.circle(50)
# # t.penup()
# # t.setposition(-50,-100)
# # t.pendown()
# # for i in range(4):
# #     t.forward(100)
# #     t.left(90)
# # t.penup()
# # t.setposition(0,-200)
# # t.pendown()
# # t.circle(50)
# # t.penup()
# # t.setposition(-50,-300)
# # t.pendown()
# # for i in range(4):
# #     t.forward(100)
# #     t.left(90)
# #
# # for i in range(4):
# #     t.forward(300)
# #     t.right(90)
# #
# # t.penup()
# # t.setposition(30,0)
# # t.pendown()
# # t.right(90)
# # t.forward(300)
# # for i in range(4):
# #     t.left(90)
# #     t.forward(30)
# #     t.left(90)
# #     t.forward(300)
# #     t.right(90)
# #     t.forward(30)
# #     t.right(90)
# #     t.forward(300)
# #
# # for i in range(2):
# #     t.left(90)
# #     t.forward(30)
# #
# # for i in range(4):
# #     t.left(90)
# #     t.forward(300)
# #     t.right(90)
# #     t.forward(30)
# #     t.right(90)
# #     t.forward(300)
# #     t.left(90)
# #     t.forward(30)
# #
# # t.left(90)
# # t.forward(300)
# # t.right(90)
# # t.forward(30)
# # t.right(90)
# # t.forward(300)
# # t.left(90)
#
# s.mainloop()
# a = input("숫자를 입력 ")
# b = 20
# print(int(a)+b)

# 입력을 받다..
# a = input("입력하세요 ")
# if int(a) < 10:
#     print("a는 10보다 작다")
# elif int(a) < 15:
#     print("a는 15보다 작다")

#  숫자 한개를 입력 받고 그 숫자가 양수인지 음수인지 판정하라.
# a = input("숫자를 입력하시오")
# if int(a) > 0:
#     print("a는 양수이다")
# elif int(a) < 0:
#     print("a는 음수이다")

# 숫자 한개를 입력받고 그 숫자가 짝수인지 홀수 인지 판정하라.
# a = input("숫자를 입력하시오")
# if int(a)%2 == 0:
#     print("a는 짝수입니다")
# else:
#     print("a는 홀수입니다")


# 반복문을 이용하여 0부터 9까지 출력하라.
# 짝수만 출력
# for i in range(10):
#     if i%2==0:
#         print(i)
# for i in range(10):
#     if i%2!=0:
#         print(i)
# 짝수번째는 '짝수' 로 출력

# for i in range(10):
#     if i%2==0:
#         print("짝수")
#     else:
#         print(i)



# 자판기
# coin = input("금액을 지불하십시오")
# 거스름돈 = int(coin)
# while True:
#     print("1.콜라(3000)  2.사이다(2000)  3.커피(5000)  4.환타(3000)")
#     a = input("메뉴를 고르시오")
#     if int(a) == 1:
#         if int(coin) >= 3000:
#             print("콜라를 선택하셨습니다")
#             거스름돈 = 거스름돈 - 3000
#         else:
#             print("금액이 부족합니다")
#             exit()
#     elif int(a) == 2:
#         if int(coin) >= 2000:
#             print("사이다를 선택하셨습니다")
#             거스름돈 = 거스름돈 - 2000
#         else:
#             print("금액이 부족합니다")
#             exit()
#     elif int(a) == 3:
#         if int(coin) >= 5000:
#             print("커피를 선택하셨습니다")
#             거스름돈 = 거스름돈 - 5000
#         else:
#             print("금액이 부족합니다")
#             exit()
#     elif int(a) == 4:
#         if int(coin) >= 3000:
#             print("환타를 선택하셨습니다")
#             거스름돈 = 거스름돈 - 3000
#         else:
#             print("금액이 부족합니다")
#             exit()
#     print("거스름돈은", 거스름돈, "원 입니다")
#     if 거스름돈 < 2000:
#         break

# 1 자판기///
#
# a = 0
# while True:
#     a += 1
#     print(a)
#     if a > 10:
#         break
# a = 0
# while a < 10:
#     a += 1
#     print(a)


# for 문으로 1부터 100까지 출력
# for i in range(1,101):
#     print(i)
# while 문으로 1부터 100까지 출력

# a=0
# while a < 100:
#     a += 1
#     print(a)

# a = 0
# while True:
#     a += 1
#     print(a)
#     if a > 99:
#         break


# 거스름돈 = 1000
# for i in range(10):
#     print("메뉴", i, "번째", 거스름돈 ,"금액")
#     거스름돈 = 거스름돈 - i
#
# print(a)

# import random
#
# com = random.randint(1,100)
# # print(com)
# count = 0
# while True:
#     user = input("숫자를 입력하라")
#     count = count + 1
#     if int(user) < com:
#         print("Up")
#     elif int(user) > com:
#         print("Down")
#     else:
#         print("정답", count, "번 만에 맞춤")
#         break

# 리스트..변수

# a = [10,20,30,40,50,60]
# for i in range(6):
#     print(a[i])

# for i in a:
#     print(i)


# 학생 점수 리스트

# 첫번째 수학,국어,과학,영어
# 김철수 = [100,80,70,50]
# 김영희 = [100,100,100,100]
# print(sum(김철수)/4)

# 키리스트 = [150,160,155,178,180,140,167]
# 키리스트.sort()
# print(키리스트)


# 리스트변수 a를 만들고 값을 출력 (4개)

# a = [100, 120, 166, 187]
#
# print(sum(a)/4)


# import turtle
# import random
# s = turtle.Screen()
# player_1 = turtle.Turtle()
# player_1.shapesize(3)
# player_1.color("red")
# player_1.shape("turtle")
# player_1.penup()
# player_1.setposition(-300,200)
#
# player_2 = turtle.Turtle()
# player_2.shapesize(3)
# player_2.color("blue")
# player_2.shape("turtle")
# player_2.penup()
# player_2.setposition(-300,0)
#
# bet = s.textinput("입력", "배팅할 색상을 선택(red or blue)")
# print(bet)
#
# for i in range(200):
#     player_1.forward(random.randint(1,5))
#     player_2.forward(random.randint(1,5))
# write = turtle.Turtle()
# write.hideturtle()
#
# if player_1.xcor() > player_2.xcor() and bet == "red":
#     write.write("레드 승리 배팅 성공", font=("굴림체" ,30,"bold"))
# elif player_1.xcor() < player_2.xcor() and bet == "blue":
#     write.write("블루 승리 배팅 성공", font=("굴림체" ,30,"bold"))
# elif player_1.xcor() > player_2.xcor() and bet == "blue":
#     write.write("레드 승리 배팅 실패", font=("굴림체" ,30,"bold"))
# elif player_1.xcor() < player_2.xcor() and bet == "red":
#     write.write("블루 승리 배팅 실패", font=("굴림체" ,30,"bold"))
#
# s.mainloop()

# t.pensize(3)
# t.pencolor("red")


# import turtle
# s = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
# t.penup()
# t.setposition(200,0)
# t.pendown()
#
# t.pencolor("blue")
# t.left(120)
# t.forward(50)
# t.pencolor("green")
# t.left(120)
# t.forward(50)
#
# for i in range(3):
#     t.pencolor("blue")
#     t.right(120)
#     t.forward(50)
#     t.pencolor("green")
#     t.left(120)
#     t.forward(50)
# t.pencolor("red")
# t.left(120)
# t.forward(200)
#
# s.mainloop()
#
# import turtle
# s = turtle.Screen()
# t = turtle.Turtle()


# def triangle(lenth):
#     t.right(60)
#     for i in range(3):
#         t.forward(lenth)
#         t.right(120)
# t.speed(0)
# def triangle(lenth):
#     for i in range(3):
#         t.forward(lenth)
#         t.left(120)
# triangle(50)
# t.right(90)
# for i in range(4):
#     t.forward(50)
#     t.left(90)
#
# for i in range(3):
#     t.penup()
#     t.forward(100)
#     t.pendown()
#     t.left(90)
#     triangle(50)
#     t.right(90)
#     for j in range(4):
#         t.forward(50)
#         t.left(90)

#
# for i in range(36):
#     t.circle(10)
#     t.penup()
#     t.left(10)
#     t.forward(20)
#     t.pendown()

# for i in range(36):
#     t.begin_fill()
#     if i % 3 == 0:
#         t.fillcolor("red")
#     elif  i % 2 == 0:
#         t.fillcolor("blue")
#     else:
#         t.fillcolor("green")
#     t.circle(10)
#     t.end_fill()
#     t.penup()
#     t.left(10)
#     t.forward(20)
#     t.pendown()

# t.penup()
# t.setposition(-300,300)
# t.pendown()
# for i in range(10):
#     t.forward(50)
#     t.right(90)
#     t.forward(50)
#     t.left(90)


#
# s.mainloop()


# 1번
# a = input("수를 입력하시오")
# b = input("다른 수를 입력하시오")
# print(int(a)+int(b))

# 2번
# a = int(input("수를 입력하시오"))
# b = int(input("다른 수를 입력하시오"))
# c = input("수식을 입력하시오")
#
# if c == "+":
#     print(a, "+", b,"=", a + b)
# elif c == "-":
#     print(a, "-", b,"=", a - b)
# elif c == "*":
#     print(a, "*", b,"=", a * b)
# else:
#     print(a, "/", b,"=", a / b)

# 3번
# a = int(input("숫자를 입력하시오"))
# sum = 0
# for i in range(a+1):
#     sum = sum + i
# print(sum)

# 4번
# a = input("숫자를 입력하시오")
# if int(a)%2 == 0:
#     print("짝수입니다")
# else:
#     print("홀수입니다")

# 5번
# a = int(input("숫자를 입력하시오"))
# for i in range(1,10):
#     print(a, "X", i ,"=", a*i)

# 6번
# count_odd = 0
# count_even = 0
# while True:
#     user = int(input("숫자 입력"))
#     if user % 2 == 0:
#         count_even += 1
#     elif user % 2 != 0:
#         count_odd +=1
#     if user == 0:
#         print("짝수의 개수", cout_even, "홀수의 개수", count_odd)
#         break

# 7번
# count = 0
# while True:
#     user = int(input("숫자 입력"))
#     sum = user + user
#     count += 1
#     if user > 100:
#         print(sum,sum/user)
#         break

 # 8번
# while True:
#     user = int(input("숫자 입력"))
#     if user == 0:

# import turtle
# import random
#
# s = turtle.Screen()
#
# player1 = turtle.Turtle()
# player1.shapesize(3)
# player1.color('red')
# player1.shape('turtle')
# player1.penup()
# player1.setposition(-300,300)
#
# player2 = turtle.Turtle()
# player2.shapesize(3)
# player2.color("blue")
# player2.shape("turtle")
# player2.penup()
# player2.setposition(-300,0)
#
# player3 = turtle.Turtle()
# player3.shapesize(3)
# player3.color("green")
# player3.shape("turtle")
# player3.penup()
# player3.setposition(-300,-300)
#
# bet = s.textinput("입력", "배팅할 색상을 선택(red or blue or green)")
# print(bet)
#
# for i in range(200):
#     player1.forward(random.randint(1,5))
#     player2.forward(random.randint(1,5))
#     player3.forward(random.randint(1,5))
# write = turtle.Turtle()
# write.hideturtle()
#
# if bet == "red":
#     if player1.xcor() > player2.xcor() and player1.xcor() > player3.xcor():
#         write.write("배팅 성공", font=("굴림체", 30, "bold"))
#     elif player1.xcor() < player2.xcor() and player1.xcor() < player3.xcor():
#         write.write("배팅 실패", font=("굴림체", 30, "bold"))
#     elif player1.xcor() < player2.xcor() and player1.xcor() > player3.xcor():
#         write.write("배팅 실패", font=("굴림체", 30, "bold"))
#     elif player1.xcor() > player2.xcor() and player1.xcor() < player3.xcor():
#         write.write("배팅 실패", font=("굴림체", 30, "bold"))
#
# elif bet == "blue":
#     if player1.xcor() < player2.xcor() and player2.xcor() > player3.xcor():
#         write.write("배팅 성공", font=("굴림체", 30, "bold"))
#     elif player1.xcor() > player2.xcor() and player1.xcor() > player3.xcor():
#         write.write("배팅 실패", font=("굴림체", 30, "bold"))
#     elif player1.xcor() > player2.xcor() and player1.xcor() < player3.xcor():
#         write.write("배팅 실패", font=("굴림체", 30, "bold"))
#     elif player1.xcor() < player2.xcor() and player2.xcor() > player3.xcor():
#         write.write("배팅 실패", font=("굴림체", 30, "bold"))
#
# elif bet == "green":
#     if player2.xcor() < player3.xcor() and player1.xcor() < player3.xcor():
#         write.write("배팅 성공", font=("굴림체", 30, "bold"))
#     elif player2.xcor() > player3.xcor() and player1.xcor() > player3.xcor():
#         write.write("배팅 실패", font=("굴림체", 30, "bold"))
#     elif player3.xcor() < player2.xcor() and player1.xcor() > player3.xcor():
#         write.write("배팅 실패", font=("굴림체", 30, "bold"))
#     elif player1.xcor() > player3.xcor() and player2.xcor() < player3.xcor():
#         write.write("배팅 실패", font=("굴림체", 30, "bold"))
#
# s.mainloop()

# import turtle
# import random
# t = turtle.Turtle()
# s = turtle.Screen()
# colors = ['red','blue','green','orange','black','violet']
# t.speed(0)
#
# for i in range(100):
#     x = random.randint(-300,300)
#     y = random.randint(-300,300)
#     t.color(random.choice(colors))
#     t.pensize(random.randint(1,10))
#     for j in range(4):
#         t.forward(100)
#         t.right(90)
#     t.penup()
#     t.setposition(x,y)
#     t.pendown()
#
# s.mainloop()

# 심심해서 만든 졸라맨 코드
# import turtle
# t = turtle.Turtle()
# s = turtle.Screen()
#
# t.circle(50)
# t.right(90)
# t.forward(150)
# t.penup()
# t.setposition(0,0)
# t.pendown()
# t.right(45)
# t.forward(90)
# t.penup()
# t.setposition(0,0)
# t.pendown()
# t.left(90)
# t.forward(90)
# t.penup()
# t.setposition(0,-150)
# t.pendown()
# t.right(80)
# t.forward(120)
# t.penup()
# t.setposition(0,-150)
# t.pendown()
# t.left(70)
# t.forward(120)
#
#
# s.mainloop()
#
# import turtle
# import random
# import time
# t = turtle.Turtle()
# t.shape('turtle')
# t.shapesize(3)
# t.color('blue')
# s = turtle.Screen()
#
# playing = True
#
# t.up()
# def up():
#     t.setheading(90)
# def down():
#     t.setheading(270)
# def left():
#     t.setheading(180)
# def right():
#     t.setheading(0)
# def space():
#     global playing
#     if playing == True:
#         playing = False
#     else:
#         playing = True
#         # s.clear()
#         s.reset()
#         play()
#
# s.listen()
# s.onkeypress(up,"Up")
# s.onkeypress(down,"Down")
# s.onkeypress(left,"Left")
# s.onkeypress(right,"Right")
# s.onkeypress(space,"space")
#
# score = turtle.Turtle()
# p = turtle.Turtle()
# p.shape('turtle')
# p.shapesize(3)
# p.color('red')
# p.penup()
# p.setposition(78,-340)
# b = turtle.Turtle()
# b.shape('circle')
# b.shapesize(1)
# b.color('green')
# b.penup()
# x = random.randint(-300, 300)
# y = random.randint(-300, 300)
# b.setposition(x,y)
# write = turtle.Turtle()
# write.hideturtle()
# wall = turtle.Turtle()
# wall.hideturtle()
# wall.speed(0)
# wall.penup()
# wall.setposition(-480,-400)
# wall.pendown()
# wall.pensize(25)
# wall.left(90)
# score.hideturtle()
# score.penup()
# count = 0
# score.setposition(400,-330)
# score.write(count, font=("굴림체", 30, "bold"))
# t.speed(7)
# b.speed(0)
# p.speed(5)
# score.speed(0)
# speed_up = turtle.Turtle()
# speed_up.shape('circle')
# speed_up.color('aqua')
# speed_up.hideturtle()
# speed_up.penup()
# x2 = random.randint(-300, 300)
# y2 = random.randint(-300, 300)
# speed_up.setposition(x2,y2)
# smaller = turtle.Turtle()
# smaller.shape('circle')
# smaller.shapesize(1)
# smaller.color('black')
# smaller.hideturtle()
# smaller.penup()
# x3 = random.randint(-300, 300)
# y3 = random.randint(-300, 300)
# smaller.setposition(x3,y3)
#
# sm = random.randint(1,8)
# while True:
#     sm = random.randint(1,8)
#     if sm == 1:
#         print("test")
#         smaller.showturtle()
#         break
#
# while True:
#     u = random.randint(1, 5)
#     if u == 1:
#         print("test")
#         speed_up.showturtle()
#         break
# for i in range(2):
#     wall.forward(800)
#     wall.right(90)
#     wall.forward(950)
#     wall.right(90)
# eat = 0
# ate = 0
# def play():
#     global playing, count,eat,ate
#     if eat == 0:
#         t.forward(7)
#     else:
#         for i in range(30):
#             t.forward(10)
#
#     if ate == 0:
#         t.shapesize(3)
#     else:
#         t.shapesize(1)
#         for i in range(30):
#             t.forward(7)
#
#
#     t.forward(10)
#     ang = p.towards(t.pos())
#     num = random.randint(1, 10)
#     if num == 1:
#         p.setheading(ang)
#     p.forward(10)
#     if t.distance(p) < 57:
#         write.write("충돌", font=("굴림체", 30, "bold"))
#         # time.sleep(5)
#         playing = False
#     # print(playing)
#     b.speed(0)
#     if t.distance(b) < 60:
#         x = random.randint(-300, 300)
#         y = random.randint(-300, 300)
#         b.setposition(x,y)
#         count += 1
#         score.clear()
#         score.write(count, font=("굴림체", 30, "bold"))
#     if t.distance(speed_up) < 60:
#         speed_up.hideturtle()
#         x2 = random.randint(-300, 300)
#         y2 = random.randint(-300, 300)
#         speed_up.setposition(x2,y2)
#         eat = 1
#         while True:
#             u = random.randint(1, 5)
#             if u == 1:
#                 print("test")
#                 speed_up.showturtle()
#                 break
#     if t.distance(smaller) < 60:
#         smaller.hideturtle()
#         x3 = random.randint(-300, 300)
#         y3 = random.randint(-300, 300)
#         smaller.setposition(x3, y3)
#         ate = 1
#         sm = random.randint(1, 8)
#         while True:
#             sm = random.randint(1, 8)
#             if sm == 1:
#                 print("test")
#                 smaller.showturtle()
#                 break
#
#
#     if playing:
#         s.ontimer(play,100)
#     if t.xcor() > 420:
#         t.backward(10)
#         t.right(180)
#     elif t.xcor() < -420:
#         t.backward(10)
#         t.right(180)
#     elif t.ycor() > 360:
#         t.backward(10)
#         t.right(180)
#     elif t.ycor() < -360:
#         t.backward(10)
#         t.right(180)
#
#     if p.xcor() > 420:
#         p.backward(10)
#         p.right(180)
#     elif p.xcor() < -420:
#         p.backward(10)
#         p.right(180)
#     elif p.ycor() > 360:
#         p.backward(10)
#         p.right(180)
#     elif p.ycor() < -360:
#         p.backward(10)
#         p.right(180)
# play()
# s.mainloop()
# while playing:

# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return '제발 홍수나서 학교 안 가게 해주세요 제발 홍수나서 학교 안 가게 해주세요 제발 홍수나서 학교 안 가게 해주세요 제발 홍수나서 학교 안 가게 해주세요 제발 홍수나서 학교 안 가게 해주세요 제발 홍수나서 학교 안 가게 해주세요'
#
# @app.route('/a')
# def a():
#     return 'hi'
#
# if __name__ == '__main__':
#     app.run(debug=True , host = "192.168.0.109", port = "5000")
#
# from flask import Flask, render_template
# app = Flask(__name__)
# student_data = {
#     1: {"name": "슈퍼맨", "score": {"국어": 90, "영어": 70, "수학": 65, "과학": 40}},
#     2: {"name": "배트맨", "score": {"국어": 75, "영어": 80, "수학": 75, "과학": 90}},
#     3: {"name": "김우찬", "score": {"국어": 90, "영어": 98, "수학": 95, "과학": 100}},
#     4: {"name": "변예은", "score": {"국어": 95, "영어": 90, "수학": 85, "과학": 95}}
# }
# @app.route('/')
# def index():
#     return render_template("index.html",
#             template_students = student_data)
# @app.route("/student/<int:id>")
# def student(id):
#     return render_template("student.html",
#             template_name=student_data[id]["name"],
#             template_score=student_data[id]["score"])
# if __name__ == '__main__':
#     app.run(debug=True, host = "192.168.0.109")


# 1번
# for i in range(1,16):
#     print(i)

# 2번
# a = int(input("100 이하의 숫자를 입력하세요"))
# i = 1
# sum = 0
# while True:
#     if i == a:
#         print(sum)
#         break
#     # print(i)
#     i = i + 1
#     sum = sum + i

# while i <= a:
#     # print(i)
#     sum = sum + i
#     i = i + 1
# print(sum)

# 3번
# while True:
#     a = int(input("숫자를 입력하세요"))
#     if a > 0:
#         print("이 수는 양수입니다")
#     if a < 0:
#         print("이 수는 음수입니다")
#     if a == 0:
#         print("프로그램을 종료합니다")
#         break

# 4번
# count = 0
# sum = 0
# while True:
#     a = int(input("숫자를 입력하세요"))
#     if a >= 100:
#         print('합계 :',sum, '평균 :', sum/count)
#         break
#     count +=1
#     sum = sum+a


# 5번
# a = int(input("숫자를 입력하시오"))
# for i in range(1,a+1):
#     print(i)

# 6번
# count_even = 0
# count_odd = 0
# while True:
#     a = int(input("숫자를 입력하세요"))
#     if a ==0:
#         print("지금까지 입력된 수 중 짝수는",count_even,"개, 홀수는",count_odd,"개입니다")
#         break
#     if a % 2 ==0:
#         count_even += 1
#     if a % 2 !=0:
#         count_odd += 1

# 7번
# count = 0
# sum = 0
# while True:
#     a = int(input("숫자를 입력하세요"))
#     if a > 100:
#         print(sum/count)
#         break
#     count+=1
#     sum = sum + a


# 8번
# count = 0
# while True:
#     a = int(input("숫자를 입력하세요"))
#     if a == 0:
#         print("3과 5의 배수를 제외한 나머지 정수들의 수는",count,"개입니다")
#     count+=1
#     if a%3==0 or a%5==0:
#         count-=1

# 9번
# Y = 0
# y = 0
#
# while True:
#     hight = int(input("높이를 입력하세요"))
#     base = int(input("밑변의 길이를 입력하세요"))
#     print("이 삼각형의 넓이는",hight*base/2,"입니다")
#     con = input("continue?")
#     if con == 'Y' or con == 'y' or con == 'continue':
#         pass
#     else:
#         break

import turtle
import time
t = turtle.Turtle()
s = turtle.Screen()
red = turtle.Turtle()
blue = turtle.Turtle()
timer = turtle.Turtle()
timer.hideturtle()
red.shape('turtle')
blue.shape('turtle')
red.shapesize(3)
blue.shapesize(3)
t.pensize(3)
t.hideturtle()
t.speed(0)
timer.speed(0)
timer.penup()
red.speed(4)
blue.speed(4)
red.color('red')
blue.color('blue')
red.penup()
blue.penup()
t.penup()
red.setposition(-200,300)
blue.setposition(-200,-300)
t.setposition(300,350)
timer.setposition(-440,-75)
t.pendown()
t.right(90)
t.forward(700)
t.penup()
t.setposition(-100,0)

start_red = time.time()
start_blue = time.time()


def move(x,y):
    if blue.xcor()  <= 250 and red.xcor() <= 250:
        blue.forward(15)



while True:
    if red.xcor()>250:
        pass
    if blue.xcor()>250:
        pass
    else:
        red.forward(1.2)
    s.onclick(move)
    if blue.xcor()>250:
        pass

    if red.xcor() > 250:
        if red.xcor() > blue.xcor():
            t.write("레드 승리", font=("굴림체", 30, "bold"))
            end_red = time.time()
            timer.write(f"레드가 결승점을  통과하기까지 걸린 시간은 변수 {round(end_red - start_red, 2)} 초 입니다", font=("굴림체", 20, "bold"))
            break

    if blue.xcor() > 250:
        if red.xcor() < blue.xcor():
            t.write("블루 승리", font=("굴림체", 30, "bold"))
            end_blue = time.time()
            timer.write(f"블루가 결승점을  통과하기까지 걸린 시간은 변수 {round(end_blue - start_blue, 2)} 초 입니다", font=("굴림체", 20, "bold"))
            break

s.mainloop()

# start = time.time()
# for i in range(100):
#     t.forward(1)
# end = time.time()
#
# print(round(end-start,2))


