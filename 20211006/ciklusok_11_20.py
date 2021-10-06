#11. feladat
"""
for i in range(-30,31,5):
    print(i, end=" ")
"""
#12. feladat
"""
for i in range(3,18):
    if i**2==0:
        print(i, end=" ")
"""
#13. feladat
"""
for i in range(1,17):
    print(pow(2,i), end=" ")
print()
for i in range(1,17):
    print("2 a(z)",i,"hatványon",pow(2,i))
print()
"""
#14. feladat

#17. feladat
"""
a=int(input("Kérek egy pozitív egész számot!"))
osszeg=0
for i in range(1,a+1):
    if a%i==0:
        osszeg+=i
print("A(z)", a, "osztóninak összege", osszeg)
"""