#list

myBands=["Slayer" , "Metallica" , "Absu"]
print(myBands)
print(type(myBands))
print(myBands[0])
print(myBands[1])
myBands[1]="home"
print ("{} Bands list".format(myBands))

#tuple
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])

#dict

myFavoriteFruitDictionary = {
  "Adam" : "apple",
  "Ben" : "banana",
  "Penny" : "pineapple"
}
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary)
print(myFavoriteFruitDictionary["Adam"])
print(myFavoriteFruitDictionary["Ben"])