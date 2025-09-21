from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 17 Pro Max", "+79876543210"),
    Smartphone("Samsung", "Galaxy S26 Ultra", "+79876543211"),
    Smartphone("Xiaomi", "Redmi Note 11S", "+79876543212"),
    Smartphone("Huawei", "P50 Pro", "+79876543213"),
    Smartphone("Google", "Pixel 7 Pro", "+79876543214"),

]
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
