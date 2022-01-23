# writecsv.py

import csv

def writecsv(data):
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)
	print('Success')

# d = ['2022-01-22 22:46:00',50,500]
# writecsv(d)

def readcsv():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file)
		# print(list(fr))
		data = list(fr)
	return data

result = readcsv()
# print(float(result[3][2]) * 10)
# print(result)

sumlist_quan = []
for d in result:
	sumlist_quan.append(float(d[1]))
print(sumlist_quan, sum(sumlist_quan))

sumquan = sum([float(d[1]) for d in result])
print(sumquan)

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

result = sumdata()
print(result)