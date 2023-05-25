# Hey welcome to my repo of python basic quesitonsHey, welcome to my repository of Python basic questions!
# In this repository, you will find various Python programming questions and their solutions. The focus of this particular file is to provide three possible solutions for replacing the values of two variables without introducing any third variable.
# Replacing the values of variables without using a third variable can be a challenging task, but fear not! This file aims to demonstrate different approaches that achieve this goal. By exploring these solutions, you'll enhance your understanding of Python's unique features and gain valuable insights into problem-solving techniques.
# So, let's dive in and explore the world of Python programming! Feel free to experiment, learn, and contribute to this repository. Happy coding!
# Author : Priyanshu Mishra <@priyanshuMishraBackendDev>

a = int(input("Enter your value for a"))
b = int(input("Enter your value for b"))
# First solution 
a,b=b,a
# The line a, b = b, a performs the swapping operation. This is a concise and elegant Python feature that allows you to assign multiple values simultaneously. Here, the values of b and a are swapped in a single line without needing a temporary variable. 
# The right-hand side of the assignment (b, a) creates a tuple (b, a), and then Python automatically unpacks the tuple and assigns the values to a and b, respectively. As a result, the values of a and b are effectively swapped.


# Second solution it has two approach one by dictionary and another one is by array
#Using a dictionary
a = {"a":a,"b":b}
b = a["a"]
a = a["b"] 
# Using an array
a = [a,b]
b = a[0]
a = a[1]