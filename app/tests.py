# from django.test import TestCase

# Create your tests here.
with open("F:\\PythonFile\\Recommend\\app\\spider\\data\\feat.txt") as f:
    cont = f.read()
dic = eval(cont)
print(type(dic))
print(dic)