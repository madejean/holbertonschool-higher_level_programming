import json
from xml.dom import minidom
from car import Car

'''read file'''
file = open("5-main.json")
content = file.read()
file_content = json.loads(content)

cars_obj = []
brands = []
nb_doors = 0

'''DOM'''
doc = minidom.Document()
cars = doc.createElement("cars")
doc.appendChild(cars)

for i in file_content:
  car = Car(i)
  cars_obj.append(car)
  brand = car.get_brand()
  if not brand in brands:
    brands.append(brand)
  nb = car.get_nb_doors()
  nb_doors += nb
  xml_car = car.to_xml_node(doc)
  cars.appendChild(xml_car)

print len(brands)
print nb_doors
print cars_obj[3]
print doc.toxml(encoding='utf-8')
