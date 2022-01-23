#BasicGUI.py

from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv

def timestamp(thai=True):
	if thai :
		stamp = datetime.now()
		stamp = stamp.replace(year=stamp.year+543)
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else:
		stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	return stamp

def writetext(quantity,total):
	stamp = timestamp()
	filename = 'data.txt'
	with open(filename,'a',encoding='utf-8') as file:
		file.write('\n'+'วัน-เวลา {} ทองคำ: {} สลึง รวมเป็นเงิน {:,.2f} บาท'.format(stamp,quantity,total))

def writecsv(data):
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)
	print('Success')

def readcsv():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file)
		# print(list(fr))
		data = list(fr)
	return data

def sumdata():
	# ใช้สำหรับรวมค่าที่ได้จาก csv สรุปออกมาเป็น 2 ค่า
	result = readcsv()
	sumlist_quan = []
	sumlist_total = []
	for d in result:
		sumlist_quan.append(float(d[1]))
		sumlist_total.append(float(d[2]))
	sumquan = sum(sumlist_quan)
	sumtotal = sum(sumlist_total)

	return (sumquan,sumtotal)

GUI = Tk()
GUI.geometry('500x500')
GUI.title('Doraeboy Program V.0.0.1')

file = PhotoImage(file='gold.png')
IMG = Label(GUI,image=file,text='')
IMG.pack()

L1 = Label(GUI,text='โปรแกรมคำนวณราคาทองคำรูปพรรณ',font=('TH Sarabun New', 25,'bold'),fg='navy')
L1.pack()

L2 = Label(GUI,text='กรุณากรอกจำนวนทองที่จะซื้อ (สลึง)',font=('TH Sarabun New', 18,))
L2.pack()

v_quantity = StringVar() #ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลของช่องกรอก

E1 = ttk.Entry(GUI,textvariable=v_quantity,font=('impact',25))
E1.pack()

def Calculate(event=None): # None คือ ถ้าไม่มีการกดปุ่ม ก็จะไม่ Error ไม่ได้ใช้ Event
	quantity = v_quantity.get()
	price = 7287
	print('จำนวน', float(quantity) * price)
	cal = float(quantity) * price

	data = [timestamp(), quantity, cal]
	writecsv(data)

	# pop up
	title = 'ขอขอบคุณที่ใช้บริการ'
	text = 'ท่านซื้อทองคำรูปพรรณ {} สลึง รวมเป็นเงินทั้งสิ้น {:,.2f} บาท'.format(quantity,cal)
	messagebox.showinfo(title,text)

	v_quantity.set('') # Clear data
	E1.focus() 

B1 = ttk.Button(GUI, text='คำนวณ', command=Calculate)
B1.pack(ipadx=25,ipady=20,pady=20)

# ตรวจสอบการกดปุ่ม Enter
E1.bind('<Return>',Calculate)

# ฟังก์ชั่นการรวมราคาของที่ขายได้
def SummaryData(event):
	sm = sumdata()
	title = 'สรุปยอดรวมทั้งหมด'
	text = 'รวมขายได้ทั้งหมด {} สลึง \nรวมเงินที่ขายได้ทั้งสิ้น {:,.2f} บาท'.format(sm[0],sm[1])
	messagebox.showinfo(title,text)

#ตรวจสอบการกดปุ่ม
GUI.bind('<F1>',SummaryData)
GUI.bind('<F2>',SummaryData)

E1.focus() # ให้ cursor ไปยังตำแหน่งของ E1
GUI.mainloop()