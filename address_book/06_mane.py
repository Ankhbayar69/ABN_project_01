contacts = []

while True:
    name = input("Нэр: ")
    phone = input("Утас: ")
    email = input("И-мэйл: ")

    # Бүртгэлтэй эсэх
    duplicate = False
    for contact in contacts:
        if contact["name"] == name and contact["phone"] == phone:
            print(" Энэ харилцагч аль хэдийн бүртгэлтэй байна!")
            duplicate = True
            break

    if not duplicate:
        new_contact = {
            "name": name,
            "phone": phone,
            "email": email
        }
        contacts.append(new_contact)
        print(" Шинэ харилцагч нэмэгдлээ!")

    more = input("Өөр харилцагч нэмэх үү? (y/n): ")
    if more.lower() != "y":
        break

# бүртгүүлсэн багын гишүүд
print("\n📒 Бүртгэлтэй харилцагчид:")
for c in contacts:
    print(c)