course = 'Python for Beginners'
print(len(course)) #We can use built in function name called "len()" . This function is used to find the number of characters in a string.
#Dot operators.
course.upper()#Variable continued by dot-upper(.upper) will change the value to upper case.
print(course.upper())
course.lower()#Variable continued by dot-lower(.lower) will change the value to lower case.
print(course.lower())
course.find('P')#Variable continued by dot-find and in brackests we should write the character which you want to find(.find('P')) will find the character and give the number where the character is stored.
print(course.find('P'))
course.find('p')# if you enter lower case it will check for the lower case letter which you have entered if the lower case wariable is not theair it will Give negitive number.
print(course.find('p'))
course.find('Beginners')#We can also pass sequance of characters
print(course.find('Beginners'))
course.replace('Beginners','Absolute Beginners')#Variable continued by dot-replace(.replace) will replace the word/letters.
print(course.replace('Beginners','Absolute Beginners'))
course.replace('P','J')#We can replace word.
print(course.replace('P','J'))
#if you want to check the exestince of a character or sequence of characters in string then we will use "in" operator.
print('Python' in course)#it will returs as boolin value.
print('python' in course)#This line give false because the letter p is in lower-case.
print(course.title())#title will print as it is.
