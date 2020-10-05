### SRC - Can you check your indentation? It should be 4 or 2, not 8!

def multiples(table,start,end,name):
	print("Hi,",name,"Here is your times table:")
	for i in range(start,end+1,table):
                ### SRC - I don't think you want to return here, but print
		### return(start,"x",end,"=",i)
		print(start,"x",end,"=",i)

### SRC you seem to have missed the input statements here?	
pupilName = input("What is your name?")
### SRC - you can't use the comma's in an input statement...
startNum = int(input("Hello," + pupilName + "What is the starting number for your times table?"))
endNum = int(input("And the end number?"))
table = int(input("And what table would you like?"))

### SRC - unless your subroutine muliples returns a string, you don't want to print it!!

### print(multiples(table,startNum,endNum,pupilName))
multiples(table,startNum,endNum,pupilName)
