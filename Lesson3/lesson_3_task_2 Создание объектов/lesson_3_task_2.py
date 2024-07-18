from smartphone import Smartphone
catalog = []
catalog.append(Smartphone("Xiaomi", "14 ultra", "+79269999999"))
catalog.append(Smartphone("Apple", "iPhone 15 Pro Max", "+7927999999"))
catalog.append(Smartphone("Samsung", "Galaxy S24 Ultra", "+79289999999"))
catalog.append(Smartphone("Honor", "Magic 6 pro", "+79299999999"))
catalog.append(Smartphone("Realme", "12 pro plus", "+79239999999"))
for phone in catalog:
    print(f"{phone.phone_brand} - {phone.model}. {phone.phone_number}")