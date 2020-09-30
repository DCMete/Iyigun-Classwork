def multiples(table,start,end,name):
	print("Hi,",name,"Here is your times table:")
	for i in range(start,end+1,table):
		return(start,"x",end,"=",i)
pupilName = ("What is your name?")
startNum = int(("Hello,",pupilName,"What is the starting number for your times table?"))
endNum = int(("And the end number?"))
table = ("And what table would you like?")
print(multiples(table,startNum,endNum,pupilName))
