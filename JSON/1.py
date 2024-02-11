import json 

with open("C:/Users/mansur/Desktop/PP2/TSIS4/JSON/ex.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU ")
print("-------------------------------------------------- --------------------  ------  ------")
    
for element in data["imdata"]:
    DN = element["l1PhysIf"]["attributes"]["dn"]
    Description = element["l1PhysIf"]["attributes"]["descr"]
    Speed = element["l1PhysIf"]["attributes"]["speed"]
    MTU = element["l1PhysIf"]["attributes"]["mtu"]
    if len(DN) == 42:
        print(DN, Description, "                           ", Speed, " ", MTU)
    else:
        print(DN, Description, "                            ", Speed, " ", MTU)