import json
readPath = "C:\\Users\\evmck_jo2z2u\\Documents\\ISU\\Summer19\\Algorithms\\recipe-ingredients-dataset\\train.json"
with open(readPath) as fp:
    book = json.load(fp)

#fill an array with no repeat cuisine categories and then print that arr into txt
if False:
    writePath = open("masterCuisine.txt",'w')  
    midpointArr = []
    for recipe in book:
        cuisine = recipe['cuisine']
        if cuisine not in midpointArr:
            midpointArr.append(cuisine)
    midpointArr.sort()
    for cuisine in midpointArr:
        writePath.write(cuisine+'\n')
    writePath.close()
    

#fill an array with no repeat ingredients and then print that arr into txt
if False:
    writePath = open("masterIngredients.txt",'w')  
    midpointArr = []
    for recipe in book:
        ingredientArr = recipe['ingredients']
        for ingredient in ingredientArr:
            if ingredient not in midpointArr:
                midpointArr.append(ingredient)
    midpointArr.sort()
    for ingredient in midpointArr:
        writePath.write(ingredient+'\n')
    writePath.close()
            
    
    
