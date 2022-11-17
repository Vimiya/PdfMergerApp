from tkinter import *
from app_functions import *


def starting():
    """
    This function will start with creating the menu for Browser and File finder
    """
    writelogs('starting', 'info', 'started with browser menu building')
    root = Tk()
    root.geometry("900x500")
    root.resizable(False, False)
    root.title("PdfMergerApp")

    try:

        label1 = Label(root, text="Please enter the directory path")
        label1.grid(row=0, column=0)
        e1 = Entry(root, width=100, border=5)
        e1.grid(row=0, column=1)
        button1 = Button(root, text='Search', command=lambda: getlist(e2))
        button1.grid(row=1, column=0)
        button2 = Button(root, text='Locate and Merge pdfs', command=lambda: getfile(e3,e4))
        button2.grid(row=1, column=1)
        button3=Button(root,text='Clear All',command=lambda: clearall())
        button3.grid(row=17,column=1)
        label2 = Label(root, text="List of files and Folders in this path: ")
        label2.grid(row=2, column=0)
        label3 = Label(root, text="Available Pdf files in this path: ")
        label3.grid(row=3, column=0)
        sb1 = Scrollbar(root,orient=VERTICAL)
        sb1.grid(row=2,column=2,sticky=NS)
        e2 = Text(root, height=10,width=60)
        e2.grid(row=2, column=1)
        e2.config(yscrollcommand=sb1.set)
        sb1.config(command=e2.yview)

        sb2 = Scrollbar(root,orient=VERTICAL)
        sb2.grid(row=3,column=2,sticky=NS)
        e3=Text(root,height=5,width=60)
        e3.grid(row=3,column=1)
        e3.config(yscrollcommand=sb2.set)
        sb2.config(command=e3.yview)

        e4 = Text(root, height=5, width=40)
        e4.grid(row=10, column=1)

        label4 = Label(root, text="Your Merged pdf path will appear here ")
        label4.grid(row=10, column=0)

    except Exception as e:
        writelogs('start1', 'error', 'Error occurred in module start1')
        writelogs('start1', 'exception', e)

    def getlist(e2):
        """
        This Function calls the getpath function to get the list of directories in
        the given path
        """
        writelogs('getlist', 'info', 'Entered to getlist')
        try:

            lst_dir = getpath(e1.get())
            e2.insert(END, str(lst_dir))
        except Exception as e:
            writelogs('getlist', 'error', 'Error occurred during listing files and directories')
            writelogs('getlist', 'exception', e)

    def getfile(e3, e4):
        """
        This function will call the fetchfile to get the list of pdf files in the given
        path
        """
        writelogs('getfile', 'info', 'entered into getfile')
        try:

            l, filename = fetchfile(e1.get())
            e3.insert(END, str(l))
            e4.insert(END,filename)
        except Exception as e:
            writelogs('getfile', 'error', 'Error occurred during listing .pdf files')
            writelogs('getfile', 'exception', e)

    def clearall():
        e1.delete(0, END)
        e2.delete("1.0","end")
        e3.delete("1.0","end")
        e4.delete("1.0","end")

    root.mainloop()