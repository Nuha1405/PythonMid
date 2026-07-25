import tkinter as tk

class Cat:

    def __init__(self,cat_id,name,breed,age,gender,vaccinated,status):
        self.cat_id=cat_id
        self.name=name
        self.breed=breed
        self.age=age
        self.gender=gender
        self.vaccinated=vaccinated
        self.status=status

BREEDS=(
    "Persian",
    "Tabby",
    "Siamese",
    "Ragdoll",
    "Mixed"
)

GENDERS=(
    "Male",
    "Female"
)

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

cat_list = [

    Cat("C001","Luna","Persian","6 Months","Female","Yes","Available"),

    Cat("C002","Leo","Tabby","1 Year","Male","Yes","Available"),

    Cat("C003","Milo","Siamese","8 Months","Male","No","Available"),

    Cat("C004","Bella","Ragdoll","2 Years","Female","Yes","Adopted"),

    Cat("C005","Nala","Mixed","5 Months","Female","No","Available"),

    Cat("C006","Oliver","Persian","3 Years","Male","Yes","Available"),

    Cat("C007","Lucy","Tabby","1 Year","Female","Yes","Available"),

    Cat("C008","Simba","Siamese","10 Months","Male","No","Available"),

    Cat("C009","Lily","Ragdoll","2 Years","Female","Yes","Available"),

    Cat("C010","Charlie","Mixed","7 Months","Male","Yes","Available")
]

def save_data():
    try:
        file = open("cats.txt","w")

        for cat in cat_list:

            file.write(
                f"{cat.cat_id},{cat.name},{cat.breed},{cat.age},{cat.gender},{cat.vaccinated},{cat.status}\n"
            )

        file.close()

    except:
        print("Error saving data.")

def load_data():
    try:
        file = open("cats.txt", "r")
        cat_list.clear()

        for line in file:

            data = line.strip().split(",")

            if len(data) == 7:

                cat = Cat(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6]
                )

                cat_list.append(cat)

        file.close()

    except FileNotFoundError:

        save_data()

    except:

        print("File is empty or corrupted.")


# ---------------- View Available Cats ----------------

def view_available_cats(text_box):

    text_box.delete("1.0", "end")

    text_box.insert(
        "end",
        f"{'ID':<6}{'Name':<10}{'Breed':<10}{'Age':<10}{'Gender':<10}{'Vaccinated':<13}{'Status'}\n"
    )

    text_box.insert("end", "-" * 70 + "\n")

    for cat in cat_list:

        if cat.status=="Available":

            text_box.insert(
                "end",
                f"{cat.cat_id:<6}"
                f"{cat.name:<10}"
                f"{cat.breed:<10}"
                f"{cat.age:<10}"
                f"{cat.gender:<10}"
                f"{cat.vaccinated:<13}"
                f"{cat.status}\n"
            )

def search_cat(text_box,breed,gender,vaccinated):

    text_box.delete("1.0","end")

    text_box.insert(
        "end",
        f"{'ID':<6}{'Name':<10}{'Breed':<10}{'Age':<10}{'Gender':<10}{'Vaccinated':<13}{'Status'}\n"
    )

    text_box.insert("end", "-" * 70 + "\n")

    found = False

    for cat in cat_list:

        if (breed == "Any" or cat.breed == breed) and \
           (gender == "Any" or cat.gender == gender) and \
           (vaccinated == "Any" or cat.vaccinated == vaccinated):

            text_box.insert(
                "end",
                f"{cat.cat_id:<6}"
                f"{cat.name:<10}"
                f"{cat.breed:<10}"
                f"{cat.age:<10}"
                f"{cat.gender:<10}"
                f"{cat.vaccinated:<13}"
                f"{cat.status}\n"
            )
            found=True
    if not found:
        text_box.insert("end","\nNo matching cats found.")

def adopt_cat(cat_id):

    for cat in cat_list:
        if cat.cat_id==cat_id:
            if cat.status=="Available":
             cat.status="Adopted"
             save_data()
             return True
        return False
    return false

def add_cat(cat):
    cat_list.append(cat)
    save_data()

def update_cat(cat_id,new_name):
    for cat in cat_list:
        if cat.cat_id==cat_id:
            cat.name = new_name
            save_data()
            return True
    return False

def count_available():
    count=0
    for cat in cat_list:
        if cat.status=="Available":
            count+=1
    return count

def count_adopted():
    count=0
    for cat in cat_list:
        if cat.status=="Adopted":
            count+=1
    return count

def count_vaccinated():
    count=0
    for cat in cat_list:
        if cat.vaccinated == "Yes":
            count += 1
    return count

def gui():

    load_data()

    root = tk.Tk()
    root.title("Happy Paws Cat Adoption")
    root.geometry("750x700")
    root.configure(bg="lightblue")

    tk.Label(root,text="Happy Paws Cat Adoption",font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)

    breed_var = tk.StringVar(value="Any")
    gender_var = tk.StringVar(value="Any")
    vacc_var = tk.StringVar(value="Any")

    text_box = tk.Text( root, width=80, height=12,font=("Courier New", 10))
    text_box.pack(pady=10)

    def show_cats():
        view_available_cats(text_box)

    def search_cats():
        search_cat(
            text_box,
            breed_var.get(),
            gender_var.get(),
            vacc_var.get()
        )

    tk.Button(root,text="View Available Cats",width=20,command=show_cats).pack(pady=5)

    tk.Label(root,text="Breed", bg="lightblue").pack() 
   
    tk.OptionMenu(root,breed_var,
    "Any",
    BREEDS[0],
    BREEDS[1],
    BREEDS[2],
    BREEDS[3],
    BREEDS[4]
    ).pack()

    tk.Label(root,text="Gender",bg="lightblue").pack()

    tk.OptionMenu(root,gender_var,
    "Any",
    GENDERS[0],
    GENDERS[1]
    ).pack()

    tk.Label(root, text="Vaccinated", bg="lightblue").pack()

    tk.OptionMenu(root,vacc_var,
     "Any",
     "Yes",
    "No"
    ).pack()

    tk.Button(root,text="Search",width=20,command=search_cats).pack(pady=5)

    tk.Label(root,text="Enter Cat ID To Adopt",bg="lightblue").pack()

    entry_id = tk.Entry(root, width=20)
    entry_id.pack()

    def adopt_now():

        if adopt_cat(entry_id.get()):

            view_available_cats(text_box)

            success = tk.Toplevel(root)
            success.title("Success")
            success.geometry("300x150")

            tk.Label(success,text="Cat Adopted Successfully!").pack(pady=20)

            tk.Button(success,text="OK",command=success.destroy).pack()

        else:
            text_box.delete("1.0", "end")
            text_box.insert("end","Cat ID Not Found or Already Adopted!")

    tk.Button(root,text="Adopt Now",width=20,command=adopt_now).pack(pady=5)

    def exit_app():
        save_data()
        root.destroy()

    tk.Button(root,text="Exit",width=20,command=exit_app).pack(pady=10)

    root.mainloop()

gui()