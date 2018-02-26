#_*_ coding:utf-8 _*_
# Author: Qiu
import random
c = 0
while c < 3:
    age = int(random.random()*100)
    guess = raw_input("输入数字：")
    if str(guess).isdigit():
        guess = int(guess)
        if guess == age:
            print "你猜对了。"
            break
        elif guess < age:
            print "小了"
        else:
            print "大了"
    else:
        print "请输入数字."
        continue
    continue_confirm = raw_input("继续请输入yes，退出请输入其他字符：")
    if continue_confirm == 'yes':
        c += 1
    else:
        print "退出游戏."
        break
    if c == 3:
        print "真笨，这都猜不对，游戏结束。"