myDict={
    "pankha": "fan",
    "Dabba":"Box",
    "Vastu": "Item"
}

print("options are ", myDict.keys())

a=input("enter the hindi word:\n")

#print("The meaning of your word is:",myDict[a])

#below line will not throw an error if the key is not present in the Dictionary

print("The meaning of your word is:" , myDict.get(a))


