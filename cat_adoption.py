import tkinter as tk
from tkinter import messagebox


# =========================
# OOP: Cat Class
# =========================

class Cat:

    def __init__(self, cat_id, name, breed, age, gender, vaccinated, price):
        self.cat_id = cat_id
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender
        self.vaccinated = vaccinated
        self.price = price


    def display(self):
        return (
            "Cat ID: " + str(self.cat_id) +
            "\nName: " + self.name +
            "\nBreed: " + self.breed +
            "\nAge: " + str(self.age) +
            "\nGender: " + self.gender +
            "\nVaccinated: " + self.vaccinated +
            "\nPrice: " + str(self.price) + " BDT\n"
            "------------------------\n"
        )


# =========================
# Pre-loaded cats
# =========================

cats = [

    Cat(101, "Maha", "Tabby", 2, "Female", "Yes", 5000),
    Cat(102, "Simba", "Persian", 1, "Male", "Yes", 15000),
    Cat(103, "Luna", "Ragdoll", 3, "Female", "No", 20000),
    Cat(104, "Leo", "British Shorthair", 2, "Male", "Yes", 18000),
    Cat(105, "Milo", "Mixed Breed", 1, "Male", "No", 4000)

]


# =========================
# Functions
# =========================

# 1. Display all cats

def view_all_cats():

    result_box.delete("1.0", tk.END)

    for cat in cats:
        result_box.insert(
            tk.END,
            cat.display()
        )



# 2. Search cats by preferences

def search_cats():

    breed = breed_choice.get()
    age = age_choice.get()
    gender = gender_choice.get()
    vaccine = vaccine_choice.get()


    result_box.delete("1.0", tk.END)

    found = False


    for cat in cats:

        if (
            (breed == "Any" or cat.breed == breed)
            and
            (age == "Any" or str(cat.age) == age)
            and
            (gender == "Any" or cat.gender == gender)
            and
            (vaccine == "Any" or cat.vaccinated == vaccine)
        ):

            result_box.insert(
                tk.END,
                cat.display()
            )

            found = True


    if not found:
        result_box.insert(
            tk.END,
            "No matching kittens found."
        )



# 3. Find cat by ID

def find_cat(cat_id):

    for cat in cats:

        if cat.cat_id == cat_id:
            return cat

    return None



# 4. Adopt cat

def adopt_cat():

    try:

        cat_id = int(adopt_entry.get())

        cat = find_cat(cat_id)


        if cat:

            cats.remove(cat)

            messagebox.showinfo(
                "Adoption Successful",
                cat.name + " has been adopted!"
            )

            view_all_cats()


        else:

            messagebox.showerror(
                "Error",
                "Cat ID not found."
            )


    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter a valid Cat ID."
        )



# 5. Count available cats

def count_available():

    return len(cats)



# 6. Calculate average price

def average_price():

    total = 0

    for cat in cats:
        total += cat.price

    if len(cats) > 0:
        return total / len(cats)

    return 0



# =========================
# GUI
# =========================

window = tk.Tk()

window.title("Happy Paws Cat Adoption")

window.geometry("600x650")


title = tk.Label(
    window,
    text="Happy Paws Cat Adoption",
    font=("Arial",18,"bold")
)

title.pack(pady=10)



tk.Button(
    window,
    text="View Available Cats",
    command=view_all_cats
).pack()



# Search section

tk.Label(
    window,
    text="Find Your Perfect Kitten",
    font=("Arial",14)
).pack(pady=10)



breed_choice = tk.StringVar(value="Any")

tk.Label(window,text="Breed").pack()

tk.OptionMenu(
    window,
    breed_choice,
    "Any",
    "Tabby",
    "Persian",
    "Ragdoll",
    "British Shorthair",
    "Mixed Breed"
).pack()



age_choice = tk.StringVar(value="Any")

tk.Label(window,text="Age").pack()

tk.OptionMenu(
    window,
    age_choice,
    "Any",
    "1",
    "2",
    "3"
).pack()



gender_choice = tk.StringVar(value="Any")

tk.Label(window,text="Gender").pack()

tk.OptionMenu(
    window,
    gender_choice,
    "Any",
    "Male",
    "Female"
).pack()



vaccine_choice = tk.StringVar(value="Any")

tk.Label(window,text="Vaccinated").pack()

tk.OptionMenu(
    window,
    vaccine_choice,
    "Any",
    "Yes",
    "No"
).pack()



tk.Button(
    window,
    text="Search",
    command=search_cats
).pack(pady=5)



# Result display

result_box = tk.Text(
    window,
    height=12,
    width=65
)

result_box.pack(pady=10)



# Adoption section

tk.Label(
    window,
    text="Enter Cat ID to Adopt"
).pack()


adopt_entry = tk.Entry(window)

adopt_entry.pack()



tk.Button(
    window,
    text="Adopt Now",
    command=adopt_cat
).pack(pady=5)



window.mainloop()
tk.tk
tk.tk