Cats.py
class Cat:

    def __init__(self, cat_id, name, breed, age, gender, vaccinated, status):
        self.cat_id = cat_id
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender
        self.vaccinated = vaccinated
        self.status = status


# Tuple
BREEDS = (
    "Persian",
    "Tabby",
    "Siamese",
    "Ragdoll",
    "Mixed"
)

GENDERS = (
    "Male",
    "Female"
)

# Set
cat_ids = {
    "C001",
    "C002",
    "C003",
    "C004",
    "C005",
    "C006",
    "C007",
    "C008",
    "C009",
    "C010"
}

# List
cat_list = [
    Cat("C001", "Luna", "Persian", "6 Months", "Female", "Yes", "Available"),
    Cat("C002", "Leo", "Tabby", "1 Year", "Male", "Yes", "Available"),
    Cat("C003", "Milo", "Siamese", "8 Months", "Male", "No", "Available"),
    Cat("C004", "Bella", "Ragdoll", "2 Years", "Female", "Yes", "Adopted"),
    Cat("C005", "Nala", "Mixed", "5 Months", "Female", "No", "Available"),
    Cat("C006", "Oliver", "Persian", "3 Years", "Male", "Yes", "Available"),
    Cat("C007", "Lucy", "Tabby", "1 Year", "Female", "Yes", "Available"),
    Cat("C008", "Simba", "Siamese", "10 Months", "Male", "No", "Available"),
    Cat("C009", "Lily", "Ragdoll", "2 Years", "Female", "Yes", "Available"),
    Cat("C010", "Charlie", "Mixed", "7 Months", "Male", "Yes", "Available")
]