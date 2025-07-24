contacts = []

while True:
    name = input("Нэр: ")
    phone = input("Утас: ")
    email = input("И-мэйл: ")

    new_contact = (name, phone, email)

    if new_contact in contacts:
        print(" Энэ харилцагч бүртгэгдсэн байна!")
    else:
        contacts.append(new_contact)
        print(" Шинэ харилцагч нэмэгдлээ!")

        break

print("\n Бүртгэлтэй харилцагчид:")
for c in contacts:
    print(c)