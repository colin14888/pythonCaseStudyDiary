# -*- coding:utf-8 -*-
from Tkinter import *
from tkFileDialog import *

def newfile():
   txt= text.get(1.0,END)
   if not txt:
       return
   savefile()

def openfile():
    filename = askopenfilename(title='open the file',
                               filetpyes=[('文本文档','*.txt'),
                                          ('ython 文件','*.py')])
    if not filename:
        return

    txt = open(filename).read()
    text.insert(1.0,txt.decode('gbk'))
    root.title(u'%s - Notebook',filename.split('/')[-1])

def savefile():

    filename = asksaveasfilename(title= 'save as...',
                      initialfile = 'untitled.txt',
                      filetypes = [('文本文档','*.text'),
                                 ('python文件','*.py')],
                                 defaultextension = '.txt')
    print filename
    if not filename:
        return
    fn = open(filename,'w')
    fn.write(text.get(1.0,END))
    fn.close()
    text.delete(1.0,END)
    root.title(u'%s - Notebook' % filename.split('/')[-1])

def saveas():
    pass

root = Tk()
#root2 = Tk()
root.title("记事本")
root.geometry("400x300+1000+300")
#菜单
me = Menu()
root.config(menu=me)

filemenu = Menu(me)
filemenu.add_command(label='新建', accelerator= 'Ctrl + N',  command = newfile)
filemenu.add_command(label='open', accelerator= 'Ctrl + S',  command = openfile)
filemenu.add_command(label='save', accelerator= 'Ctrl + S',  command = savefile)
filemenu.add_command(label='save as',  command = saveas)
filemenu.add_separator()
filemenu.add_command(label='页面设置')
filemenu.add_command()


filemenu.add_command(label='exit', command =root.quit)




me.add_cascade(label='文件',menu=filemenu)
#编辑区
text = Text()   #多行文本框 # 可配置颜色, 大小,字体..等
text.pack(expand = YES,fill = BOTH)
root.mainloop()

