#4)Find the nth Term of  Arithmetic Sequence
 #  Formula: nth term = a+(n-1)*d
a=int(input("Enter the first number of the Arithmetic Sequence:\n"))
d=int(input("Enter the Common Difference in the series:\n"))
n=int(input("Enter the value of n:\n"))
nth_term = a + (n - 1) * d
print('The nth term is:{}'.format(nth_term))
