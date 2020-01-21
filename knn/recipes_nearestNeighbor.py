###Classification Machine Learning
##given ingredients show recipes that will use most similar ingredients
##nearest neighbors using jaccard index to calculate a distance
k=5
def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 
def union(lst1, lst2): 
    return list(set(lst1) | set(lst2))  
def jaccardIndex(lst1,lst2):
    #fix variations by changing to match substring
    list1 = list(lst1)
    list2 = list(lst2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            list1[i].lower()
            list2[j].lower()
            element1 = list1[i]
            element2 = list2[j]
            if element1.find(element2) != -1:
                list1[i] = element2
            elif element2.find(element1) != -1:
                list2[j] = element1
    return len(intersection(list1,list2))/len(union(list1,list2))
def main(k):

    #fill user array
    userIngredients = []
    print("'f' to end selection")
    userinput = ""
    ingcount =1
    while (userinput != "f"):
        userinput = input("ingredient #" + str(ingcount)+ str(":\n"))
        if not userinput == "f":
            userIngredients.append(userinput)
        ingcount = ingcount+1
        
    #open training data
    import json
    readPath = "recipe-ingredients-dataset\\train.json"
    with open(readPath) as fp:
        book = json.load(fp)

    #dictValues stores id:jaccardIndex
    dictValues = {}
    #dictRecipes stores id:ingredients
    dictRecipes = {}
    #dictCusine stores id:cuisine category
    dictCuisine = {}
    
    #fill hashmaps
    for recipe in book:
        dictRecipes[recipe['id']] = recipe['ingredients']
        dictCuisine[recipe['id']] = recipe['cuisine']
        dictValues[recipe['id']] = jaccardIndex(recipe['ingredients'], userIngredients)
    sortedKeys = sorted(dictValues, key = dictValues.get, reverse = True)

    #creates dict classification that counts cuisine category for k closest neighbors
    cuisinePath = open("masterCuisine.txt", "r") 
    listofcats = cuisinePath.read().splitlines()
    classification = dict.fromkeys(listofcats,0)
    
    for kcounter in range(k):
        p_element = sortedKeys[kcounter]
        p_jaccardValue = dictValues.get(p_element)
        p_category = dictCuisine.get(p_element)
        #p_ingredients = dictRecipes.get(p_element)
        #print ("recipe id:", p_element)
        #print("recipe similarity score:", p_jaccardValue)
        #print("recipe category:", p_category)
        #print("recipe ingredients:", p_ingredients)
        #print("\n")
        classification[p_category] = classification.get(p_category) + 1
        kcounter = kcounter+1
        if p_jaccardValue != dictValues.get(sortedKeys[kcounter]):
            fail =True   
        
    ##return cuisine category that occured the most
    sortedCats = sorted(classification, key = classification.get, reverse = True)
    print("I think the cateogry is", sortedCats[0])

    
def testJaccard():
    l1 = ["bacon strips", "egg", "apple"]
    l2 = ["bacon", "egg whites", "orange"]
    j = jaccardIndex(l1,l2)
    print(j)
  
main(k)
input()
