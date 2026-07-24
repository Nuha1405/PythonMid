from CatData import Cat, cat_list



def save_data():

    try:

        file = open("cats.txt", "w")

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




def view_available_cats(text_box):

    text_box.delete("1.0", "end")

    text_box.insert(
        "end",
        f"{'ID':<6}{'Name':<10}{'Breed':<10}{'Age':<10}{'Gender':<10}{'Vaccinated':<13}{'Status'}\n"
    )

    text_box.insert("end", "-" * 70 + "\n")

    for cat in cat_list:

        if cat.status == "Available":

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




def search_cat(text_box, breed, gender, vaccinated):

    text_box.delete("1.0", "end")

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

            found = True

    if not found:

        text_box.insert("end", "\nNo matching cats found.")



def adopt_cat(cat_id):

    for cat in cat_list:

        if cat.cat_id == cat_id:

            if cat.status == "Available":

                cat.status = "Adopted"

                save_data()

                return True

            return False

    return False




def add_cat(cat):

    cat_list.append(cat)

    save_data()




def update_cat(cat_id, new_name):

    for cat in cat_list:

        if cat.cat_id == cat_id:

            cat.name = new_name

            save_data()

            return True

    return False




def count_available():

    count = 0

    for cat in cat_list:

        if cat.status == "Available":

            count += 1

    return count


def count_adopted():

    count = 0

    for cat in cat_list:

        if cat.status == "Adopted":

            count += 1

    return count


def count_vaccinated():

    count = 0

    for cat in cat_list:

        if cat.vaccinated == "Yes":

            count += 1

    return count
