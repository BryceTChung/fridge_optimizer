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
        for x in tag_string:
            if x == ',':
                ingr.tags.append(tag)
                tag = ""
            tag = tag + x
        #ingr.tags = i["tags"]
        ingre_list.append(ingr)
    for j in ingre_list:
        print(j.name)
        print(j.expir_date)
        print(j.tags)
