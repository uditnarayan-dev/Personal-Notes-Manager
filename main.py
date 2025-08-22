from datetime import datetime

print("Welcome to Notes Manager")


#1
def add_notes():
    while True:
        c = input("Enter category (w = work/p = personal): ")
        if(c == "w"):
            print("Noting For Work")
            title = input("Enter title: ")
            note = input("Enter note: ")
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            final_note = f"""\nD&T: {current_datetime}\nTitle: {title}\nNote: {note}\n-----\n"""

            with open("work_notes.txt", "a") as f:
                f.write(final_note)
                print("Notes Added Successfully")
            break

        elif(c == "p"):
            print("Noting For Personal")
            title = input("Enter title: ")
            note = input("Enter note: ")
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            final_note = f"""\nD&T: {current_datetime}\nTitle: {title}\nNote: {note}\n-----\n"""

            with open("personal_notes.txt", "a") as f:
                f.write(final_note)
                print("Notes Added Successfully")
            break
        else:
            print("Choose correct option")
        
#2
def view_notes():
    while True:
        c = input("Enter category (w = work/p = personal): ")
        if(c == "w"):
            print("Your Work Notes: ")
            filename = "work_notes.txt"
        elif(c == "p"):
            print("Your Personal Notes: ")
            filename = "personal_notes.txt"
        else:
            print("Choose correct option")
            continue

        try:
            with open(filename, "r") as f:
                content = f.read().strip()
                if not content:
                    print("There is no Notes")
                else:
                    notes = content.split("-----")
                    for i, note in enumerate(notes, start=1):
                        if note.strip():
                            print(f"\nNote {i}: \n{note.strip()}")
                        
            break
        except FileNotFoundError:
            print("No notes file found yet. Add some notes first.\n")
            break
    return filename
#3
def search_notes():
    while True:
        c = input("Enter category (w = work/p = personal): ")
        if(c == "w"):
            print("Checking for Work Notes: ")
            filename = "work_notes.txt"
            keyword = input("Enter keyword to search: ").strip()
        elif(c == "p"):
            print("Checking for Personal Notes: ")
            filename = "personal_notes.txt"
            keyword = input("Enter keyword to search: ").strip()
        else:
            print("Choose correct option")
            continue

        try:
            with open(filename, "r") as f:
                content = f.read().strip()
                if not content:
                    print("No notes yet in this category")
                else:
                    notes = content.split("-----")
                    found = False
                    for i, note in enumerate(notes, start=1):
                        if (keyword.lower() in note.lower()):
                            if note.strip():
                                print(f"\nNote{i}: \n{note.strip()}")
                                found = True
                    if not found:
                        print("No notes matched your search")
            break

        except FileNotFoundError:
            print("No notes file found yet. Add some notes first.\n")
            break
#4
def delete_notes():
    filename = view_notes()
    try:
        note_to_delete = int(input("Enter note number you want to Delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    with open(filename, "r") as f:
        content = f.read().strip()
    if not content:
        print("There is no Notes")
        return
        

    notes = [n.strip() for n in content.split("-----") if n.strip()]
    if note_to_delete<= len(notes):
        del notes[note_to_delete-1]
        with open(filename, "w") as f:
            f.write("-----".join(notes))
            print("Note deleted successfully ✅")      
    else: 
        print("Choose from Range")

    return None
#5
def exit_app():
    print("Exiting... Goodbye!")
    quit()

while True:
    print("""
    1. Add Note 2. View Notes 3. Search Notes 4. Delete Note 5. Exit""")
    choice = int(input("Enter choice: "))

    if(choice == 1):
        add_notes()
    elif(choice == 2):
        view_notes()
    elif(choice == 3):
        search_notes()
    elif(choice == 4):
        delete_notes()
    elif(choice == 5):
        exit_app()
    else:
        print("Invalid choice. Please try again.")

