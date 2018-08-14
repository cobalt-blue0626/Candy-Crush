file_name=input("Please input the file's name:")
while True:
	if file_name[:11]!="candy_input":
		print("Invalid input.Try again.")
		file_name=input("Please input the file's name:")
	else:
		break
file_name1=file_name+".txt"
file=open(file_name1,"r")
i,data_space,check=0,[],[]
while i<10:
	line1=file.readline()
	if line1=="":
		break
	line2=line1.split("\n")
	line3="".join(line2)
	line4=line3.split(",")
	data_space+=[line4]
	i+=1
i=0
while i<len(data_space):
	print(data_space[i])
	i=i+1
file.close()
file=open(file_name1,"r")
i=0
while i<10:
	line1=file.readline()
	if line1=="":
		break
	line2=line1.split("\n")
	line3="".join(line2)
	line4=line3.split(",")
	check+=[line4]
	i+=1
file.close()
true_false=1
while true_false!=0:
	row_len=len(check[0])
	column_len=len(check)
	row,row1=0,0
	#將符合candy crush遊戲規則的行或列轉為-1
	while row<column_len:
		row1=0
		while row1<(row_len-2):
			if check[row][row1]==check[row][row1+1] and check[row][row1+1]==check[row][row1+2] and check[row][row1]==check[row][row1+2] and check[row][row1+1]!="0":
				data_space[row][row1],data_space[row][row1+1],data_space[row][row1+2]="-1","-1","-1"
			row1=row1+1
		row=row+1
	column=0
	column1=0
	while column<row_len:
		column1=0
		while column1<column_len-2:
			if check[column1][column]==check[column1+1][column] and check[column1+1][column]==check[column1+2][column] and check[column1][column]==check[column1+2][column] and check[column1+1][column]!="0":
				data_space[column1][column],data_space[column1+1][column],data_space[column1+2][column]="-1","-1","-1"
			column1+=1
		column+=1
	data_space=[["0"]*(row_len)]*(column_len)+data_space
	#將元素為-1的位置取代為上面一格元素的值
	x=0
	y=0
	while x<row_len:
		y=column_len
		while y<(column_len*2):
			if data_space[y][x]=="-1":
				rr=0
				while rr<column_len:
					data_space[y-rr][x]=data_space[y-rr-1][x]
					rr=rr+1
			y=y+1
		x=x+1
	data_space=data_space[column_len:]
	file_output=file_name1[:6]+"output"+file_name1[11:]
	out=open(file_output,"w")
	tt=0
	ttt=0
	while tt<column_len:
		if ttt!=0:
			out.write("\n")
		out.write(",".join(data_space[tt]))
		tt+=1
		ttt+=1
	out.close()
	file1=open(file_output,"r")
	i=0
	data_space=[]
	check=[]
	while i<10:
		line1=file1.readline()
		if line1=="":
			break
		line2=line1.split("\n")
		line3="".join(line2)
		line4=line3.split(",")
		data_space+=[line4]
		i+=1
	file1.close()
	file2=open(file_output,"r")
	i=0
	check=[]
	while i<10:
		line1=file2.readline()
		if line1=="":
			break
		line2=line1.split("\n")
		line3="".join(line2)
		line4=line3.split(",")
		check+=[line4]
		i+=1
	file2.close()
	row_len,column_len,row,row1=len(check[0]),len(check),0,0
	#將符合candy crush遊戲規則的行或列轉為-1
	while row<column_len:
		row1=0
		while row1<(row_len-2):
			if check[row][row1]==check[row][row1+1] and check[row][row1+1]==check[row][row1+2] and check[row][row1]==check[row][row1+2] and check[row][row1+1]!="0":
				data_space[row][row1],data_space[row][row1+1],data_space[row][row1+2]="-1","-1","-1"
			row1=row1+1
		row=row+1
	column,column1=0,0
	while column<row_len:
		column1=0
		while column1<column_len-2:
			if check[column1][column]==check[column1+1][column] and check[column1+1][column]==check[column1+2][column] and check[column1][column]==check[column1+2][column] and check[column1+1][column]!="0":
				data_space[column1][column],data_space[column1+1][column],data_space[column1+2][column]="-1","-1","-1"
			column1+=1
		column+=1
	x,y,true_false=0,0,0
	#判斷是否繼續進行消去
	while x<row_len:
		y=0
		while y<column_len:
			if data_space[y][x]=="-1":
				true_false+=1
			else:
				true_false=true_false+0
			y+=1
		x+=1
print("=========================================================================================")
i=0
while i<column_len:
	print(data_space[i])
	i=i+1
