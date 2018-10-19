Meals = float(100)


while True:
    numFamilies = int(input('How many families are there? '))
    if numFamilies > 0:
        break
    
while True:
    familySize= int(input('How many people are in each family? '))
    if familySize > 0:
        break

MealsPerson= round(Meals/(familySize*numFamilies),2)

for j in range (1, numFamilies+1):
    for i in range (1, familySize+1):
         print ('Here is your food person#' + str(i) + ' in family#' + str(j) + ', you get ' + str(MealsPerson) + ' meals.')


