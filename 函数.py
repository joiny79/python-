money=500000
name=None
name=input("请输入你的名字：")
def query(show_header):
    if show_header:
        print("-------查询余额--------")
    print(f"{name}，你好，你的余额剩余{money}元")
def saving(num):
    global money
    money=money+num
    print("-------存款-------")
    print(f"{name}，您好，您存款{num}元成功")

    query(False)
def get_money(num):
    global money
    money+=num
    print("--------取款---------")
    print(f"{name},您好，您取款{num}元成功")

    query(False)
def main():
    print("-------主菜单-------")
    print(f"{name},您好，欢迎来到刘氏银行ATM，请选择操作")
    print("查询余额[输入1]")
    print("存款[输入2]")
    print("取款[输入3]")
    print("退出[输入4]")
    return input("请输入您的选择：")
while True:
    keyboard_input=main()
    if keyboard_input=="1":
        query(True)
        continue
    elif keyboard_input=="2":
        num=int(input("您想要存多少钱："))
        saving(num)
        continue
    elif keyboard_input=="3":
        num=int(input("你想要取多少钱："))
        get_money(num)
        continue
    else:
        print("程序退出")
        break
