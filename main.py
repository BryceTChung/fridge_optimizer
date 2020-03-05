import csv
from ingredient_class import ingredient

ingre_list = []
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
read_ingre()
write_ingre()
for j in ingre_list:
    print(j.name)
    print(j.expir_date)
    print(j.tags)
