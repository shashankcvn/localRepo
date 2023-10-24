
myDict={"fast": "in a quick manner", "harry": "very faster",
"marks":[55,65,85],
 "anotherDict":{'Harry':'player'}
}


myDict['marks']=[40,70]

#print(myDict['Fast'])

print(myDict['marks'])

#print(myDict['anotherDict']['Harry'])

print(list(myDict.keys()))   #dictionary methods
print(myDict.values())       #dictionary methods#

print(myDict.items())

updateDict={
    "Lovish":"friend"
}

myDict.update(updateDict)

print(myDict)


print(myDict.get("Lovish"))

print(myDict["Lovish"])