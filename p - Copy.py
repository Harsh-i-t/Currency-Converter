##########################################
from forex_python.converter import CurrencyRates
c=CurrencyRates()
print(c.get_rates('USD'))
# from forex_python.converter import CurrencyRates
from tkinter import *
import tkinter.messagebox
# from PIL import ImageTk, Image
import time
import datetime

root = Tk()

root.title("CURRENCY CONVERTER")
root.geometry('1350x650') #or 500x500


# image=ImageTk.PhotoImage(Image.open('D:\\Rakshabandhan 2020 Corona Kaal\\currency1.jpeg'))
# img_label=Label(root,image=image,bd=0)
# img_label.pack()

ip1=StringVar(root)
ip2=StringVar(root)

ip1.set('Select')
ip2.set('Select')



width=1350
height=650


Tops=Frame(root,width=width,height=100,bd=8,relief='raise')
Tops.pack(side=TOP)


localtime=time.asctime(time.localtime(time.time()))
lblInfo=Label(Tops,font=('helvetica',50,'bold'),text="CURRENCY CONVERTER",fg="Black",bd=10,anchor='w',bg='yellow')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def RealTimeCurrencyConversion():

    c=CurrencyRates()

    from_currency = ip1.get()
    to_currency = ip2.get()

    if (value.get()==""):
        tkinter.messagebox.showerror('Error','Amount NOT Entered.\n''ENTER AMOUNT')
    elif (from_currency=='Select' or to_currency=='Select'):
        tkinter.messagebox.showerror('Error','Currency NOT selected.\n' 'PLEASE SELECT COUNTRY')    
    else:
        new_amt= c.convert(from_currency,to_currency,float(value.get()))
        new_amount = float("{:.4f}".format(new_amt))
        output.insert(0,str(new_amount))
def showfullform():
    tkinter.messagebox.showerror('FullForm','|EUR - Euro Member Countries \n|IDR - Indonesia Rupiah \n|BGN - Bulgaria Lev \n|ILS - Israel Shekel \n|GBP - UnitedKingdom Pound \n|DKK - Denmark Krone \n|CAD - Canada Dollar \n|JPY - Japan Yen \n|HUF - Hungary Forint \n|RON -Romania New Leu \n|MYR - Malaysia Ringgit \n|SEK - Sweden Krona \n|SGD - Singapore Dollar \n|HKD - Hong KongDollar \n|AUD - Australia Dollar \n 1CHF - Switzerland Franc \n|KRW - Korea (South) Won \n|CNY - China Yuan Renminbi\n|TRY - Turkey Lira \n|HRK - Croatia Kuna \n|NZD - New Zealand Dollar \n|THB - Thailand Baht \n|USD - United StatesDollar \n|NOK - Norway Krone \n|RUB - Russia Ruble \n|INR - India Rupee \n|MXN - Mexico Peso \n|CZK - Czech RepublicKoruna \n|BRL - Brazil Real \n|PLN - Poland Zloty \n|PHP - Philippines Peso \n|ZAR - South Africa Rand')

def clear():
    value.delete(0,END)
    output.delete(0,END)
    ip1.set("Select")
    ip2.set("Select")


def qExit():
    root.destroy()    

CurrencyCode_list ={'GBP': 0.7610620929, 'HKD': 7.7512162942, 'IDR': 14080.003298425, 'ILS': 3.2546384102, 'DKK': 6.137461862, 'INR': 73.7779335367, 'CHF': 0.8894203018, 'MXN': 20.1333388307, 'CZK': 21.7102333636, 'SGD': 1.336934114, 'THB': 30.0948297188, 'HRK': 6.2154696133, 'EUR': 0.8246062505, 'MYR': 4.0515378907, 'NOK': 8.8206481405, 'CNY': 6.5462191803, 'BGN': 1.6127649048, 'PHP': 48.1067040488, 'PLN': 3.657788406, 'ZAR': 15.1261647563, 'CAD': 1.2770677002, 'ISK': 127.6490475798, 'BRL': 5.0670404882, 'RON': 4.0156675188, 'NZD': 1.4100766884, 'TRY': 7.8896676837, 'JPY': 104.1312773151, 'RUB': 73.1733322339, 'KRW': 1092.867155933, 'USD': 1.0, 'AUD': 1.3267914571, 'HUF': 292.5785437454, 'SEK': 8.4571617053}

label1 =  Label(root,font=('Helvetica',15,'bold'), text = 'Amount:  ',bg='yellow', fg = 'black')
label1.place(x=20,y=30)

label2 =  Label(root,font=('Helvetica',15,'bold'), text = 'From:  ',bg='yellow', fg = 'black')
label2.place(x=20,y=120)

label3 =  Label(root,font=('Helvetica',15,'bold'), text = 'To:  ',bg='yellow', fg = 'black')
label3.place(x=20,y=170)

label4 =  Label(root,font=('Helvetica',15,'bold'), text = 'Converted Amount:  ',bg='yellow', fg = 'black')
label4.place(x=20,y=300)


FromCurrency_option = OptionMenu(root, ip1, *CurrencyCode_list)
ToCurrency_option = OptionMenu(root, ip2, *CurrencyCode_list)

FromCurrency_option.place(x=100,y=120)
ToCurrency_option.place(x=100,y=170)

value = Entry(root)
value.place(x=150,y=35)

output = Entry(root)
output.place(x=250,y=305)

value = Entry(root)
value.place(x=150,y=35)

output = Entry(root)
output.place(x=250,y=305)

convert= Button(root,bd=16,fg="black",font=('arial',16,'bold'),width=10,text='Convert',padx=2,command=RealTimeCurrencyConversion)
convert.place(x=200,y=220)

reset = Button(root,bd=16,fg="black",font=('arial',16,'bold'),width=10,text='Reset',padx=2,command=clear)
reset.place(x=208,y=400)

full_form = Button(root,bd=16,fg="black",font=('arial',16,'bold'),width=10,text='FullForms',padx=2,command=showfullform)
full_form.place(x=30,y=500)

Exit=Button(root,padx=6,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit)
Exit.place(x=200,y=500)

root.mainloop()
#############################################


#|EUR - Euro Member Countries |IDR - Indonesia Rupiah |BGN - Bulgaria Lev |ILS - Israel Shekel |GBP - United
#Kingdom Pound |DKK - Denmark Krone |CAD - Canada Dollar |JPY - Japan Yen |HUF - Hungary Forint |RON -
#Romania New Leu |MYR - Malaysia Ringgit |SEK - Sweden Krona |SGD - Singapore Dollar |HKD - Hong Kong
#Dollar |AUD - Australia Dollar |CHF - Switzerland Franc |KRW - Korea (South) Won |CNY - China Yuan Renminbi
#|TRY - Turkey Lira |HRK - Croatia Kuna |NZD - New Zealand Dollar |THB - Thailand Baht |USD - United States
#Dollar |NOK - Norway Krone |RUB - Russia Ruble |INR - India Rupee |MXN - Mexico Peso |CZK - Czech Republic
#Koruna |BRL - Brazil Real |PLN - Poland Zloty |PHP - Philippines Peso |ZAR - South Africa Rand

#1) auto reset of converted amount
#2) heading with time and date
#3) box sizes and arrangement

###############################################
