'''learn from Mike via youtube, and book <<(Learn to Program with Python3_Richard_Halterman_in2011)Haltermanpythonbook.pdf>> '''
'''name=input("Please enter your name here: ")
print("Good Morning "+name+" !")
print("Its type: ",type(name))
#draw a picture
print("      *      ")
print("     ***     ")
print("    *****    ")
print("      *      ")
print("      *      ")
print("      *      ")
avogadros_number=6.022e23
c=2.998e8
print("Avogadro's number =",avogadros_number)
print("Speed of light =",c)'''
#caculator
#Chapter 8. More on Functions
#Lists
#List Processing
#Chapter11 Objects
#Custom Types
#Handling Exceptions
#print("This is a test at Ford Motor on Apr 25th 2019 via Ford Talent")
'''
x=0
while x<100:
    try:
        x=int(input("Please enter a small positive integer: "))
        print("x= ",x, " as you just entered.")
        if x<5:
            a=None
            a[3]=2
            print("x= ", x," at this time")  # debugging is needed here
        elif x<10:
            a=[0,1]
            a[2]=3
    print("Program continuous")
print("Program done")'''
'''#definite2.py
n=1
stop=int(input("Please enter a small positive integer: "))
while n<=stop:
    print("n= ",n, " starting from 1 as pre-condition.")
    n+=1'''
#lfFordInterview  Question1
'''thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print("The thisdict is : ",thisdict)
#Question2.
def myFun(arg1, *argv):
    print("The arg1 is ", arg1)
    for myStar_argv in argv:
        print("Other argument(s) in STARargv: ", myStar_argv)
# myFunTest
myFun('thisarg1','Other_argumentOne','Other_argumentTwo','Other_argumentThree')
#Question5
text='geeks for geeks'
print(text.split())
text='geeksTwo,forTwo,geeksTwo'
print(text.split(','))
text='geeksThree:forThree:geeksThree'
print(text.split(':'))
text='geeksFour,  forFour,  geeksFour'
print(text.split(',  '))
word='CatBatSatFatOr'
print([word[i:i+3] for i in range(0,len(word),3)])  #two functions: range(0, len(word),3)  ;len(word)
example='  xoxo love xoxo'
print(example.strip())
print(example.strip(' xoxoe'))
print(example.strip('str'))
example2='android is awesome'
print(example2.strip('an'))
class MyClass:
    def my_first_method(self):
        return self.my_second_method()

    def my_second_method(self):
        return 'Ford'

class MySecondClass(MyClass):
    def my_second_method(self):
        return 'Lincoln'

myclass_object=MyClass()
mysecondclass_object=MySecondClass()

print(myclass_object.my_first_method(),mysecondclass_object.my_first_method())
print(myclass_object.my_second_method(), mysecondclass_object.my_second_method())
#issubclass(myclass_object, mysecondclass_object)
#question8
def string_UPPERlower(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("UPPER Case Letters are: ",d["UPPER_CASE"],",Lower Case Letters are: ",d["LOWER_CASE"])

string_UPPERlower("The Test")
#question11
class Customer:
    pass
myCustomer=Customer()
myCustomer.fn='David'
myCustomer.ln='Kuang'
print("The myCustomer = ",myCustomer.fn,myCustomer.ln)
#question12
cars=['Escape','Edge','Explorer']
car=[i[0].upper() for i in cars]
print(car)
#question13
thislist={"apple","banana","cherry"}
print("Python list :",thislist)
aPythonTuple=("ZeroInTuple","OneInTuple","TwoInTuple")
print("Python tuple:",aPythonTuple)
#question14
cars='{1},{3},{0} and {2}'.format('Escape','Edge','Explorer','Explorer')
print(cars)
#question15
class MyCar():
    __model_name='F150'

car_object=MyCar()
#print the value of class member(_model_name)
print(car_object._MyCar__model_name)
#leetcode_problem1twoSum   Give nums=[2,7,11,15] target=9 return [0,1] because nums0+nums1=> 2+7=>9
nums=[2,7,11,15]
myTarget=9
def two_sum_brute_force(A,target):
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i]+A[j]==target:
                print(A[i],A[j])
                return True
    return False

print(two_sum_brute_force(nums,myTarget))
#DKPython3Solution
nums=[2,7,11,15]
myTarget=9
class DKPython3Solution:
    def two_sum_lfDK(self,A,target):
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                if A[i]+A[j]==target:
                    print(A[i],A[j])
                    return True
        return False

#DKPython3SolutionTest
myDKPython3Solution=DKPython3Solution()
print(myDKPython3Solution.two_sum_lfDK(nums,myTarget))
#somebodyelse
nums=[2,7,11,15]
myTarget=9
class Solution:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

mySolution=Solution()
print(mySolution.twoSum(nums,myTarget))
#somebodyelseTwo
nums=[2,7,11,15]
myTarget=9
class Solution(object):  #with object or without object, it doesn't matter
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

mySolution_with_object=Solution()
print(mySolution_with_object.twoSum(nums,myTarget))
#Leetcode_Problem1033_Move stones until consecutive
theA=1
theB=2
theC=5
class Solution:
    def numMovesStones(self, a, b, c):
        maxi = max(a, b, c) - min(a, b, c) - 2
        mini = max((min(abs(a - b), abs(b - c), abs(a - c), 3) - 1), 1)
        if maxi == 0: mini = 0
        return [mini, maxi]

myS=Solution()
print(myS.numMovesStones(theA,theB,theC))
#right_video_Apr 30th Tue 2019
class Base_Model():
    trim='normal'
    engine_liters=1.5
    miles_range=450
    tank_capacity=45
    color='white'
    transmission='automatic'

    @classmethod
    def miles_per_liter(cls):
        return cls.miles_range / cls.tank_capacity

    @classmethod
    def miles_per_gallon(cls):
        return cls.miles_per_liter()* 3.78541

    def __init__(self,price,transmission='automatic',color='white'):
        self.price=price
        self.transmission=transmission
        self.color=color

    def __str__(self):
        return 'a %s base model with %s transmission ' % (self.color,self.transmission)

myBase_Model=Base_Model(price=25000,transmission='automatic',color='green')
#myBase_Model = Base_Model(color='green',transmission='automatic',price=25000)
print(myBase_Model,myBase_Model.miles_per_gallon())
print(Base_Model,Base_Model.miles_per_gallon())'''
#Leetcode_problem28 Implement strStr
'''myHaystack="watermelon"
myNeedle="a"  
class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

mySolution=Solution()
print("Output: ",mySolution.strStr(myHaystack,myNeedle))
a='Hello'
print(a)
print(a+str(6))
if a== 'HelloElse':
    print('Here a equals to \'Hello\'')
else:
    print('The above condition was NOT true, Else statement')
name="David"
id=9
if name=='Alice':
    print('Alice mode')
if name=='Alice' or name=='Nick':
    print('Mode either Alice or Nick')
if name=="David" and id ==9:
    print('This is David and her id is 9')
print(name.lower())
print(name.upper())
print(name.find('d'))
print(name[2])
print('Hi %s has %d donuts' % ('Matthew',42))
a='Hello'
print(len(a))
print(a[-3:])
x=[1,2,3]
y=[1,2,3]
print(x is y)
print(x==y)
print("python3 on May 28th 2019")
import re
match = re.search('iig','called piiig')
print(match)
print("Try on Jun 10th Mon 2019")
print(str(912))
print("David Kuang working in UofM-Dearborn US since Jun23rd2019...")'''
myHaystack="hallo David Kuang"
myNeedle="ll"
print("myHaystack=",myHaystack)
print("myNeedle=",myNeedle)

