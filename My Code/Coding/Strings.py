a = "Die Gedanken sind frei"
print(a[3:])
if "sind" in a:
    print("Yes there is the word")

print(a[:-5])
print(a[-5:])

b = "Hallo meine lieben Joonges"
print(b.upper())
print(b.lower())

c = "       Hello, world!"
print(c.strip())                #removes whitespace before strings


print(b.replace("o", "%"))

d = "Guten Morgen, herzlich wilkommen."
print(d.split(","))

age = 554
txt = "My name is John, and I am {}"
print(txt.format(age))              #formartiert die Zahl age and der Stelle {}
