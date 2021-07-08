s1=int(input("Enter first side of triangle"))
s2=int(input("Enter second side of triangle"))
s3=int(input("Enter third side of triangle"))

if s1==s2 and s2 == s3:
     print("Equilateral triangle")
elif (s1==s2 and s2!=s3) or (s2==s3 and s2!=s1) or (s1==s3 and s1!=s2):
     print("Isosceles Triangle")
elif s1!=s2 and s1!=s3 and s2!=s3:
     print("Scalene Triangle")