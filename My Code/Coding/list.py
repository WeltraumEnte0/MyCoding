
def hellolist():
    thislist = ["apple", "banana", "cherry"]
    if "apple" in thislist:
        print("Yes, 'apple' is in the fruits list") 
    thislist[1] = "horst"
    print(thislist)

def mylist():
  listone = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
  print(listone)
  listone[1:3] = ["blackcurrant", "watermelon"]
  print(listone)


#hellolist()
#mylist()

def list():
  thislist = ["apple", "banana", "cherry"]
  thislist[1:2] = ["blackcurrant", "watermelon"]
  print(thislist)

#list()


#inserting without removing items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append elements from another list to current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove first occurance of an item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#remove an index (index() removes the last one)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#clear whole list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#fruits with letter a copy in new list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)