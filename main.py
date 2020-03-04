import csv
from ingredient_class import ingredient

ingre_list = []
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
    for j in ingre_list:
        print(j.name)
        print(j.expir_date)
        print(j.tags)
