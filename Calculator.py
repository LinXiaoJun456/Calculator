while True:
    f=input("输入表达式:")
    #功能模块
    try:
        result=eval(f)
        if result%1==0:
            result=int(result)
        print("=",result,"\n")
    #错误处理模块
    except ZeroDivisionError:
        print("除数不能为零！\n")

    except BaseException:
        print("输入错误！\n")
