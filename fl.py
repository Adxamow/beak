# f=open('oxford.txt','w',encoding='utf-8')
# f.write('Python — высокоуровневый язык программирования ')
# f.close()
# fl=open('python.txt','r',encoding='utf-8')
# print(fl.read())
# fl.close()
##########################################################
# py=open('back.py','w',encoding='utf-8')
# py.write("print('Hello World')")
# py.close()
##########################################################
# login=input("Введите логин: ")
# password=input("Введте пароль: ")
# f=open('passwords.txt','a+',encoding='utf-8')
# f.write(f"{login,password}\n")
# f.close()
###########################################################
# with open('itrun.txt','w',encoding='utf-8')as f:
#     f.write("Python the best!")
# with open('itrun.txt',"r",encoding='utf-8')as re:
#     print(re.read())
# n=0
# while True:
#     n+=1
#     with open(f'hello{n}.txt','w',encoding='utf-8')as h:
#         h.write(f"Hello world{n}")
#     if n==200:
#         print("stop")
#         break