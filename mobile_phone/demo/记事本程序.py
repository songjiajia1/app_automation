# -*- coding: utf-8 -*-
# @Time    : 2020/12/28
# @Author  : songjj
# @File    : notepad.py
# @Version : 1.0
# @Python Version : 3.9.0
# @Software: PyCharm


from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import os

filename = ''

def new_file(*args):  # 新建文件
    global top, filename, textPad
    top.title("未命名文件")
    filename = None
    textPad.delete(1.0, END)

def open_file(*args):  # 打开文件
    global filename
    filename = askopenfilename(defaultextension=".txt")
    if filename == "":
        filename = None
    else:
        top.title("" + os.path.basename(filename))
        textPad.delete(1.0, END)
        f = open(filename, 'r', encoding="utf-8")
        textPad.insert(1.0, f.read())
        f.close()

def click_open(event):  # 单击打开
    global filename
    top.title("" + os.path.basename(filename))
    textPad.delete(1.0, END)
    f = open(filename, 'r', encoding="utf-8")
    textPad.insert(1.0, f.read())
    f.close()

def save(*args):  # 保存
    global filename
    try:
        f = open(filename, 'w', encoding="utf-8")
        msg = textPad.get(1.0, 'end')
        f.write(msg)
        f.close()
    except:
        save_as()

def save_as(*args):   # 另存为
    global filename
    f = asksaveasfilename(initialfile="未命名.txt", defaultextension=".txt")
    filename = f
    fh = open(f, 'w', encoding="utf-8")
    msg = textPad.get(1.0, END)
    fh.write(msg)
    fh.close()
    top.title("" + os.path.basename(f))

def rename(newname):  # 重命名
    global filename
    name = os.path.basename(os.path.splitext(filename)[0])
    oldpath = filename
    newpath = os.path.dirname(oldpath) + '/' + newname + '.txt'
    os.rename(oldpath, newpath)
    filename = newpath
    refresh()

def rename_file(*args):  # 重命名文件
    global filename
    t = Toplevel()
    t.geometry("260x80+650+250")
    t.title('重命名')
    frame = Frame(t)
    frame.pack(fill=X)
    lable = Label(frame, text="文件名")
    lable.pack(side=LEFT, padx=5)
    var = StringVar()
    e1 = Entry(frame, textvariable=var)
    e1.pack(expand=YES, fill=X, side=RIGHT)
    botton = Button(t, text="确定", command=lambda: rename(var.get()))
    botton.pack(side=BOTTOM, pady=10)

def delete(*args):  # 删除
    global filename, top
    choice = askokcancel('提示', '确定删除吗？')
    if choice:
        if os.path.exists(filename):
            os.remove(filename)
            textPad.delete(1.0, END)
            top.title("记事本")
            filename = ''

def cut():  # 剪切
    global textPad
    textPad.event_generate("<<Cut>>")

def copy():  # 复制
    global textPad
    textPad.event_generate("<<Copy>>")

def paste():  # 粘贴
    global textPad
    textPad.event_generate("<<Paste>>")

def undo():  # 撤销
    global textPad
    textPad.event_generate("<<Undo>>")

def select_all():  # 全选
    global textPad
    textPad.tag_add("sel", "1.0", "end")

def find(*agrs):  # 查找
    global textPad
    t = Toplevel(top)
    t.title("查找")
    t.geometry("260x80+650+250")
    t.transient(top)
    Label(t, text="查找：").grid(row=0, column=0, sticky="e")
    v = StringVar()
    e = Entry(t, width=20, textvariable=v)
    e.grid(row=0, column=1, padx=2, pady=2, sticky="we")
    e.focus_set()
    c = IntVar()
    Checkbutton(t, text="不区分大小写", variable=c).grid(row=1, column=1, sticky='e')
    Button(t, text="查找所有", command=lambda: search(v.get(), c.get(), textPad, t, e)).grid\
        (row=0, column=2, sticky="e" + "w", padx=2, pady=2)

    def close_search():  # 关闭搜索
        textPad.tag_remove("match", "1.0", END)
        t.destroy()

    t.protocol("WM_DELETE_WINDOW", close_search)

def mypopup(event):  # 弹出式菜单
    global editmenu
    editmenu.tk_popup(event.x_root, event.y_root)

def search(needle, cssnstv, textPad, t, e):  # 搜索
    textPad.tag_remove("match", "1.0", END)
    count = 0
    if needle:
        start = 1.0
        while True:
            pos = textPad.search(needle, start, nocase=cssnstv, stopindex=END)
            if not pos:
                break
            strlist = pos.split('.')
            left = strlist[0]
            right = str(int(strlist[1]) + len(needle))
            lastpos = left + '.' + right
            textPad.tag_add("match", pos, lastpos)
            count += 1
            start = lastpos
            textPad.tag_config('match', background="yellow")
        e.focus_set()
        t.title(str(count) + "个被匹配")

def refresh():  # 刷新
    global top, filename
    if filename:
        top.title(os.path.basename(filename))
    else:
        top.title("记事本")

def help():  # 帮助
    showinfo(title='关于记事本', message='功能持续升级中，敬请期待！')

def power():  # 版权
    showinfo(title='版权信息', message='本版权永久免费！')

top = Tk()
top.title("记事本")
top.geometry("750x500+450+150")

menubar = Menu(top)  # 把menu的功能（菜单小部件，显示菜单栏，下拉菜单和弹出菜单）赋给menubar

# 文件功能
filemenu = Menu(top)  # 把menu的功能（菜单小部件，显示菜单栏，下拉菜单和弹出菜单）赋给filemenu
menubar.add_cascade(label="文件", menu=filemenu)   # add_cascade（添加层次菜单项）
filemenu.add_command(label="新建", accelerator="Ctrl+N", command=new_file)
filemenu.add_command(label="打开", accelerator="Ctrl+O", command=open_file)
filemenu.add_command(label="保存", accelerator="Ctrl+S", command=save)
filemenu.add_command(label="另存为", accelerator="Ctrl+shift+s", command=save_as)
filemenu.add_command(label="重命名", accelerator="Ctrl+R", command=rename_file)
filemenu.add_command(label="删除", accelerator="Ctrl+D", command=delete)

# 编辑功能
editmenu = Menu(top)
menubar.add_cascade(label="编辑", menu=editmenu)
editmenu.add_command(label="撤销", accelerator="Ctrl+Z", command=undo)
editmenu.add_command(label="剪切", accelerator="Ctrl+X", command=cut)
editmenu.add_command(label="复制", accelerator="Ctrl+C", command=copy)
editmenu.add_command(label="粘贴", accelerator="Ctrl+V", command=paste)
editmenu.add_command(label="查找", accelerator="Ctrl+F", command=find)
editmenu.add_command(label="全选", accelerator="Ctrl+A", command=select_all)

# 帮助功能
aboutmenu = Menu(top)
menubar.add_cascade(label="帮助", menu=aboutmenu)
aboutmenu.add_command(label="版权信息", command=power)
aboutmenu.add_command(label="关于记事本", command=help)

top['menu'] = menubar

textPad = Text(top, undo=True)
textPad.pack(expand=YES, fill=BOTH)
scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)

# 热键绑定
textPad.bind("<Control-N>", new_file)
textPad.bind("<Control-n>", new_file)
textPad.bind("<Control-O>", open_file)
textPad.bind("<Control-o>", open_file)
textPad.bind("<Control-S>", save)
textPad.bind("<Control-s>", save)
textPad.bind("<Control-D>", delete)
textPad.bind("<Control-d>", delete)
textPad.bind("<Control-R>", rename_file)
textPad.bind("<Control-r>", rename_file)
textPad.bind("<Control-A>", select_all)
textPad.bind("<Control-a>", select_all)
textPad.bind("<Control-F>", find)
textPad.bind("<Control-f>", find)
textPad.bind("<Button-3>", mypopup)

top.mainloop()






