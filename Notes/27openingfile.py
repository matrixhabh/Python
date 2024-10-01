f = open('myfile.txt') # open file for reading (here r{read} is default)
# Note you've to create a myfile.txt file first
# print(f)
text = f.read() # read the file
print(text)
f.close() # close the file


# Modes in file
# There are various modes in which we can open files.

# read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

# create (x): This mode creates a file and gives an error if the file already exists.

# text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

# binary (b): used to handle binary files (images, pdfs, etc).


# Writing a file

f = open('myfile.txt2', 'w')
f.write('Hello World!')
f.close()
# will create a file named myfile.txt2 and write the text Hello World! in it.


# Appending a file

f = open('myfile.txt3', 'a')
f.write('Hello Again!')
f.close()
# will create a file named myfile.txt3 and write the text Hello Again! in it.   


# The 'with' statement

# Alternatively, you can use the with statement to automatically close the file after you are done with it.

with open('myfile.txt', 'r') as f:
    # ... do something with the file
    # example:
    f.write('Hey I am inside with')



# Updated Module

# Readlines() Method

# The readline method reads a single line from the file.
# If we want to read multiple lines, we can use loop.

# EXAMPLE:
# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

i = 0
while true:
    i = i + 1
    line = f.readline()
    if not line:
        break
    print(line)
    m1 = line.split(',')[0]
    m2 = line.split(',')[1]
    m3 = line.split(',')[2]
    print(f"Marks of student {i} in Maths is {m1}")
    print(f"Marks of student {i} in Science is {m2}")
    print(f"Marks of student {i} in English is {m3}")

    print(line)

# Writelines() Method

# The writeline() method writes a sequence of strings to a file.
# The sequence can be iterate object, such as a list or a tuple.

# Here's an example of how to use writelines() method:

# example:
f = open('myfile.txt', 'w')
lines = ['line1', 'line2', 'line3']
f.writelines(lines)
f.close()

# Keep in mind that the writelines() method does not add a newline character at the end of each line and 
# characters between the strings of sequence.
# If you want to add newlines between the strings, you can use a loop to write each string separately.

#example:
f = open('myfile.txt', 'w')
lines = ['line1', 'line2', 'line3']
for line in lines:
    f.write(line) #or f.write(line + '\n')
    f.write('\n')
f.close()

# Another Upddated Module

# Seek() Function

with open('file.txt', 'r') as f:
    print(type(f))
    # Move to the 10th byte in file
    f.seek(10)
    # To find out how much byte we've moved on to we use
    print(f.tell())
    # Read the next 5 bytes
    data = f.read(5)
    print(data)


# Truncate() Function

# When you open a file in Python using the open function, you can specify the mode in 
# which you want to open the file. If you specify the mode as 'w' or 'a', 
# the file is opened in write mode and you can write to the file. 
# However, if you want to truncate the file to a specific size, you can use the truncate function.

with open('sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(3)

with open('sample.txt', 'r') as f:
  print(f.read())


# Updated Module:-

# Lambda Function
# In python lambda is a small anonymous function without a name
# It is defined using the lambda keyword and has the following syntax:

lambda arguments: expression

# lambda function is often used in situations where a short function is required for a short period of time

# for example-

# def double(x):
#     return x*2   

# # This can also be written as:
double = lambda x: x*2

print(double(5))

# Another example with multiple arguments

avg = lambda x,y,z: (x+y+z)/3
print(avg(2,4,6))

# Without addressing a function method:

def appl(fx, value):
    return 6 + fx(value)

print(appl(lambda x: x*x*x, 2))

def appl(fx, value):
    return 6 + fx(value)

print(appl(lambda x: x*x*x, 2))
