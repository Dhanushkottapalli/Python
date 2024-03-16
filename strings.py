course = 'Python for Beginners'
# course = 'Python's course for Beginners'
#if you want to write "Python's course for Beginners" then it will give you an error.Remove the 2nd line from coment.
course = "Python's course for Beginners" #to avoid the error write the sentence in "".
print(course)
course = 'Python for "Beginners"' #If you want to write Beginners in "" then write whole sentences in ''.
print(course)
course = '''
Hi k.d,

Here is our first email to you.

Thank you.
The support team.
'''                               #if you want to write a paragraph in your program then use ''' '''.
print(course)

course = 'Python for Beginners'
#         0123456789
print(course[0])  #Writing 0 in [] will print first letter of a string.

course = 'Python for Beginners'
#         0123456789
print(course[-1])  #Writing -1 in [] will print last letter of a string.

course = 'Python for Beginners'
#         0123456789
print(course[0:3])  #Writing 0:3 in [] will print letters beetwin 0-3 from a string.

course = 'Python for Beginners'
#         0123456789
print(course[0:])  #Writing 0: in [] will print from 0 to the ending walue of a string.

course = 'Python for Beginners'
#         0123456789
print(course[1:])  #Writing 1: in [] will print from 1 to the ending walue of a string.

course = 'Python for Beginners'
#         0123456789
print(course[:5])  #Writing :5 in [] will take 0 as defalt value and ending value as 5.

course = 'Python for Beginners'
#         0123456789
print(course[:])  #Writing : in [] will take 0 as defalt value and ending value of a string.

course = 'Python for Beginners'
another = course[:] #course[:] will store in "another" veriable.
print(another)


name='Jenniifer'
print(name[1:-1])
#Think what might be the out put?
