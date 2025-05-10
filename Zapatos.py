import json 

with open ("Zapatos.json","r",encoding="utf-8") as file:
    data=json.load(file)

for i in data ["zapatos"]:
    print("Modelo:",i["modelo"],"Color:",i["color"],"Precio:", i["precio"])