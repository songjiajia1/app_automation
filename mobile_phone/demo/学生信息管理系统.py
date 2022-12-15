from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image,ImageTk
import tkinter
import sqlite3

#创建本地数据库
"""
conn.execute ('''CREATE TABLE StudentTable(
    ID INTEGER PRIMARY KEY   AUTOINCREMENT,
    StuId         INTEGER     NOT NULL,
    NAME           TEXT      NOT NULL,
    CLASS            INT       NOT NULL,
    AGE           INTEGER     Not NULL);''')
print("Table created successfully")
"""
#打开本地数据库用于存储用户信息
conn = sqlite3.connect('student1.db')
#主界面
root=Tk()
root.title("学生信息管理系统")
root.config(width=600)
root.config(height=600)


#增加学生信息
def insert_stu():  #录入学生信息
    root1=Tk()
    root1.title("录入学生信息")
    root1.config(width=600)
    root1.config(height=600)
    #创建关联字符变量
    varName=StringVar(root1,value='')
    varId=StringVar(root1,value='')
    varClass=StringVar(root1,value='')
    varAge=StringVar(root1,value='')
    #创建标签组件
    label=Label(root1,text="姓名：",font=("微软雅黑 -20"))
    #label.grid(row=0,sticky=E)
    label.place(x=30,y=60,height=40,width=80)
    label=Label(root1,text="学号：",font=("微软雅黑 -20"))
    #label.grid(row=1,sticky=E)
    label.place(x=30,y=110,height=40,width=80)
    label=Label(root1,text="班级：",font=("微软雅黑 -20"))
    #label.grid(row=2,sticky=E)
    label.place(x=30,y=160,height=40,width=80)
    label=Label(root1,text="年龄：",font=("微软雅黑 -20"))
    #label.grid(row=3,sticky=E)
    label.place(x=30,y=210,height=40,width=80)
    #创建文本框组件，同时设置关联的变量
    #    姓名entryName
    #    学号entryId
    #    班级entryClass
    #    年龄entryAge
    entryName=Entry((root1),textvariable=varName)
    #entryName.grid(row=0,column=1,sticky=W)
    entryName.place(x=120,y=60,height=40,width=200)
    entryId=Entry((root1),textvariable=varId)
    #entryId.grid(row=1,column=1,sticky=W)
    entryId.place(x=120,y=110,height=40,width=200)
    entryClass=Entry((root1),textvariable=varClass)
    #entryClass.grid(row=2,column=1,sticky=W)
    entryClass.place(x=120,y=160,height=40,width=200)
    entryAge=Entry((root1),textvariable=varAge)
    #entryAge.grid(row=3,column=1,sticky=W)
    entryAge.place(x=120,y=210,height=40,width=200)
    def buttonOK():
       i=0
       conn = sqlite3.connect('student1.db')
       stu_id = eval(entryId.get())#学号输入
       stu_name =str(entryName.get())#姓名录入
       stu_class =eval(entryClass.get())#班级录入
       stu_age=eval(entryAge.get())#年龄录
       cursor = conn.execute("SELECT * from StudentTable;")
       conn.commit()
       for row in cursor:#进行遍历查找是否有重复的学号
           if stu_id==row[0]:
               i=1
               break
           else:
               i=0
               #查找完成若有重复的学号，则警告。否则录入数据库
       if i==1:
           messagebox.showerror('警告',message='学号重复，请重新输入')
       else:
           try:
               sql1 = "INSERT INTO StudentTable(StuId,NAME,CLA,AGE)"
               sql1+="VALUES(%d,'%s',%d,%d)"%(stu_id,stu_name,stu_class,stu_age)
               conn.execute(sql1)
               conn.commit()
               messagebox.showinfo(title='恭喜',message='录入成功！')
               root1.destroy()
           except:
               messagebox.showerror('警告',message='未录入成功')
    buttonbuttonOK=Button(root1,text="录入学生信息",font=("微软雅黑 -20"),command=buttonOK)
    buttonbuttonOK.place(x=150,y=300,height=40,width=200)
    def cancel():
        varName.set('')
        varId.set('')
        varClass.set('')

        varAge.set('')
    # 取消键
    buttonCancel = Button(root1, text="取消", font=("微软雅黑 -20"), command=cancel)
    buttonCancel.place(x=150, y=350, height=40, width=200)

    # 退出键
    buttondel = Button(root1, text="退出", font=("微软雅黑 -20"), command=root1.destroy)
    buttondel.place(x=150, y=400, height=40, width=200)
    root1.mainloop()


#删除学生信息
def delete_stu():
    root2=Tk()
    root2.title("删除学生信息")
    root2.config(width=600)
    root2.config(height=600)

    #创建标签
    label=Label(root2,text="学号：",font=("微软雅黑 -20"))
    #label.grid(row=1,sticky=E)
    label.place(x=30,y=20,height=40,width=80)
    entryId=Entry(root2)
    entryId.place(x=120,y=20,height=40,width=200)

    def delete():
        conn = sqlite3.connect('student1.db')
        stu_id = eval(entryId.get())#学号输入
        conn.execute("DELETE from StudentTable where StuId = '%s';"%stu_id)
        conn.commit()
        messagebox.showinfo(title='恭喜',message='删除成功！')
        root2.destroy()

    #删除键
    buttondelete=Button(root2,text="删除",font=("微软雅黑 -20"),command=delete)
    buttondelete.place(x=150,y=160,height=40,width=200)

    #退出键
    buttondel=Button(root2,text="退出",font=("微软雅黑 -20"),command=root2.destroy)
    buttondel.place(x=150,y=210,height=40,width=200)
    root2.mainloop()


#查询学生信息
def sel_stu():
    root3=Tk()
    root3.title("查询学生信息")
    root3.config(width=600)
    root3.config(height=600)

    #创建关联变量
    sId=StringVar(root3,value='')

    #创建文本组件框\标签组件
    label=Label(root3,text="学号",font=("微软雅黑 -20"))
    label.place(x=30,y=10,height=40,width=80)
    selId=Entry((root3),textvariable=sId)
    selId.place(x=120,y=10,height=40,width=200)

    def select():
        #创建关联字符变量
        varName=StringVar(root3,value='')
        varId=StringVar(root3,value='')
        varClass=StringVar(root3,value='')
        varAge=StringVar(root3,value='')
        conn = sqlite3.connect('student1.db')
        stu_id = eval(selId.get())#学号输入
        cursor = conn.execute("SELECT * from StudentTable where StuId = '%d';"%stu_id)
        conn.commit()
        for row in cursor:
             if stu_id == row[0]:
                 stu_name=row[1]
                 stu_class=row[2]
                 stu_age=row[3]
        #创建标签组件
        label=Label(root3,text="姓名：",font=("微软雅黑 -20"))
        #label.grid(row=0,sticky=E)
        label.place(x=30,y=110,height=40,width=80)
        label=Label(root3,text="学号：",font=("微软雅黑 -20"))
        #label.grid(row=1,sticky=E)
        label.place(x=30,y=160,height=40,width=80)
        label=Label(root3,text="班级：",font=("微软雅黑 -20"))
        #label.grid(row=2,sticky=E)
        label.place(x=30,y=210,height=40,width=80)
        label=Label(root3,text="年龄：",font=("微软雅黑 -20"))
        #label.grid(row=3,sticky=E)
        label.place(x=30,y=260,height=40,width=80)
        #创建文本框组件，同时设置关联的变量
        #    姓名entryName
        #    学号entryId
        #    班级entryClass
        #    年龄entryAge
        entryName=Entry((root3),textvariable=varName)
        #entryName.grid(row=0,column=1,sticky=W)
        entryName.place(x=120,y=110,height=40,width=200)
        entryId=Entry((root3),textvariable=varId)
        #entryId.grid(row=1,column=1,sticky=W)
        entryId.place(x=120,y=160,height=40,width=200)
        entryClass=Entry((root3),textvariable=varClass)
        #entryClass.grid(row=2,column=1,sticky=W)
        entryClass.place(x=120,y=210,height=40,width=200)
        entryAge=Entry((root3),textvariable=varAge)
        #entryAge.grid(row=3,column=1,sticky=W entryAge.place(x=120,y=260,height=40,width=200)
        varName.set(stu_name)
        varId.set(stu_id)
        varClass.set(stu_class)
        varAge.set(stu_age)
    #查询键
    buttonselect=Button(root3,text="查询",font=("微软雅黑 -20"),command=select)
    buttonselect.place(x=200,y=60,height=40,width=100)
    #取消键
    def cancel():
        sId.set('')
    buttoncancel=Button(root3,text="取消",font="微软雅黑 -20",command=cancel)
    buttoncancel.place(x=50,y=60,height=40,width=100)
    #退出键
    buttondel=Button(root3,text="退出",font="微软雅黑 -20",command=root3.destroy)
    buttondel.place(x=350,y=60,height=40,width=100)
    root3.mainloop()


#修改学生信息
def change_stu():
    root4=Tk()
    root4.title("修改学生信息")
    root4.config(width=600)
    root4.config(height=600)
    #创建关联变量
    sId=StringVar(root4,value='')
    #创建文本组件框\标签组件
    label=Label(root4,text="学号",font=("微软雅黑 -20"))
    label.place(x=30,y=10,height=40,width=80)
    selId=Entry((root4),textvariable=sId)
    selId.place(x=120,y=10,height=40,width=200)
    #创建关联字符变量
    varName=StringVar(root4,value='')
    varId=StringVar(root4,value='')
    varClass=StringVar(root4,value='')
    varAge=StringVar(root4,value='')
    #创建标签组件
    label=Label(root4,text="姓名：",font=("微软雅黑 -20"))
    #label.grid(row=0,sticky=E)
    label.place(x=30,y=110,height=40,width=80)
    label=Label(root4,text="学号：",font=("微软雅黑 -20"))
    #label.grid(row=1,sticky=E)
    label.place(x=30,y=160,height=40,width=80)
    label=Label(root4,text="班级：",font=("微软雅黑 -20"))
    #label.grid(row=2,sticky=E)
    label.place(x=30,y=210,height=40,width=80)
    label=Label(root4,text="年龄：",font=("微软雅黑 -20"))
    #label.grid(row=3,sticky=E)
    label.place(x=30,y=260,height=40,width=80)
        #创建文本框组件，同时设置关联的变量
        #    姓名entryName
        #    学号entryId
        #    班级entryClass
        #    年龄entryAge
    entryName=Entry((root4),textvariable=varName)
        #entryName.grid(row=0,column=1,sticky=W)
    entryName.place(x=120,y=110,height=40,width=200)
    entryId=Entry((root4),textvariable=varId)
    #entryId.grid(row=1,column=1,sticky=W)
    entryId.place(x=120,y=160,height=40,width=200)
    entryClass=Entry((root4),textvariable=varClass)
        #entryClass.grid(row=2,column=1,sticky=W)
    entryClass.place(x=120,y=210,height=40,width=200)
    entryAge=Entry((root4),textvariable=varAge)
        #entryAge.grid(row=3,column=1,sticky=W)
    entryAge.place(x=120,y=260,height=40,width=200)
    def select():
        conn = sqlite3.connect('student1.db')
        stu_id = eval(selId.get())#学号输入
        cursor = conn.execute("SELECT * from StudentTable where StuId = %d;"%stu_id)
        conn.commit()
        for row in cursor:
             if stu_id == row[0]:
                 stu_name=row[1]
                 stu_class=row[2]
                 stu_age=row[3]
        varName.set(stu_name)
        varId.set(stu_id)
        varClass.set(stu_class)
        varAge.set(stu_age)
    def saveName():
        name=entryName.get()
        conn=sqlite3.connect('student1.db')
        sql="UPDATE StudentTable SET NAME='%s' WHERE StuId=%d;"%(name,eval(selId.get()))
        conn.execute(sql)
        conn.commit()
        messagebox.showinfo(title='恭喜',message='保存成功！')
    def saveCla():
        cla=eval(entryClass.get())
        conn=sqlite3.connect('student1.db')
        sql="UPDATE StudentTable SET CLA=%d WHERE StuId=%d;"%(cla,eval(selId.get()))
        conn.execute(sql)
        conn.commit()
        messagebox.showinfo(title='恭喜',message='保存成功！')
    def saveAge():
        age=eval(entryAge.get())
        conn=sqlite3.connect('student1.db')
        sql="UPDATE StudentTable SET AGE=%d WHERE StuId=%d;"%(age,eval(selId.get()))
        conn.execute(sql)
        conn.commit()
        messagebox.showinfo(title='恭喜',message='保存成功！')
    #保存键
    buttonname=Button(root4,text="保存",font=("微软雅黑 -20"),command=saveName)
    buttonname.place(x=330,y=110,height=40,width=60)
    buttoncla=Button(root4,text="保存",font=("微软雅黑 -20"),command=saveCla)
    buttoncla.place(x=330,y=210,height=40,width=60)
    buttonage=Button(root4,text="保存",font=("微软雅黑 -20"),command=saveAge)
    buttonage.place(x=330,y=260,height=40,width=60)
    def cancel():
        sId.set('')     #取消键
    buttoncancel=Button(root4,text="取消",font=("微软雅黑 -20"),command=cancel)
    buttoncancel.place(x=20,y=60,height=40,width=60)
    #查询键
    buttonselect=Button(root4,text="查询",font=("微软雅黑 -20"),command=select)
    buttonselect.place(x=100,y=60,height=40,width=60)
    #退出键
    buttondel=Button(root4,text="退出",font="微软雅黑 -20",command=root4.destroy)
    buttondel.place(x=260,y=60,height=40,width=60)
    root4.mainloop()

#创建顶级菜单及其下拉菜单
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=False)
filemenu.add_command(label="增加",command=insert_stu)
filemenu.add_command(label="删除",command=delete_stu)#command接删除函数/下面接修改函数
filemenu.add_command(label="修改",command=change_stu)
filemenu.add_command(label="查询",command=sel_stu)

filemenu.add_separator()
filemenu.add_command(label="退出",command=root.destroy)
menubar.add_cascade(label="菜单",menu=filemenu)

#显示菜单
root.config(menu=menubar)
buttoninsert_stu=Button(root,text="录入学生信息",font=("微软雅黑 -20"),command=insert_stu)
#buttoninsert_stu.grid(row=2,column=0)由下面的代码将该代码覆盖，显示的是在界面上的位置
buttoninsert_stu.place(x=50,y=50,height=40,width=200)
buttondelete_stu=Button(root,text="删除学生信息",font=("微软雅黑 -20"),command=delete_stu)
#buttondelete_stu.grid(row=2,column=1)
buttondelete_stu.place(x=50,y=150,height=40,width=200)
buttonchange_stu=Button(root,text="修改学生信息",font=("微软雅黑 -20"),command=change_stu)
#buttonchange_stu.grid(row=4,column=0)
buttonchange_stu.place(x=50,y=250,height=40,width=200)
buttonsel_stu=Button(root,text="查询学生信息",font=("微软雅黑 -20"),command=sel_stu)
#buttonsel_stu.grid(row=4,column=1)
buttonsel_stu.place(x=50,y=350,height=40,width=200)
root.mainloop()