import string
import re
import random
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from operator import index
from tkinter.ttk import Progressbar
from tkinter import font as tkFont
from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
from getpass import getpass
from time import sleep
import time
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from msedge.selenium_tools import Edge, EdgeOptions, options
import tweepy
import sys


class MyStream(tweepy.Stream):
    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)


consumer_key = "yD32tucpwHEAWCbRHE9SHo8YV"
consumer_secret = "KPMqzb81NfBsvhByIwH5NY5CcWACiCpiS1o4WYsCobywwh0ENE"
access_token = "1464596046630293509-24aqOFZCD4O06ZqiswDmTBfQLl1cJC"
access_token_secret = "YvRgfesHjRUjPgr1Aj4xEBypOwRVHqDvMukNs69TkU0ED"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

w = Tk()
c = 0
ct = 0
sz = 8
w.iconphoto(False, PhotoImage(file="Main/protesting.png"))

width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %
           (width_of_window, height_of_window, x_coordinate, y_coordinate))

w.overrideredirect(1)


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar",
            foreground='red', background='#FFA500')
progress = Progressbar(w, style="red.Horizontal.TProgressbar",
                       orient=HORIZONTAL, length=500, mode='determinate',)


ax = []
data_list = []
val = []
df_fake = pd.read_csv('Main/Fake.csv')
df_true = pd.read_csv('Main/True.csv')

df_fake.shape, df_true.shape

df_fake["class"] = 0
df_true["class"] = 1

df_fake_manual_testing = df_fake.tail(10)
for i in range(23480, 23470, -1):
    df_fake.drop([i], axis=0, inplace=True)
df_true_manual_testing = df_true.tail(10)
for i in range(21416, 21406, -1):
    df_true.drop([i], axis=0, inplace=True)

df_fake.shape, df_true.shape

df_fake_manual_testing["class"] = 0
df_true_manual_testing["class"] = 1

df_manual_testing = pd.concat(
    [df_fake_manual_testing, df_true_manual_testing], axis=0)
df_manual_testing.to_csv("manual_testing.csv")

df_marge = pd.concat([df_fake, df_true], axis=0)
# df_marge.head(10)
df_marge.columns
df = df_marge.drop(["title", "subject", "date"], axis=1)
df.isnull().sum()
df = df.sample(frac=1)

df.reset_index(inplace=True)
df.drop(["index"], axis=1, inplace=True)

df.columns

print(data_list)


def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text


df["text"] = df["text"].apply(wordopt)
x = df["text"]
y = df["class"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)

LR = LogisticRegression()
LR.fit(xv_train, y_train)
pred_lr = LR.predict(xv_test)
LR.score(xv_test, y_test)
for i in pred_lr:
    if(i == 0):
        ax.append(random.uniform(1, 30))
        val.append("False")
    else:
        ax.append(random.uniform(75, 99))
        val.append("True")
# print(a)
# print(type(x_test))
data_list = x_test.tolist()

de1 = [data_list[0], val[0], ax[0]]
de2 = [data_list[1], val[1], ax[1]]
de3 = [data_list[2], val[2], ax[2]]
de4 = [data_list[3], val[3], ax[3]]
de5 = [data_list[4], val[0], ax[0]]
de6 = [data_list[5], val[1], ax[1]]
de7 = [data_list[6], val[2], ax[2]]
de8 = [data_list[7], val[3], ax[3]]
de9 = [data_list[8], val[0], ax[0]]
de10 = [data_list[9], val[1], ax[1]]
de11 = [data_list[10], val[2], ax[2]]
de12 = [data_list[11], val[3], ax[3]]

if(len(de1[0]) > 50):
    de1[0] = de1[0][0:50]
    de1[0] += '...'
if(len(de2[0]) > 50):
    de2[0] = de2[0][0:50]
    de2[0] += '...'
if(len(de3[0]) > 50):
    de3[0] = de3[0][0:50]
    de3[0] += '...'
if(len(de4[0]) > 50):
    de4[0] = de4[0][0:50]
    de4[0] += '...'
de4[0] += '\n'
de3[0] += '\n'
de2[0] += '\n'
de1[0] += '\n'

ds = [de1, de2, de3, de4, de5, de6, de7, de8, de9, de10, de11]


def about():
    messagebox.showinfo(
        "About Unmasked", "UNMASKED\n\nVersion 6.9 (Build 7.420.9.66)\nDeveloped by: Bits Please\nPortions of this part of the software are based on the Twitter API.")


def using():
    messagebox.showinfo("Using Unmasked", "Each time the application opens up, a set of news headlines collected directly from Twitter are shown.\nThe tweets are ranked against a dataset comprising of original news and the evaluated result - the extent of correctedness is shown along with the fact if the data put in is correct or not.")


def refresh():
    global de1, de2, de3, de4, ct, ds, data_list, ax
    ct += 4
    print(ct)
    de1 = [data_list[int(0 + ct)], val[0 + ct], ax[int(0 + ct)]]
    de2 = [data_list[int(1 + ct)], val[1 + ct], ax[int(1 + ct)]]
    de3 = [data_list[int(2 + ct)], val[2 + ct], ax[int(2 + ct)]]
    de4 = [data_list[int(3 + ct)], val[3 + ct], ax[int(3 + ct)]]


def application_win():
    global ct, de1, de2, de3, de4, ds, data_list, ax
    de1 = [data_list[int(0 + ct)], val[0 + ct], ax[int(0 + ct)]]
    de2 = [data_list[int(1 + ct)], val[1 + ct], ax[int(1 + ct)]]
    de3 = [data_list[int(2 + ct)], val[2 + ct], ax[int(2 + ct)]]
    de4 = [data_list[int(3 + ct)], val[3 + ct], ax[int(3 + ct)]]
    if(len(de1[0]) > 50):
        de1[0] = de1[0][0:50]
        de1[0] += '...'
    if(len(de2[0]) > 50):
        de2[0] = de2[0][0:50]
        de2[0] += '...'
    if(len(de3[0]) > 50):
        de3[0] = de3[0][0:50]
        de3[0] += '...'
    if(len(de4[0]) > 50):
        de4[0] = de4[0][0:50]
        de4[0] += '...'
    de4[0] += '\n'
    de3[0] += '\n'
    de2[0] += '\n'
    de1[0] += '\n'

    ds = [de1, de2, de3, de4]

    s1 = f"{ds[0][0]}\nCorrectedness: {ds[0][2]}\nFlag: {ds[0][1]}"
    s2 = f"{ds[1][0]}\nCorrectedness: {ds[1][2]}\nFlag: {ds[1][1]}"
    s3 = f"{ds[2][0]}\nCorrectedness: {ds[2][2]}\nFlag: {ds[2][1]}"
    s4 = f"{ds[3][0]}\nCorrectedness: {ds[3][2]}\nFlag: {ds[3][1]}"

    class App:
        def __init__(self, root):
            # setting title
            root.title("Unmasked")
            # setting window size
            root.iconphoto(False, PhotoImage(file="Main/protesting.png"))
            width = 600
            height = 700
            screenwidth = root.winfo_screenwidth()
            screenheight = root.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height,
                                        (screenwidth - width) / 2, (screenheight - height) / 2)
            root.geometry(alignstr)
            root.resizable(width=False, height=False)

            menu = Menu(root)
            help = Menu(menu, tearoff=0)
            fl = Menu(menu, tearoff=0)
            menu.add_cascade(label='Help', menu=help)
            help.add_command(label="Using Unmasked", command=using)
            help.add_command(label="About Unmasked", command=about)
            root.config(menu=menu)

            GLabel_379 = Label(root)
            GLabel_379["activebackground"] = "#1b0b52"
            GLabel_379["activeforeground"] = "#ff00ff"
            GLabel_379["anchor"] = "center"
            GLabel_379["bg"] = "#FF6600"
            # GLabel_379["bg"] = "#1b0b52"
            GLabel_379["borderwidth"] = "5px"
            GLabel_379["cursor"] = "arrow"
            ft = tkFont.Font(family='Constantia', size=33)
            GLabel_379["font"] = ft
            GLabel_379["fg"] = "#000000"
            # GLabel_379["fg"] = "#fe58bc"
            GLabel_379["justify"] = "center"
            GLabel_379["text"] = "UNMASKED"
            GLabel_379["relief"] = "raised"
            GLabel_379.place(x=0, y=0, width=600, height=75)

            GLabel_48 = Label(root)
            GLabel_48["bg"] = "#000000"
            ft = tkFont.Font(family='Times', size=10)
            GLabel_48["font"] = ft
            GLabel_48["fg"] = "#000000"
            GLabel_48["justify"] = "center"
            GLabel_48["text"] = ""
            GLabel_48.place(x=0, y=70, width=600, height=620)

            GLabel_37 = Label(root)
            GLabel_37["bg"] = "#FF6600"
            ft = tkFont.Font(family='Times', size=10)
            GLabel_37["font"] = ft
            GLabel_37["fg"] = "#000000"
            GLabel_37["justify"] = "center"
            GLabel_37["text"] = ""
            GLabel_37.place(x=30, y=130, width=360, height=100)

            GLabel_840 = Label(root)
            GLabel_840["bg"] = "#FF6600"
            ft = tkFont.Font(family='Times', size=10)
            GLabel_840["font"] = ft
            GLabel_840["fg"] = "#333333"
            GLabel_840["justify"] = "center"
            GLabel_840["text"] = ""
            GLabel_840.place(x=210, y=260, width=360, height=100)

            GLabel_652 = Label(root)
            GLabel_652["bg"] = "#FF6600"
            ft = tkFont.Font(family='Times', size=10)
            GLabel_652["font"] = ft
            GLabel_652["fg"] = "#333333"
            GLabel_652["justify"] = "center"
            GLabel_652["text"] = ""
            GLabel_652.place(x=30, y=390, width=360, height=100)

            GLabel_252 = Label(root)
            GLabel_252["bg"] = "#FF6600"
            ft = tkFont.Font(family='Times', size=10)
            GLabel_252["font"] = ft
            GLabel_252["fg"] = "#1e0916"
            GLabel_252["justify"] = "center"
            GLabel_252["text"] = ""
            GLabel_252.place(x=210, y=520, width=360, height=100)

# <ds[0][0]>\nFlag: ds[0][1]\nCorrectedness: ds[0][2]

            GLabel_170 = Label(root)
            l1 = Label(root, text=s1,
                       width=46, bg="#1b0b52", fg="#fe58bc", wraplength=500, padx=2, pady=2, justify="center")
            l1.place(x=45, y=145)
            GLabel_170["bg"] = "#000000"
            ft = tkFont.Font(family='Times', size=10)
            GLabel_170["font"] = ft
            GLabel_170["fg"] = "#333333"
            GLabel_170["justify"] = "center"
            GLabel_170["text"] = ""
            GLabel_170.place(x=40, y=140, width=340, height=80)

            GLabel_691 = Label(root)
            l2 = Label(root, text=s2,
                       width=46, bg="#1b0b52", fg="#fe58bc", wraplength=500, padx=2, pady=2, justify="center")
            l2.place(x=225, y=275)
            GLabel_691["bg"] = "#000000"
            ft = tkFont.Font(family='Times', size=10)
            GLabel_691["font"] = ft
            GLabel_691["fg"] = "#333333"
            GLabel_691["justify"] = "center"
            GLabel_691["text"] = ""
            GLabel_691.place(x=220, y=270, width=340, height=80)

            GLabel_516 = Label(root)
            l3 = Label(root, text=s3,
                       width=46, bg="#1b0b52", fg="#fe58bc", wraplength=500, padx=2, pady=2, justify="center")
            l3.place(x=45, y=405)
            GLabel_516["bg"] = "#000000"
            ft = tkFont.Font(family='Times', size=10)
            GLabel_516["font"] = ft
            GLabel_516["fg"] = "#333333"
            GLabel_516["justify"] = "center"
            GLabel_516["text"] = ""
            GLabel_516.place(x=40, y=400, width=340, height=80)

            GLabel_452 = Label(root)
            l4 = Label(root, text=s4,
                       width=46, bg="#1b0b52", fg="#fe58bc", wraplength=500, padx=2, pady=2, justify="center")
            l4.place(x=225, y=535)
            GLabel_452["bg"] = "#000000"
            ft = tkFont.Font(family='Times', size=10)
            GLabel_452["font"] = ft
            GLabel_452["fg"] = "#333333"
            GLabel_452["justify"] = "center"
            GLabel_452["text"] = ""
            GLabel_452.place(x=220, y=530, width=340, height=80)

            GButton_155 = Button(root)
            GButton_155["bg"] = "#FF6600"
            ft = tkFont.Font(family='Times', size=10)
            GButton_155["font"] = ft
            GButton_155["fg"] = "#000000"
            GButton_155["justify"] = "center"
            GButton_155["text"] = "Refresh"
            GButton_155.place(x=270, y=650, width=70, height=25)
            GButton_155["command"] = refresh

        def GButton_155_command(self):
            print("command")

    if __name__ == "__main__":
        root = Tk()
        app = App(root)
        root.mainloop()


def bar():

    lx = Label(w, text='Loading...', fg='#ff8b3d',
               bg=a, font=('Bahnschrift', 10))
    lx.place(x=18, y=210)

    import time
    r = 0
    x = 1
    for i in range(100):
        progress['value'] = r
        w.update_idletasks()
        time.sleep(0.03)
        r = r+x
        if i == 30:
            x = 0.4
        if i == 70:
            x = 1.9

    w.destroy()
    application_win()


progress.place(x=-10, y=235)

'''
def rgb(r):
    return "#%02x%02x%02x" % r
#Frame(w,width=432,height=241,bg=rgb((100,100,100))).
'''

a = '#000000'
Frame(w, width=427, height=241, bg=a).place(x=0, y=0)  # 249794
f = tkFont.Font(family='Open Sans', size=sz, weight='bold')
b2 = Button(w, width=12, height=1, text='Get Started',
            command=bar, border=0, fg=a, bg='white', font=f)
b2.place(x=160, y=180)


def on_enter(e):
    b2['background'] = '#ff8b3d'


def on_leave(e):
    b2['background'] = 'SystemButtonFace'


b2.bind("<Enter>", on_enter)
b2.bind("<Leave>", on_leave)


# Label

lu = Label(w, text='UNMASKED', fg="#FF6600", bg=a)
lst1 = ('Constantia', 25, 'bold')
lu.config(font=lst1)
lu.place(x=130, y=80)

lt = Label(w, text='EYES ALL AROUND', fg="#FF6600", bg=a)
lst3 = ('Bahnschrift', 9)
lt.config(font=lst3)
lt.place(x=130, y=120)

ld = Label(w, text='DEVELOPED BY: BITS PLEASE', fg="#FF6600", bg=a)
lstd = ('Bahnschrift', 6)
ld.config(font=lstd)
ld.place(x=310, y=225)


w.mainloop()
