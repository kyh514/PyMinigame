from tkinter import *
import os

# 최상위 객체
root = Tk()

root.title("Python 미니게")
# 사이즈 고정시키기(800*640의 크기, x축으로 500, y축으로 200만큼 이동)
root.geometry("800x640+500+200")
# 사이즈 조절 불가
root.resizable(False, False)

root.configure(bg='pink')

def pingpong():
    os.system('minigame1.py')

def pairgame():
    os.system('minigame2.py')

label2 = Label(root, width=10, height=10, bg='pink')
label2.pack()

label1 = Label(root, text = "미니게임", bg='pink', font=('굴림', 30, 'bold'), width=20)
label1.pack(pady=30)

label2 = Label(root, width=10, height=1, bg='pink')
label2.pack()

btnPingpong= Button(label2, text="핑퐁게임", bg="lightblue", borderwidth=0, font=('굴림', 20, 'bold'), pady=20, cursor="hand2", command=pingpong)
btnPingpong.pack(side="left", padx=10)

btnPair = Button(label2, text="짝맞추기", bg="lightblue", borderwidth=0, font=('굴림', 20, 'bold'), pady=20, cursor="hand2", command=pairgame)
btnPair.pack(side="left", padx=10)


# mainloop() 반복문을 계속 돌겠다. 
# 왜 사용하냐면 이벤트를 체크하기 위해서
root.mainloop()

