cart=["apples", "bananas", 'cheeries']
cart.append("donuts") # adds item to list
cart.append("milk")
cart.append("eggs")
print(cart)
cart.remove("bananas") # removes item (specific value) from list
print(cart)
cart.pop(2) # removes item at indicated index 
print(cart)
cart.pop() # removes item at the last index-- last item, treats like a stack LIFO
print(cart)
cart.append("bananas")
cart.append("bananas")
cart.sort() # orders items in list alphabetically 
print(cart)
cart.reverse() # reverses order of items
print(cart)
cart.reverse()
print(cart.count("bananas")) # count returns number of times item indicated shows up in list

#slicing with lists:
fruit_basket=cart[0:4]
print(fruit_basket)

squares=[]
for i in range(1,5):
    squares.append(i*i)
print(squares)
squares=[x*x for x in range(1,10)]
print(squares)
b_items=[i for i in cart if i.startswith('b')]
print(b_items)

inventory=[0]*10 #create a list fill with default values (10 zeros)
inventory[4]=5
print(inventory)
empty_list=[] #cannot assign value to index ex: empty_list[y]=x ; cannot do

#sets-- cannot change the values, no duplicates, {}
book_genres={"mystery", "science fiction", "fantasy"}
book_genres.add("romance")
print(book_genres)
nums=[1,1,2,2,3,3,4,4,5,5]
unique=set(nums) # gets rid of duplicates
print(unique)

#dictionaries
fav_snacks={"Zoe":"Cheezits", "Kathleen": "chips", "Caroline":"applesauce"}
k_snack=fav_snacks["Zoe"]
print(k_snack)
fav_snacks["Kathleen"]="tortilla chips"
for key in fav_snacks:
    print(key, fav_snacks[key])
for person, snack in fav_snacks.items():
    print(person, snack)
if "Jack" in fav_snacks:
    print(fav_snacks["Jack"])
else:
    fav_snacks["Jack"]="popcorn"
print(fav_snacks)