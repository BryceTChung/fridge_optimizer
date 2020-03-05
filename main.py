import csv
from ingredient_class import ingredient
from recipe_class import recipe_class

def read_ingre():
    with open("ingredients.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for i in reader:
            ingr = ingredient()
            ingr.name = i["name"]
            ingr.quantity = i["quantity"]
            ingr.expir_date = i["expir_date"]
            tag_string = i["tags"]
            tag = "" 
            while True:
                if type(tag_string) == type(None):
                    break
                for x in tag_string:
                    if x == ',':
                        ingr.tags.append(tag)
                        tag = ""
                        x=''
                    tag = tag + x
                ingr.tags.append(tag)
                break
            #ingr.tags = i["tags"]
            ingre_list.append(ingr)

def write_ingre():
    field_names = ["name","quantity","expir_date","tags"]

    with open("ingredients.csv", "w",newline="") as new_file:
        writer = csv.writer(new_file)
        writer.writerow(field_names)
        for i in ingre_list:
            csv_row = []
            csv_row.append(i.name)
            csv_row.append(i.quantity)
            csv_row.append(i.expir_date)
            tag_str = ""
            new = ""
            for x in i.tags:
                tag_str = tag_str + str(x) + ","
            new = tag_str[0:(len(tag_str)-1)]
            csv_row.append(new)
            
            writer.writerow(csv_row)

def read_recipe():
    with open("recipes.csv","r",newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for i in reader:
            recipe = recipe_class()
            recipe.name = i["name"]
            ingre_list_str = i["ingredients"]
            ingre =""
            quantity = ""
            ingre_quantity =[]
            x=0
            #print(ingre_list_str)
            #print(len(ingre_list_str))
            while(x != len(ingre_list_str)-1):

                print("x:",x)
                if ingre_list_str[x] == ":":
                    
                    ingre_quantity.append(ingre)
                    x+=1
                    while x <= len(ingre_list_str)-1 and ingre_list_str[x] != ",":
                        quantity = quantity + ingre_list_str[x]
                        x+=1
                    x+=1
                    ingre_quantity.append(int(quantity))
                    quantity = ""
                    ingre =""
                    recipe.ingredients.append(ingre_quantity)
                    ingre_quantity =[]
                    if x >= len(ingre_list_str):
                        break

                ingre = ingre + ingre_list_str[x]
                x +=1

            tag_string = i["tags"]
            tag = "" 
            while True:
                if type(tag_string) == type(None):
                    break
                for x in tag_string:
                    if x == ',':
                        recipe.tags.append(tag)
                        tag = ""
                        x=''
                    tag = tag + x
                recipe.tags.append(tag)
                break
            recipe_list.append(recipe)

def write_recipe():
    field_names = ["name","ingredients","tags"]
    with open("recipes.csv", "w",newline="") as new_file:
        writer = csv.writer(new_file)
        writer.writerow(field_names)
        for i in recipe_list:
            csv_row = []
            csv_row.append(i.name)
            ingre_str = ""
            for x in i.ingredients:
                ingre_str = ingre_str +str(x[0])+":"+str(x[1])+","
            final = ingre_str[0:(len(ingre_str)-1)]
            csv_row.append(final)
            tag_str = ""
            new = ""
            for x in i.tags:
                tag_str = tag_str + str(x) + ","
                new = tag_str[0:(len(tag_str)-1)]
            csv_row.append(new)
            writer.writerow(csv_row)


ingre_list = []
read_ingre()
write_ingre()
# for j in ingre_list:
#     print(j.name)
#     print(j.expir_date)
#     print(j.tags)

recipe_list = []
read_recipe()
write_recipe()
for j in recipe_list:
    print(j.name)
    print(len(j.ingredients))
    print(j.ingredients)
    print(j.tags)
