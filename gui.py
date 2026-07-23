import tkinter as tk

from CatData import BREEDS, GENDERS
from Functions import (
    load_data,
    save_data,
    view_available_cats,
    search_cat,
    adopt_cat
)

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