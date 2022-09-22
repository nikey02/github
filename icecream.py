from tkinter import *
import random
import time;
import datetime
import sqlite3 as db
def dbcreate():
	conn = db.connect('bill.db')
	cur = conn.cursor()
	cur2 = conn.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS "Quantity"("Bill"	TEXT NOT NULL, "Almond_Chocolate_Coconut"	INTEGER, "Chocolate_Marshmallow"	INTEGER, "Butter_Fudge_Almond"	INTEGER, "Mint_Fudge_Crunch"	INTEGER, "Red_Velvet_Cake_Batter"	INTEGER, "Chocolate_Oreo"	INTEGER, "Boston_Cream_Pie"	INTEGER, "Cake_Batter"	INTEGER, "Blueberry_Cobbler"	INTEGER, "Caramel_Apple"	INTEGER, "Tuxedo_Strawberry"	INTEGER,	"Cinnamon_Bun"	INTEGER,	"Coffee_Cake_Streusel"	INTEGER,	"Cherry_Vanilla"	INTEGER,	"Fudgie_Cheesecake"	INTEGER,	"Lemon_CrÃ¨me"	INTEGER,	PRIMARY KEY("Bill"))')
	cur.close()
	conn.commit()
	cur2.execute('CREATE TABLE IF NOT EXISTS "receipt" ("Bill_id"	TEXT NOT NULL, "date"	TEXT NOT NULL, "cost"	TEXT NOT NULL, PRIMARY KEY("Bill_id"))')
	cur2.close()
	conn.commit()
	conn.close()

dbcreate()
root=Tk()
root.geometry("1350x750+0+0")
root.title("Icecream Shop")
root.configure(background='orange')

Tops=Frame(root, width=1150, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)

f1=Frame(root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)

f2=Frame(root, width=540, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a=Frame(f1, width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)

f2a=Frame(f1, width=900, height=320, bd=6, relief="raise")
f2a.pack(side=BOTTOM)

ft2=Frame(f2, width=440, height=450, bd=12, relief="raise")
ft2.pack(side=TOP)
fb2=Frame(f2, width=440, height=250, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa=Frame(f1a, width=200, height=250,bd=12, relief="raise")
f1aa.pack(side=LEFT)
f1ab=Frame(f1a, width=200, height=250,bd=12, relief="raise")
f1ab.pack(side=RIGHT)

f2aa=Frame(f2a, width=480, height=50, relief="raise")
f2aa.pack(side=LEFT)

f2ab=Frame(f2a, width=480, height=50, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='red')
f1.configure(background='green')
f2.configure(background='red')

lblInfo=Label(Tops, font=('arial',70,'bold'), text= "       ICE-CREAM  PARLOUR     ",bd=5)
lblInfo.grid(row=0,column=0)


#=======================================================================Method============================================================================
def CostofItem():
    Item1=float(E_Almond_Chocolate_Coconut.get())
    Item2=float(E_Chocolate_Marshmallow.get())
    Item3=float(E_Butter_Fudge_Almond.get())
    Item4=float(E_Mint_Fudge_Crunch.get())
    Item5=float(E_Red_Velvet_Cake_Batter.get())
    Item6=float(E_Chocolate_Oreo.get())
    Item7=float(E_Boston_Cream_Pie.get())
    Item8=float(E_Cake_Batter.get())

    Item9=float(E_Blueberry_Cobbler.get())
    Item10=float(E_Caramel_Apple.get())
    Item11=float(E_Tuxedo_Strawberry.get())
    Item12=float(E_Cinnamon_Bun.get())
    Item13=float(E_Coffee_Cake_Streusel.get())
    Item14=float(E_Cherry_Vanilla.get())
    Item15=float(E_Fudgie_Cheesecake.get())
    Item16=float(E_Lemon_Crème.get())

    PriceofIcecream=(Item1 * 150)+(Item2 * 200)+(Item3 * 250)+(Item4 * 300)+(Item5 * 350)+(Item6 * 400)+(Item7 * 450)+(Item8 * 500)
    PriceofFruitIcecream=(Item9 * 150)+(Item10 * 200)+(Item11 * 250)+(Item12 * 300)+(Item13 * 350)+(Item14 * 400)+(Item15 * 450)+(Item16 * 500)

    IcecreamPrice=str('%f'%(PriceofIcecream))
    FruitIcecreamPrice=str('%f'%(PriceofFruitIcecream))
    CostofIcecream.set(IcecreamPrice)
    CostofFruitIcecream.set(FruitIcecreamPrice)
    SC=str('%f'%(14))
    ServiceCharge.set(SC)


    SubTotalofITEMS=str('%f'%(PriceofIcecream + PriceofFruitIcecream + 14))
    SubTotal.set(SubTotalofITEMS)

    Tax=str('%f'%((PriceofIcecream +PriceofFruitIcecream+14)*0.05))
    PaidTax.set(Tax)
    TT=((PriceofIcecream + PriceofFruitIcecream + 14)*0.05)
    TC=str('%f'%(PriceofIcecream + PriceofFruitIcecream + 14 + TT))
    TotalCost.set(TC)


#==================================Receipt=============================
def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10908, 500876)
    randomRef=str(x)
    Receipt_Ref.set("BILL"+ randomRef)


    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+ Receipt_Ref.get()+'\t\t'+ Dateoforder.get()+"\n")
    txtReceipt.insert(END,'Items\t\t\t\t'+ "CostofItems \n\n")
    if var1.get() != 0: txtReceipt.insert(END,'Almond_Chocolate_Coconut:  \t\t\t\t'+ E_Almond_Chocolate_Coconut.get()+ "\n") 
    if var2.get() != 0: txtReceipt.insert(END,'Chocolate_Marshmallow:  \t\t\t\t'+ E_Chocolate_Marshmallow.get()+ "\n") 
    if var3.get() != 0: txtReceipt.insert(END,'Butter_Fudge_Almond:  \t\t\t\t'+ E_Butter_Fudge_Almond.get()+ "\n") 
    if var4.get() != 0: txtReceipt.insert(END,'Mint_Fudge_Crunch:  \t\t\t\t'+ E_Mint_Fudge_Crunch.get()+ "\n") 
    if var5.get() != 0: txtReceipt.insert(END,'Red_Velvet_Cake_Batter:  \t\t\t\t'+ E_Red_Velvet_Cake_Batter.get()+ "\n") 
    if var6.get() != 0: txtReceipt.insert(END,'Chocolate_Oreo:  \t\t\t\t'+ E_Chocolate_Oreo.get()+ "\n") 
    if var7.get() != 0: txtReceipt.insert(END,'Boston_Cream_Pie:  \t\t\t\t'+ E_Boston_Cream_Pie.get()+"\n") 
    if var8.get() != 0: txtReceipt.insert(END,'Cake_Batter:  \t\t\t\t'+ E_Cake_Batter.get()+ "\n") 
    if var9.get() != 0: txtReceipt.insert(END,'Blueberry_Cobbler:  \t\t\t\t'+ E_Blueberry_Cobbler.get()+ "\n") 
    if var10.get() != 0: txtReceipt.insert(END,'Caramel_Apple:  \t\t\t\t'+ E_Caramel_Apple.get()+ "\n") 
    if var11.get() != 0: txtReceipt.insert(END,'Tuxedo_Strawberry:  \t\t\t\t'+ E_Tuxedo_Strawberry.get()+ "\n") 
    if var12.get() != 0: txtReceipt.insert(END,'Cinnamon_Bun:  \t\t\t\t'+ E_Cinnamon_Bun.get() +"\n") 
    if var13.get() != 0: txtReceipt.insert(END,'Coffee_Cake_Streusel:  \t\t\t\t' +E_Coffee_Cake_Streusel.get()+ "\n") 
    if var14.get() != 0: txtReceipt.insert(END,'Cherry_Vanilla:  \t\t\t\t'+ E_Cherry_Vanilla.get() +"\n") 
    if var15.get() != 0: txtReceipt.insert(END,'Fudgie_Cheesecake:  \t\t\t\t'+ E_Fudgie_Cheesecake.get() +"\n") 
    if var16.get() != 0: txtReceipt.insert(END,'Lemon_Crème:  \t\t\t\t'+ E_Lemon_Crème.get() +"\n") 
    txtReceipt.insert(END,'Cost of Icecream: Rs'+ CostofIcecream.get() + '\nTax Paid: Rs' + PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Fruit Icecream:Rs'+ CostofFruitIcecream.get() +'\nSubTotal:' + SubTotal.get()+"\n")
    txtReceipt.insert(END,'Service Charge:Rs'+ ServiceCharge.get() +'\n\n\nTotalCost: Rs' + TotalCost.get()+"\n")
    dbcon(randomRef)

def dbcon(x):
	conn =db.connect('bill.db')
	cur = conn.cursor()
	cur2 = conn.cursor()
	try:
		cur.execute("insert into receipt values('%s','%s','%s')"%(x,Dateoforder.get(), TotalCost.get()))
		cur.close()
		conn.commit()
		tup = (x,var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get(),var10.get(),var11.get(),var12.get(),var13.get(),var14.get(),var15.get(),var16.get())
		cur2.execute("insert into Quantity Values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%tup)
		cur2.close()
		conn.commit()
	finally:
		conn.close()

def qExit():
          qExit=messagebox.askyesno("Quit System","Do you want to quit?")
          if qExit > 0:
              root.destroy()
              return
def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofIcecream.set("")
    CostofFruitIcecream.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)

    E_Almond_Chocolate_Coconut.set("0")
    E_Chocolate_Marshmallow.set("0")
    E_Butter_Fudge_Almond.set("0")
    E_Mint_Fudge_Crunch.set("0")
    E_Red_Velvet_Cake_Batter.set("0")
    E_Chocolate_Oreo.set("0")
    E_Boston_Cream_Pie.set("0")
    E_Cake_Batter.set("0")



    E_Blueberry_Cobbler.set("0")
    E_Caramel_Apple.set("0")
    E_Tuxedo_Strawberry.set("0")
    E_Cinnamon_Bun.set("0")
    E_Coffee_Cake_Streusel.set("0")
    E_Cherry_Vanilla.set("0")
    E_Fudgie_Cheesecake.set("0")
    E_Lemon_Crème.set("0")


    
#========================================================================checkbutton==================================================================
def chkACC():
    if (var1.get() == 1):
        txtAlmond_Chocolate_Coconut.configure(state= NORMAL)
        txtAlmond_Chocolate_Coconut.focus()
        Almond_Chocolate_Coconut.delete('0',END)
        E_Almond_Chocolate_Coconut.set("")
    elif(var1.get() == 0):
        txtAlmond_Chocolate_Coconut.configure(state=DISABLED)
        E_Almond_Chocolate_Coconut.set("0")

def chkCM():        
    if (var2.get() == 1):
       txtChocolate_Marshmallow.configure(state=NORMAL)
       txtChocolate_Marshmallow.focus()
       Chocolate_Marshmallow.delete('0',END)
       E_Chocolate_Marshmallow.set("0")
    elif var2.get() == 0:
        txtChocolate_Marshmallow.configure(state=DISABLED)
        E_Chocolate_Marshmallow.set("0")

        
def chkBFA():         
    if (var3.get() == 1):
       txtButter_Fudge_Almond.configure(state=NORMAL)
       txtButter_Fudge_Almond.focus()
       Butter_Fudge_Almond.delete('0',END)
       E_Butter_Fudge_Almond.set("0")
    elif var3.get() == 0:
        txtButter_Fudge_Almond.configure(state=DISABLED)
        E_Butter_Fudge_Almond.set("0")
         
def chkMFC():       
    if (var4.get() == 1):
       txtMint_Fudge_Crunch.configure(state=NORMAL)
       txtMint_Fudge_Crunch.focus()
       Mint_Fudge_Crunch.delete('0',END)
       E_Mint_Fudge_Crunch.set("0")
    elif var4.get() == 0:
        txtMint_Fudge_Crunch.configure(state=DISABLED)
        E_Mint_Fudge_Crunch.set("0")

        
def chkRVCB():        
    if (var5.get() == 1):
        txtRed_Velvet_Cake_Batter.configure(state=NORMAL)
        txtRed_Velvet_Cake_Batter.focus()
        Red_Velvet_Cake_Batter.delete('0',END)
        E_Red_Velvet_Cake_Batter.set("0")
    elif var5.get() == 0:
        txtRed_Velvet_Cake_Batter.configure(state=DISABLED)
        E_Red_Velvet_Cake_Batter.set("0")

        
def chkCO():
    if (var6.get() == 1):
        txtChocolate_Oreo.configure(state=NORMAL)
        txtChocolate_Oreo.focus()
        Chocolate_Oreo.delete('0',END)
        E_Chocolate_Oreo.set("0")
    elif var6.get() == 0:
        txtChocolate_Oreo.configure(state=DISABLED)
        E_Chocolate_Oreo.set("0")

        
def chkBCP():    
    if (var7.get() == 1):
        txtBoston_Cream_Pie.configure(state=NORMAL)
        txtBoston_Cream_Pie.focus()
        Boston_Cream_Pie.delete('0',END)
        E_Boston_Cream_Pie.set("0")
    elif var7.get() == 0:
        txtBoston_Cream_Pie.configure(state=DISABLED)
        E_Boston_Cream_Pie.set("0")


        
def chkCB():        
    if (var8.get() == 1):
        txtCake_Batter.configure(state=NORMAL)
        txtCake_Batter.focus()
        Cake_Batter.delete('0',END)
        E_Cake_Batter.set("0")
    elif var8.get() == 0:
        txtCake_Batter.configure(state=DISABLED)
        E_Cake_Batter.set("0")


        
def chkBC():        
    if (var9.get() == 1):
        txtBlueberry_Cobbler.configure(state=NORMAL)
        txtBlueberry_Cobbler.focus()
        Blueberry_Cobbler.delete('0',END)
        E_Blueberry_Cobbler.set("0")
    elif var9.get() == 0:
        txtBlueberry_Cobbler.configure(state=DISABLED)
        E_Blueberry_Cobbler.set("0")


        
def chkCA():         
    if (var10.get() == 1):
        txtCaramel_Apple.configure(state=NORMAL)
        txtCaramel_Apple.focus()
        Caramel_Apple.delete('0',END)
        E_Caramel_Apple.set("0")
    elif var10.get() == 0:
        txtCaramel_Apple.configure(state=DISABLED)
        E_Caramel_Apple.set("0")


        
def chkTS():        
    if (var11.get() == 1):
        txtTuxedo_Strawberry.configure(state=NORMAL)
        txtTuxedo_Strawberry.focus()
        Tuxedo_Strawberry.delete('0',END)
        E_Tuxedo_Strawberry.set("0")
    elif var11.get() == 0:
        txtTuxedo_Strawberry.configure(state=DISABLED)
        E_Tuxedo_Strawberry.set("0")


        
def chkCB():        
    if (var12.get() == 1):
        txtCinnamon_Bun.configure(state=NORMAL)
        txtCinnamon_Bun.focus()
        Cinnamon_Bun.delete('0',END)
        E_Cinnamon_Bun.set("0")
    elif var12.get() == 0:
        txtCinnamon_Bun.configure(state=DISABLED)
        E_Cinnamon_Bun.set("0")


        
def chkCCS():         
    if (var13.get() == 1):
        txtCoffee_Cake_Streusel.configure(state=NORMAL)
        txtCoffee_Cake_Streusel.focus()
        Coffee_Cake_Streusel.delete('0',END)
        E_Coffee_Cake_Streusel.set("0")
    elif var13.get() == 0:
        txtCoffee_Cake_Streusel.configure(state=DISABLED)
        E_Coffee_Cake_Streusel.set("0")


        
def chkCV():        
    if (var14.get() == 1):
        txtCherry_Vanilla.configure(state=NORMAL)
        txtCherry_Vanilla.focus()
        Cherry_Vanilla.delete('0',END)
        E_Cherry_Vanilla.set("0")
    elif var14.get() == 0:
        txtCherry_Vanilla.configure(state=DISABLED)
        E_Cherry_Vanilla.set("0")


        
def chkFC():         
    if (var15.get() == 1):
        txtFudgie_Cheesecake.configure(state=NORMAL)
        txtFudgie_Cheesecake.focus()
        Fudgie_Cheesecake.delete('0',END)
        E_Fudgie_Cheesecake.set("0")
    elif var15.get() == 0:
        txtFudgie_Cheesecake.configure(state=DISABLED)
        E_Fudgie_Cheesecake.set("0")


        
def chkLC():        
    if (var16.get() == 1):
        txtLemon_Crème.configure(state=NORMAL)
        txtLemon_Crème.focus()
        Lemon_Crème.delete('0',END)
        E_Lemon_Crème.set("0")
    elif var16.get() == 0:
        txtLemon_Crème.configure(state=DISABLED)
        E_Lemon_Crème.set("0")
        
#==========================================================================================================================================
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtAlmond_Chocolate_Coconut.configure(state=DISABLED)
    txtChocolate_Marshmallow.configure(state=DISABLED)
    txtButter_Fudge_Almond.configure(state=DISABLED)
    txtMint_Fudge_Crunch.configure(state=DISABLED)
    txtRed_Velvet_Cake_Batter.configure(state=DISABLED)
    txtChocolate_Oreo.configure(state=DISABLED)
    txtBoston_Cream_Pie.configure(state=DISABLED)
    txtCake_Batter.configure(state=DISABLED)
    txtBlueberry_Cobbler.configure(state=DISABLED)
    txtCaramel_Apple.configure(state=DISABLED)
    txtTuxedo_Strawberry.configure(state=DISABLED)
    txtCinnamon_Bun.configure(state=DISABLED)
    txtCoffee_Cake_Streusel.configure(state=DISABLED)
    txtCherry_Vanilla.configure(state=DISABLED)
    txtFudgie_Cheesecake.configure(state=DISABLED)
    txtLemon_Crème.configure(state=DISABLED)



#==========================================================variables======================================================================================================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

Dateoforder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofIcecream=StringVar()
CostofFruitIcecream=StringVar()
ServiceCharge=StringVar()

E_Almond_Chocolate_Coconut=StringVar()
E_Chocolate_Marshmallow=StringVar()
E_Butter_Fudge_Almond=StringVar()
E_Mint_Fudge_Crunch=StringVar()
E_Red_Velvet_Cake_Batter=StringVar()
E_Chocolate_Oreo=StringVar()
E_Boston_Cream_Pie=StringVar()
E_Cake_Batter=StringVar()



E_Blueberry_Cobbler=StringVar()
E_Caramel_Apple=StringVar()
E_Tuxedo_Strawberry=StringVar()
E_Cinnamon_Bun=StringVar()
E_Coffee_Cake_Streusel=StringVar()
E_Cherry_Vanilla=StringVar()
E_Fudgie_Cheesecake=StringVar()
E_Lemon_Crème=StringVar()



E_Almond_Chocolate_Coconut.set("0")
E_Chocolate_Marshmallow.set("0")
E_Butter_Fudge_Almond.set("0")
E_Mint_Fudge_Crunch.set("0")
E_Red_Velvet_Cake_Batter.set("0")
E_Chocolate_Oreo.set("0")
E_Boston_Cream_Pie.set("0")
E_Cake_Batter.set("0")



E_Blueberry_Cobbler.set("0")
E_Caramel_Apple.set("0")
E_Tuxedo_Strawberry.set("0")
E_Cinnamon_Bun.set("0")
E_Coffee_Cake_Streusel.set("0")
E_Cherry_Vanilla.set("0")
E_Fudgie_Cheesecake.set("0")
E_Lemon_Crème.set("0")

Dateoforder.set(time.strftime("%d/%m/%y"))






#==========================================================Icecream===================================================================
Almond_Chocolate_Coconut=Checkbutton(f1aa, text="Almond Chocolate Coconut ", variable = var1, onvalue = 1, offvalue=0,
                                     font=('arial',18,'bold'),command = chkACC).grid(row=0, column=0)
Chocolate_Marshmallow=Checkbutton(f1aa, text="Chocolate Marshmallow ", variable=var2,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkCM).grid(row=1,column=0)
Butter_Fudge_Almond=Checkbutton(f1aa, text="Butter Fudge Almond ", variable=var3,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkBFA).grid(row=2,column=0)
Mint_Fudge_Crunch=Checkbutton(f1aa, text="Mint Fudge Crunch ", variable=var4,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkMFC).grid(row=3,column=0)
Red_Velvet_Cake_Batter=Checkbutton(f1aa, text="Red Velvet Cake Batter ", variable=var5,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkRVCB).grid(row=4,column=0)
Chocolate_Oreo=Checkbutton(f1aa, text=" Chocolate Oreo", variable=var6,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkCO).grid(row=5,column=0)
Boston_Cream_Pie=Checkbutton(f1aa, text="Boston Cream Pie ", variable=var7,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkBCP).grid(row=6,column=0)
Cake_Batter=Checkbutton(f1aa, text="Cake Batter ", variable=var8,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkCB).grid(row=7,column=0)
 

#===============================================================Fruit====================================================
Blueberry_Cobbler=Checkbutton(f1ab, text="Blueberry Cobbler ", variable=var9,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkBC).grid(row=0,column=0)
Caramel_Apple=Checkbutton(f1ab, text="Caramel Apple ", variable=var10,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkCA).grid(row=1,column=0)
Tuxedo_Strawberry=Checkbutton(f1ab, text="Tuxedo Strawberry ", variable=var11,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkTS).grid(row=2,column=0)
Cinnamon_Bun=Checkbutton(f1ab, text="Cinnamon Bun ", variable=var12,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkCB).grid(row=3,column=0)
Coffee_Cake_Streusel=Checkbutton(f1ab, text="Coffee Cake Streusel ", variable=var13,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkCCS).grid(row=4,column=0)
Cherry_Vanilla=Checkbutton(f1ab, text="Cherry Vanilla ", variable=var14,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkCV).grid(row=5,column=0)
Fudgie_Cheesecake=Checkbutton(f1ab, text="Fudgie Cheesecake ", variable=var15,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkFC).grid(row=6,column=0)
Lemon_Crème=Checkbutton(f1ab, text="Lemon Crème ", variable=var16,onvalue=1,offvalue=0,
                                     font=('arial',18,'bold'),command = chkLC).grid(row=7,column=0)



#========================================================weight===================================================================================================
txtAlmond_Chocolate_Coconut = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',state= DISABLED,textvariable=E_Almond_Chocolate_Coconut)
txtAlmond_Chocolate_Coconut.grid(row=0,column=1)
txtChocolate_Marshmallow= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Chocolate_Marshmallow, state= DISABLED)
txtChocolate_Marshmallow.grid(row=1,column=1)
txtButter_Fudge_Almond = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Butter_Fudge_Almond, state= DISABLED)
txtButter_Fudge_Almond.grid(row=2,column=1)
txtMint_Fudge_Crunch = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Mint_Fudge_Crunch, state= DISABLED)
txtMint_Fudge_Crunch.grid(row=3,column=1)
txtRed_Velvet_Cake_Batter = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Red_Velvet_Cake_Batter, state= DISABLED)
txtRed_Velvet_Cake_Batter.grid(row=4,column=1)
txtChocolate_Oreo = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Chocolate_Oreo, state= DISABLED)
txtChocolate_Oreo.grid(row=5,column=1)
txtBoston_Cream_Pie = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Boston_Cream_Pie, state= DISABLED)
txtBoston_Cream_Pie.grid(row=6,column=1)
txtCake_Batter = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Cake_Batter, state= DISABLED)
txtCake_Batter.grid(row=7,column=1)


#======================================================fruit weight=================================================================================================
txtBlueberry_Cobbler = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Blueberry_Cobbler, state= DISABLED)
txtBlueberry_Cobbler.grid(row=0,column=1)
txtCaramel_Apple = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                         justify='left',textvariable=E_Caramel_Apple, state= DISABLED)
txtCaramel_Apple.grid(row=1,column=1)
txtTuxedo_Strawberry = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                             justify='left',textvariable=E_Tuxedo_Strawberry, state= DISABLED)
txtTuxedo_Strawberry.grid(row=2,column=1)
txtCinnamon_Bun = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                        justify='left',textvariable=E_Cinnamon_Bun, state= DISABLED)
txtCinnamon_Bun.grid(row=3,column=1)
txtCoffee_Cake_Streusel = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                                justify='left',textvariable=E_Coffee_Cake_Streusel, state= DISABLED)
txtCoffee_Cake_Streusel.grid(row=4,column=1)
txtCherry_Vanilla = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                          justify='left',textvariable=E_Cherry_Vanilla, state= DISABLED)
txtCherry_Vanilla.grid(row=5,column=1)
txtFudgie_Cheesecake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                             justify='left',textvariable=E_Fudgie_Cheesecake, state= DISABLED)
txtFudgie_Cheesecake.grid(row=6,column=1)
txtLemon_Crème = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                       justify='left',textvariable=E_Lemon_Crème, state=DISABLED)
txtLemon_Crème.grid(row=7,column=1)



#==============================Cost Items ===============================================================================================
lblCostofIcecream = Label(f2aa,font=('arial',12,'bold'), text="Cost of Icecream", bd=8, anchor='w')
lblCostofIcecream.grid(row=2,column=0, sticky=W)
txtCostofIcecream = Entry(f2aa,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left', textvariable=CostofIcecream)
txtCostofIcecream.grid(row=2,column=1)

lblCostofFruitIcecream = Label(f2aa,font=('arial',12,'bold'), text="Cost of Fruit Icecream", bd=8,anchor='w')
lblCostofFruitIcecream.grid(row=3,column=0, sticky=W)
txtCostofFruitIcecream = Entry(f2aa,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left', textvariable=CostofFruitIcecream)
txtCostofFruitIcecream.grid(row=3,column=1)

lblServiceCharge = Label(f2aa,font=('arial',12,'bold'), text="Service Charge", bd=8,anchor='w')
lblServiceCharge.grid(row=4,column=0)
txtServiceCharge = Entry(f2aa,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left',textvariable=ServiceCharge)
txtServiceCharge.grid(row=4,column=1)




#===================================Payment===================================================================================================
lblPaidTax = Label(f2ab,font=('arial',12,'bold'), text="Paid Tax", bd=8)
lblPaidTax.grid(row=2,column=0, sticky=W)
txtPaidTax = Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left', textvariable=PaidTax)
txtPaidTax.grid(row=2,column=1,sticky=W)

lblSubTotal = Label(f2ab,font=('arial',12,'bold'), text="Sub Total", bd=8)
lblSubTotal.grid(row=3,column=0, sticky=W)
txtSubTotal = Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left', textvariable=SubTotal)
txtSubTotal.grid(row=3,column=1,sticky=W)

lblTotalCost= Label(f2ab,font=('arial',12,'bold'), text="Total", bd=8)
lblTotalCost.grid(row=4,column=0, sticky=W)
txtTotalCost= Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left', textvariable= TotalCost)
txtTotalCost.grid(row=4,column=1,sticky=W)

# #==========================================fb2============================================================================
# lblReceipt = Label(ft2,font=('arial',12,'bold'), text="Receipt", bd=2,anchor='w')
# lblReceipt.grid(row=0,column=0,sticky=W)
# txtReceipt = Text(ft2, width=59,height=22,bg="white",bd=8,font=('arial',11,'bold'))
# txtReceipt.grid(row=1,column=0)                      
#===============================Button=========================================================================================================
btnTotal=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text="Total",command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text="Receipt",command=Receipt).grid(row=0,column=1)
btnReset=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text="Reset",command=Reset).grid(row=0,column=2)
btnExit=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text="Exit",command=qExit).grid(row=0,column=3)




root.mainloop()