#Say "Hello, World!" With Python
print("Hello, World!")


#Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())

if (n % 2) == 0 and (n < 5 or n > 20) :
    print("Not Weird")
else :
    print("Weird")


#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
c = a + b
d = a - b
e = a * b

print(c)
print(d)
print(e)


#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())

if b == 0 :
    print("Not valid input")
else:
    intero = a // b
    fraz = a / b
    print(intero,"\n",fraz)
    
#Loops
if __name__ == '__main__':
    n = int(input())
    
for i in range(0,n) :
    print(i**2)


#Write a function
def is_leap(year):
    leap = False
    
    if (year % 100 == 0 and year % 400 == 0):
        leap = True
    elif (year % 100 != 0 and year % 4 == 0):
        leap = True
    return leap


#Print Function
if __name__ == '__main__':
    n = int(input())

stringone=""
for i in range(1,n+1):
    stringone += str(i)
    
print(stringone)


#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())



perm = [[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if (i+j+k) != n]

print(perm)


#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

scores = set(arr)
lista = list(scores) 
lista.sort()   
print(lista[-2])


#Nested Lists
if __name__ == '__main__':
    lista1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista1.append([name,score])

studenti = []
voti = set()
for i in range(len(lista1)) :
    voti.add(lista1[i][1])

voti = list(voti)
voti.sort()
bound = voti[1]

for i in range(len(lista1)) :
    if lista1[i][1] == bound :
        studenti.append(lista1[i][0])
studenti.sort()        
for stud in studenti:
    print(stud)


#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
marks = []
for key, value in student_marks.items():
     if key == query_name :
        marks = value
avg = sum(marks)/len(marks)

print("%.2f" %avg)


#Lists
if __name__ == '__main__':
    N = int(input())
result = []    
for i in range(N):
    instr = input().split()
    if instr[0] == "insert":
        result.insert(int(instr[1]), int(instr[2])) 
    elif instr[0] == "remove":
        result.remove(int(instr[1]))
    elif instr[0] == "sort":
        result.sort() 
    elif instr[0] == "append":
        result.append(int(instr[1]))
    elif instr[0] == "pop":
        result.pop()
    elif instr[0] == "reverse":
        result.reverse()    
    else:
        print(result)
     

#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

integer_list = tuple(integer_list)
print(hash(integer_list))


#sWAP cASE
def swap_case(s):
    s2 = ""
    for i in range(len(s)):
        if s[i].isupper():
            s2 += s[i].lower()
        else :
            s2 += s[i].upper()
    s = s2
    return s
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result


#String Split and Join
def split_and_join(line):
    line = line.split()
    line = "-".join(line)
    return line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


#Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i + len(sub_string)] == sub_string :
            count += 1
        else :
            continue
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    

#What's Your Name?
def print_full_name(firstname, lastname):
    print("Hello", firstname, lastname+ "! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
 
#Mutations
def mutate_string(string, position, character):
    position = int(position)
    string = string[:position] + character + string[(position+1):]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    

#String Validators
if __name__ == '__main__':
    s = input()
    
rows = [False] * 5  

for i in range(len(s)):
    if s[i].isalnum():
        rows[0] = True
    if s[i].isalpha():
        rows[1] = True
    if s[i].isdigit():
        rows[2] = True
    if s[i].islower():
        rows[3] = True
    if s[i].isupper():
        rows[4] = True
    else:
        continue
    
for elem in rows:
    print(elem)


#Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    

#Text Wrap
import textwrap

def wrap(string, max_width):
    text = ""
    cont = 1
    for i in range(0,len(string)):
        if cont == max_width:
            text += string[i]+"\n"
            cont = 1
        else:
            text += string[i]
            cont += 1
    return text        
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


#Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

#upper triangle
for i in range((n-1)//2):
    sy = ".|." * ((i*2)+1)
    print(sy.center(m,"-"))

print("WELCOME".center(m,"-"))
    
#lower trinagle
for i in range(((n-1)//2)-1, -1, -1):
    sy = ".|." * ((i*2)+1)
    print(sy.center(m,"-"))


#String Formatting
def print_formatted(number):
    width = number.bit_length()
    for i in range(number):
        print(f'{i+1:{width}d} {i+1:{width}o} {i+1:{width}X} {i+1:{width}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
   
   
#Alphabet Rangoli
import string

def print_rangoli(size):
    
    width = (((size*2)-1)*2)-1
    
    #initializing the alphabet using the string module
    alph = string.ascii_lowercase
    
    #fixing the error with size=1
    if size == 1:
        print(alph[0])
    else:
        #upper part of the rhombus
        for i in range(size-1, -1, -1):
            #create the letters for each row of the rangoli
            lett = ""
            for j in range((size-1), (i-1), -1):
                lett += alph[j] + "-"
            
            #add the reversed string to the letters in order to create a symmetric path
            rev = lett[::-1]
            lett += rev[3:]
            print(lett.center(width,"-"))
            
        #lower part of the rhombus  
        for i in range(size-1):
            #create the letters for each row of the rangoli
            lett = ""
            for j in range((size-1), i, -1):
                lett += alph[j] + "-"
            
            #add the reversed string to the letters in order to create a symmetric path
            rev = lett[::-1]
            lett += rev[3:]
            print(lett.center(width,"-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
    
#Capitalize!
#!/bin/python3

import math
import os
import random
import re
import sys
import re
# Complete the solve function below.
def solve(s):
    s1 = ""
    for i in range(len(s)):
        if s[i] == " ":
            s1 += " "
        elif (s[i].isalpha() and s[i-1] == " ") or i == 0 :
            s1 += s[i].upper()
        else:
            s1 += s[i]
    
    return s1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


#Merge the Tools!
def merge_the_tools(string, k):
    # create the strings
    l = []
    for i in range(0,len(string)-k+1, k):
        l.append(string[i:i+k])
    
    l1 = []

    for i in range(len(l)):
        visited = set()
        newstr = ""
        for j in range(len(l[i])):
            if l[i][j] not in visited:
                newstr += l[i][j]
                visited.add(l[i][j])
        l1.append(newstr)
    for i in l1:
        print(i)    
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    

#collections.Counter()
from collections import Counter, defaultdict
#number of shoes
X = int(input())

#list of all the shoe sizes in the shop
size_list = map(int,input().split())

#num of customers
N = int(input())

#initialize the revenue accumulator
rev = 0

#create the the stock counter dictionary
count = Counter(size_list)

#shoe size and price of the shoe desired by x
for i in range(N):
    size, price = map(int,input().split())
    if count[size] != 0:
        count[size] -= 1
        rev += price

print(rev)


#Introduction to Sets
def average(array):
    array = set(array)
    return round(sum(array)/len(array), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
    
#No Idea!
# dimensions
n, m = map(int, input().split())
# array
arr = map(int, input().split())
# set a 
A = map(int, input().split())
A = set(A)
# set b 
B = map(int, input().split())
B = set(B)

happ = 0
for i in arr:
    if i in A:
        happ += 1
    elif i in B:
        happ -= 1

print(happ)


#Symmetric Difference
m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))

U = M.union(N)
I = M.intersection(N)
sy_diff = U.difference(I)

sy_diff = list(sy_diff)
sy_diff.sort()

for i in sy_diff:
    print(i)


#Set.add()
N = int(input())
countries = set()
for i in range(N):
    countries.add(input())
    
print(len(countries))


#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i  in range(N):
    comm = input().split()
    if comm[0] == "pop":
        s.pop()
    elif comm[0] == "remove":
        s.remove(int(comm[1]))
    elif comm[0] == "discard":
        s.discard(int(comm[1]))
        
print(sum(s))


#Set .union() Operation
n = int(input())
eng_sub = set(map(int, input().split()))
b = int(input())
fre_sub = set(map(int, input().split()))

union = eng_sub.union(fre_sub)
print(len(union))


#Set .intersection() Operation
n = int(input())
eng_sub = set(map(int, input().split()))
b = int(input())
fre_sub = set(map(int, input().split()))

inter = eng_sub.intersection(fre_sub)
print(len(inter))


#Set .difference() Operation
n = int(input())
eng_sub = set(map(int, input().split()))
b = int(input())
fre_sub = set(map(int, input().split()))

diff = eng_sub.difference(fre_sub)
print(len(diff))


#Set .symmetric_difference() Operation
n = int(input())
eng_sub = set(map(int, input().split()))
b = int(input())
fre_sub = set(map(int, input().split()))

sy_diff = eng_sub.symmetric_difference(fre_sub)
print(len(sy_diff))


#Set Mutations
a = int(input())
A = set(map(int, input().split()))

N = int(input())
for i in range(N):
    # take the operation in input
    lista = input().split()
    op = lista[0]
    # construct the new set
    num = int(lista[1])
    new_set = set(map(int, input().split()))
    if op == "update":
        A.update(new_set)
    elif op == "intersection_update":
        A.intersection_update(new_set)    
    elif op == "difference_update":
        A.difference_update(new_set)
    elif op == "symmetric_difference_update":
        A.symmetric_difference_update(new_set)  
    
print(sum(A))


#Check Subset
T = int(input())
for i in range(T):
    n1 = int(input())
    A = set(map(int, input().split())) 
    n2 = int(input())
    B = set(map(int, input().split()))
    if A.intersection(B) == A:
        print(True) 
    else: 
        print(False)


#The Captain's Room
import collections

K = int(input())
bookings = input().split()
counter = collections.Counter(bookings)

print(*[i for i,j in counter.items() if j==1])
       
        
#Check Strict Superset
result = True
A = set(map(int, input().split()))
n = int(input())

for i in range(n):
    B = set(map(int, input().split()))
    if (B.intersection(A) != B) or (len(A) <= len(B)):
        result = False
        break
    
print(result)


#DefaultDict Tutorial
from collections import defaultdict

n, m = map(int,input().split())

dictio = defaultdict(list)
#group A 
for i in range(n):
    dictio["A"].append(input())

#group B
for i in range(m):
    dictio["B"].append(input())

for w in range(len(dictio["B"])):
    if dictio["B"][w] not in dictio["A"]:
        print(-1)
    else:
        for v in range(len(dictio["A"])):
            if dictio["B"][w] == dictio["A"][v]:
                print(v+1, end=" ")
        print()
        
        
#Collections.namedtuple()
from collections import namedtuple, defaultdict

N = int(input())

Student = namedtuple('Student', input().split())
students = []

for i in range(N):
    c1, c2, c3, c4 = input().split()
    students.append(Student(c1, c2, c3, c4))
    
s = 0
for student in students:
    s += int(student.MARKS)
    
print(s / len(students)) 


#Collections.OrderedDict()
from collections import OrderedDict

N = int(input())
ord_dict = OrderedDict()
for i in range(N):
    lista = input().split()
    name = " ".join(lista[:-1])
    price = int(lista[-1])
    try:
        ord_dict[name] += price
    except KeyError:
        ord_dict[name] = price

for i, j in ord_dict.items():
    print(i, j)


#Word Order
from collections import OrderedDict

n = int(input())
ord_dict = OrderedDict()
for i in range(n):
    word = input()
    try:
        ord_dict[word] += 1
    except KeyError:
        ord_dict[word] = 1
    
print(len(ord_dict.keys()))
for i in ord_dict.values():
    print(i, end=" ")
    
    
#Collections.deque()
from collections import deque

dq = deque()
n = int(input())

for i in range(n):
    inp = input().split()
    op = inp[0]
    if len(inp) != 1:
        m = int(inp[1])
        getattr(dq, op)(m)
    else:
        getattr(dq, op)()

for i in dq:
    print(i, end=" ")
    
    
#Company Logo
import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s = input()

counter = Counter(s)

counter = {k: v for k, v in sorted(counter.items(), key=lambda item: (-item[1],item[0]), reverse = False)}

c = 0
for i, j in counter.items():
    if c == 3:
        break
    print(i, j)
    c += 1
    

#Calendar Module
import calendar

days = calendar.day_name
date = list(map(int, input().split()))
day = calendar.weekday(date[2], date[0], date[1])

print(days[day].upper())


#Time Delta
import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    diff = t1 - t2
    seconds = abs(diff.total_seconds())
    return str(int(seconds))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
    

#Exceptions
T = int(input())

for i in range(T):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e1:
        print("Error Code:",e1)
    except ValueError as e2:
        print("Error Code:",e2)


#Zipped!
N, X = map(int, input().split())

marks = []
for i in range(X):
    stdnt_marks = list(map(float, input().split()))
    marks += [stdnt_marks]
    
for i in (zip(*marks)):
    print(sum(i)/len(i))
  
  
#Athlete Sort
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

arr = sorted(arr, key = lambda arr: arr[k] )

for i in arr:
    print(*i)


#ginortS
s = input()
lower = [i for i in s if i.islower()]
upper = [i for i in s if i.isupper()]
digits = [int(i) for i in s if i.isdigit()]

digits.sort()
even = [str(i) for i in digits if i%2==0]
odd = [str(i) for i in digits if str(i) not in even]

lower.sort()
upper.sort()

lower.extend(upper)
lower.extend(odd)
lower.extend(even)

string = "".join(lower)
print(string)


#Map and Lambda Function
cube = lambda x: x**3 

def fibonacci(n):
    l = []
    for i in range(n):
        if i == 0 or i == 1:
            l.append(i)
        else:
            l.append(sum(l[i-2:i]))
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
    
#Detect Floating Point Number
import re

T = int(input())
for i in range(T):
    N = input()
    result = re.match(r"^[+-]?\d*\.\d+$" , N)
    print(bool(result))


#Re.split()
egex_pattern = r"[,.]"
import re
print("\n".join(re.split(regex_pattern, input())))


#Group(), Groups() & Groupdict()
import re

s = input()
char = ""
result = "-1"
for i in s:
    if re.match(r"[a-zA-Z0-9]", i) and (i == char):
        result = i
        break
    else:
        char = i
        
print(result)


#Re.findall() & Re.finditer()
import re

S = input()
result = re.findall(r"(?<=[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])([aeiouAEIOU]{2,})(?=[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])", S)

if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)

#Re.start() & Re.end()
import re

S = input()
k = re.compile(input())

m = k.search(S)

if m == None:
    print((-1, -1))
else:
    while m != None: 
        print((m.start(),m.end()-1))
        m = k.search(S, m.start() + 1)


#Regex Substitution
import re

N = int(input())

for i in range(N):
    line = input()
    sub = re.sub(r"(?<=\s)&&(?=\s)","and",line )
    print(re.sub(r"(?<=\s)\|\|(?=\s)","or",sub ))

    
#Validating Roman Numerals
zero_nine = "(V?I{0,3}|I[XV])"
decine = "(L?X{0,3}|X[LC])"
centinaia = "(D?C{0,3}|C[DM])"
tot = "(M{0,3})" + centinaia + decine + zero_nine + "$"
regex_pattern = rf"{tot}"

import re
print(str(bool(re.match(regex_pattern, input()))))


#Validating phone numbers
import re

N = int(input())
pattern = r"^[7-9]\d{9}$"
for i in range(N):
    s = input()
    if re.search(pattern, s) == None:
        print("NO")
    else:
        print("YES")  
    

#Validating and Parsing Email Addresses
import email.utils
import re

n = int(input())
pattern = r"^<[a-zA-Z][0-9a-zA-z._-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>$"

for i in range(n):
    name, mail = input().split()
    tup = email.utils.parseaddr(f'{name} {mail}')
    if re.fullmatch(pattern, mail) == None:
        continue
    print(email.utils.formataddr(tup))


#Hex Color Code
import re

N = int(input())
pattern = r"[\s,:()](#(?:[0-9A-Fa-f]{3}){1,2})"


for i in range(N):
    line = input()
    result = re.findall(pattern, line)
    if result == []:
        continue
    for i in result:
        print(i)
        
        
#HTML Parser - Part 1
from html.parser import HTMLParser

N = int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

for i in range(N):
    parser.feed(input()) 


#HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data != "\n":
            print(">>> Data")
            print(data)
    def handle_comment(self, data):
        if data != "\n":
            if "\n" in data:
                print(">>> Multi-line Comment")
                print(data)
            else:
                print(">>> Single-line Comment")
                print(data)
    
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


#Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser

N = int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")


parser = MyHTMLParser()

for i in range(N):
    parser.feed(input()) 


#Validating UID
import re

T = int(input())
pattern = r"^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$"

for i in range(T):
    if re.fullmatch(pattern, input()) != None:
        print("Valid")
    else:
        print("Invalid")


#Validating Credit Card Numbers
import re

N = int(input())

patt1 = r'^[4-6](d{15}|\d{3}(-?\d{4}){3})$'
patt2 = r'(\d)-?\1-?\1-?\1'

for i in range(N):
    card = input()
    if (re.fullmatch(patt1, card) != None) and (re.search(patt2, card) == None):
        print("Valid")
    else:
        print("Invalid")


#Validating Postal Codes
regex_integer_in_range = r"^[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(?=(\d).\1)"


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


#Matrix Script
#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
patt = r"(?<=[a-zA-Z0-9])[\W\s]{1,}(?=[a-zA-Z0-9])"
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

result = []
for i in range(m):
    s = ""
    for j in range(n):
        s += matrix[j][i]
    result.append(s)   

solution = re.sub(patt, " ", "".join(result))
print(solution)
        
        
#XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    count = len(node.attrib.values())
    for child in node:
        count += get_attr_number(child)
    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
    
    
#XML2 - Find the Maximum Depth
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    level += 1
    global maxdepth
    if maxdepth < level:
        maxdepth = level
    for child in elem:
        depth(child,level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
    
    
#Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            l[i] = "+91 " + l[i][len(l[i])-10:len(l[i])-5] + " " + l[i][len(l[i])-5:]
        return f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


#Decorators 2 - Name Directory
import operator

def person_lister(f):
    def inner(people):
        for p in people:
            p[2] = int(p[2])
        people.sort(key=operator.itemgetter(2))
        return map(f, people)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
    
    
#Arrays
import numpy

def arrays(arr):
    a = numpy.array(arr, float)
    return numpy.flip(a)
    
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)


#Shape and Reshape
import numpy as np

lista = list(map(int, input().split()))
arr = np.array(lista)
print(np.reshape(arr, (3,3)))


#Transpose and Flatten
import numpy as np

N, M = map(int, input().split())
matrix = []
for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
    
matrix = np.array(matrix)
print(np.transpose(matrix))
print(matrix.flatten())


#Concatenate
import numpy as np

N, M, P = map(int, input().split())

m1 = []
for i in range(N):
    row = list(map(int, input().split()))
    m1.append(row)

m2 = []
for i in range(M):
    row = list(map(int, input().split()))
    m2.append(row)

m1 = np.array(m1)
m2 = np.array(m2)


print(np.concatenate((m1, m2), axis = 0))   


#Zeros and Ones
import numpy as np

dim = tuple(map(int, input().split()))


print(np.zeros(dim,  dtype = np.int))
print(np.ones(dim, dtype = np.int))
    

#Eye and Identity
import numpy as np
np.set_printoptions(legacy='1.13')

m, n = map(int, input().split())

print(np.eye(m, n))


#Array Mathematics
import numpy as np

n, m = map(int, input().split())

   
arr1 = []
for i in range(n):
    arr1.append(input().split())
    
arr2 = []
for i in range(n):
    arr2.append(input().split())

arr1 = np.array(arr1, int)
arr2 = np.array(arr2, int)
print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))  
print(np.multiply(arr1, arr2))
print(np.floor_divide(arr1, arr2))
print(np.mod(arr1, arr2))
print(np.power(arr1, arr2))


#Floor, Ceil and Rint
import numpy as np
np.set_printoptions(legacy='1.13')

arr = np.array(input().split(), float)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))


#Sum and Prod
import numpy as np

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(input().split())
    
arr = np.array(arr, int)

arr = np.sum(arr, axis = 0)
print(np.product(arr))


#Min and Max
import numpy as np

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(input().split())
    
arr = np.array(arr, int)

arr = np.min(arr, axis = 1)
print(np.max(arr))


#Mean, Var, and Std
import numpy as np

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(input().split())
    
arr = np.array(arr, int)

print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
if np.std(arr, axis=None)==0:
    print(np.std(arr, axis=None))
else:
    print(f'{np.std(arr, axis=None):.11f}')


#Dot and Cross
import numpy as np

n = int(input())

a = []
for i in range(n):
    a.append(input().split())
b = []
for i in range(n):
    b.append(input().split())

a = np.array(a, int)
b = np.array(b, int)
print(np.dot(a, b))


#Inner and Outer
import numpy as np

a = np.array(input().split(), int)
b = np.array(input().split(), int)

print(np.inner(a, b))
print(np.outer(a, b))


#Polynomials
import numpy as np

p = list(map(float, input().split()))
x = float(input())

print(np.polyval(p,x))


#Linear Algebra
import numpy as np

n = int(input())
a = []
for i in range(n):
    a.append(input().split())

a = np.array(a, float)

print(round(np.linalg.det(a),2))


#Piling Up!
from collections import deque
import math


t = int(input())
for i in range(t):
    m = int(input())
    block = deque(map(int, input().split()))
    for j in range(m-1):
        if block[0] >= block[1] and block[0] >= block[-1]:
            block.popleft()
        elif block[-1] >= block[-2] and block[-1] >= block[0]:
            block.pop()
    if len(block) < 2:
        print('Yes')
    else:
        print('No')


#Birthday Cake Candles
import math
import os
import random
import re
import sys
from collections import Counter

def birthdayCakeCandles(candles):
    c = Counter(candles)
    return c[max(candles)]
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#Number Line Jumps
import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if ((v1-v2)>0):
        if ((x2-x1)%(v1-v2)==0):
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


#Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

def likesAtDay(n):
    if n==1:
        return 2
    return math.floor((likesAtDay(n-1)*3)/2)

def viralAdvertising(n):
    count = 0
    for i in range(1,n+1):
        count += likesAtDay(i)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


#Insertion Sort - Part 1
import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    k = arr[n-1]
    
    for i in range(n-2,-1,-1):
        if arr[i] < k:
            arr[i+1] = k
            print(*arr)
            break
        else:
            arr[i+1] = arr[i]
        print(*arr)
        if i == 0:
            arr[i+1] = arr[i]
            arr[0] = k
            print(*arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


#Insertion Sort - Part 2
#!/bin/python3
import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            ins = arr[i+1] 
            arr[i+1] = arr[i]
            arr.remove(arr[i])
            for j in range(i+1):  
                if ins < arr[j] or j==i: 
                    arr.insert(j, ins)
                    break
        print(*arr)
            
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


#Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys
def superDigit(n, k):
    if len(str(n)) == 1 and k == 1:
        return int(n)
    else:
        s = sum(list(map(int, n)))
        return superDigit(str(s*k), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
    


#The Minion Game
def real_count(string, sub_str) :
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_str)] == sub_str:
            count += 1
        else : 
            continue
    return count

def minion_game(string):
    s = 0
    k = 0
    s_words = []
    k_words = []
    vowels = "AEIOU"
    for i in range(len(string)) :
        first = string[i]
        for j in range(i,len(string)+1) :
            sub_str = string[i:j]
            if sub_str == "":
                continue
            elif (first in vowels) and (sub_str not in k_words):
                k += real_count(string, sub_str)
                k_words.append(sub_str)
            elif (first not in vowels) and (sub_str not in s_words):
                s += real_count(string, sub_str)
                s_words.append(sub_str)
            else:
                pass
            
    if k > s:
        print("Kevin",k)
    else:
        print("Stuart",s)
        
    return None




if __name__ == '__main__':

