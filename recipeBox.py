
#Recipe box code
#https://www.bettycrocker.com/recipes/lemon-squares/2ad1502f-5a4d-44e7-a463-c229831b2a5b

#INGREDIENTS as a dictionary

ingredients = ["all-purpose flour", "butter or margarine", "powdered sugar", "sugar", "grated lemon peel", "lemon juice", "baking powder", "salt", "eggs"]
amount = ["1 cup", "1/2 cup", "1/4 cup", "1 cup", "2 tsp", "2 tbs", "1/2 tsp", "1/4 tsp", "2"]

ingredientsDict = dict(zip(ingredients, amount))

#print(ingredientsDict) #printing like this looks nasty so I printed these as strings. But the dictionary version also exists to store the data together

print("\nIngredients:")

for item in range(len(ingredientsDict)):
    print(amount[item] + "    " + ingredients[item])

#INSTRUCTIONS as a list

instructions = ["1. Heat oven to 350°F. In small bowl, mix flour, butter and 1/4 cup powdered sugar. Press in ungreased 8-inch or 9-inch square pan, building up 1/2-inch edge. Bake 20 minutes.",
"2. In small bowl, beat granulated sugar, lemon peel, lemon juice, baking powder, salt and eggs with electric mixer on high speed about 3 minutes or until light and fluffy. Pour over hot crust.",
 "3. Bake 25 to 30 minutes or until almost no indentation remains when touched lightly in center. Cool completely, about 1 hour. Sprinkle with additional powdered sugar. For squares, cut into 5 rows by 5 rows."]

print("\nInstructions:")

for number in instructions:
    print(number)
