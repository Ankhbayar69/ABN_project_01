
contact1 = {"name": "Namjilsuren",
            "phone": "99115090", 
            "email": "namjilsuren5090@gmail.com"}

contact2 = {
    "name": "Batotgon",
    "phone": "88008051",
    "email": "batotgon1111@gmail.com"
}

contact3 = {
           'name' : 'TS.Ankhbayar',
           'phone' : '99090105',
           'email' : 'mongoloo.soft@gmail.com'
            }


contacts = []

name = input("Нэр оруулна уу: ")
phone = input("Утасны дугаар оруулна уу: ")

contact = {
    "name": name,
    "phone": phone
}

contacts.append(contact)

print("Хадгалсан хаягууд:", contacts)
