#Create a code that demonstrates object oriented programming by modifying a list. 

#first define the main function 
def main():
    try:
     # Create and print a list named fruit.
     fruit_list = ["pear", "banana", "apple", "mango"]
     print(f"original: {fruit_list}")
     #add code to reverse the list 
     fruit_list.reverse()
     #print it
     print(f"reversed list:{fruit_list}")
     #append orange to the fruit list 
     fruit_list.append("orange")
     #print append list
     print(f"append orange:{fruit_list}")
     #Add code to find where "apple" is located in fruit_list and 
     #insert "cherry" before "apple" in the list and print the list.
     fruit_list.index("apple")
     fruit_list.insert(1,"cherry")
     print(f"Insert cherry:{fruit_list}")
     #Add code to remove "banana" from fruit_list and print the list.
     fruit_list.remove("banana")
     print(f"remove banana{fruit_list}")
     #Add code to pop the last element from fruit_list and 
     #print the popped element and the list.
     fruit_list.pop(-1)
     print(f"popped last:{fruit_list}")
     #Add code to sort and print fruit_list.
     fruit_list.sort()
     print(f"Sorted fruitlist:{fruit_list}")
     #Add code to clear and print fruit_list.
     fruit_list.clear()
     print(f"clear list:{fruit_list}")
    except IndexError as index_err:
        print(type(index_err). __name__,index_err, sep=":")










#call the main function
if __name__=="__main__":
    main()
