import json
from xml.dom import minidom
from car import Car

'''read file'''
file = open("5-main.json")
content = file.read()
file_content = json.loads(content)

cars = [] 
brands = []
nb_doors = 0

for i in file_content:
    car = Car(i)
    brands = car.get_brand()
    brands.append(brands)
    nb = car.get_nb_doors()
    nb_doors += nb
    xml_car = car.to_xml_node(doc)
    cars.appendChild(xml_car)

'''DOM'''
doc = minidom.Document()
cars = doc.createElement("cars")
doc.appendChild(cars)

print len(brands)
print nb_doors
print cars[3]
print doc.toxml(encoding='utf-8')
