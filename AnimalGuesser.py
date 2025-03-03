import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
from PIL import Image, ImageTk
import random 

class AnimalQuizApp:
    def __init__(self, root):
        # Initialize the main app window and set up the initial question, answers, and UI elements
        self.root = root
        self.root.title("Animal Quiz")
        self.root.geometry("500x900")
        self.root.configure(bg="#f4f4f4")
        self.current_question = 0
        self.answers = []
        self.animals = self.load_animals()
        self.questions = list(self.questions_map.keys())
        self.asking_additional_questions = False
        self.summary_frame = None
        self.button_save = None
        self.button_guess = None
        self.guess_count = 0

        # Label for displaying questions
        self.label = tk.Label(root, text=self.questions[self.current_question], font=("Arial", 14, "bold"), bg="#f4f4f4", wraplength=450)
        self.label.pack(pady=20)
        
        # Frame for holding the answer buttons
        self.button_frame = tk.Frame(root, bg="#f4f4f4")
        self.button_frame.pack()

        # Create buttons for answering Yes, No, or Don't know
        self.create_buttons()

    def load_animals(self, filename="animals.csv"):
        # Load animal data from a CSV file into a list of dictionaries
        animals = []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                animals.append(row)
        return animals

    questions_map = {
        "Is it wild?": "Wild",
        "Is it a mammal?": "Mammal",
        "Is it herbivorous?": "Herbivore",
        "Is it bipedal?": "Biped",
        "Is it fast?": "Fast",
        "Is it big?": "Large",
        "Can it fly?": "Flies",
        "Can it swim?": "Can Swim",
        "Does it have claws?": "Has Claws",
        "Does it live in the jungle?": "Lives in Jungle",
        "Does it live in the desert?": "Lives in Desert",
        "Does it live in the water?": "Lives in Water"
    }

    additional_questions_map = {
        "Is it nocturnal?": "Nocturnal",
        "Does it have feathers?": "Has Feathers",
        "Does it have sharp teeth?": "Sharp Teeth",
        "Does it have horns?": "Has Horns",
        "Is it venomous?": "Venomous"
    }

    def create_buttons(self):
        # Create the answer buttons for Yes, No, and Don't know
        self.button_yes = tk.Button(self.button_frame, text="Yes", command=lambda: self.next_question("Yes"),
                                    bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=10, height=2)
        self.button_yes.grid(row=0, column=0, padx=5, pady=5)

        self.button_no = tk.Button(self.button_frame, text="No", command=lambda: self.next_question("No"),
                                   bg="#F44336", fg="white", font=("Arial", 12, "bold"), width=10, height=2)
        self.button_no.grid(row=0, column=1, padx=5, pady=5)

        self.button_unknown = tk.Button(self.button_frame, text="Don't know", command=lambda: self.next_question("Don't know"),
                                        bg="#2196F3", fg="white", font=("Arial", 12, "bold"), width=10, height=2)
        self.button_unknown.grid(row=0, column=2, padx=5, pady=5)
    
    def next_question(self, answer):
        # Record the answer and move to the next question
        self.answers.append(answer)
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.label.config(text=self.questions[self.current_question])
        else:
            self.show_summary()

    def show_summary(self):
        # Hide answer buttons and show summary of answers
        self.button_frame.pack_forget()
        if self.button_guess:
            self.button_guess.pack_forget()
        if self.button_save:
            self.button_save.pack_forget()

        self.label.config(text="Summary of answers:")
        self.summary_frame = tk.Frame(self.root, bg="#f4f4f4")
        self.summary_frame.pack()

        self.entries = []
        for i, question in enumerate(self.questions):
            tk.Label(self.summary_frame, text=question, font=("Arial", 10, "bold"), bg="#f4f4f4").grid(row=i, column=0, sticky='w', padx=5, pady=2)
            var = tk.StringVar(value=self.answers[i])
            dropdown = tk.OptionMenu(self.summary_frame, var, "Yes", "No", "Don't know")
            dropdown.grid(row=i, column=1, padx=5, pady=2)
            self.entries.append(var)
        
        self.create_guess_and_save_buttons()

    def create_guess_and_save_buttons(self):
        # Create the buttons for saving answers and guessing the animal
        self.button_save = tk.Button(self.root, text="Save Changes", command=self.save_changes, font=("Arial", 12, "bold"), bg="#9E9E9E", fg="white")
        self.button_save.pack(pady=10)
        
        self.button_guess = tk.Button(self.root, text="Guess", command=self.guess_animal, font=("Arial", 14, "bold"), bg="#673AB7", fg="white")
        self.button_guess.pack(pady=10)

    def save_changes(self):
        # Save the updated answers from the dropdowns
        self.answers = [var.get() for var in self.entries]
        messagebox.showinfo("Saved", "Answers have been updated.")
    
    def guess_animal(self):
        # Filter animals based on the current answers and make a guess
        filtered_animals = self.animals.copy()

        for i, question in enumerate(self.questions[:len(self.questions_map)]):
            csv_column = self.questions_map.get(question)
            if csv_column:
                expected_answer = self.answers[i]
                if expected_answer in ["Yes", "No"]:
                    filtered_animals = [animal for animal in filtered_animals if csv_column in animal and animal[csv_column].strip().lower() == expected_answer.lower()] 

        if self.asking_additional_questions:
            for i, question in enumerate(self.questions[len(self.questions_map):] ):
                csv_column = self.additional_questions_map.get(question)
                if csv_column:
                    expected_answer = self.answers[len(self.questions_map) + i]
                    if expected_answer in ["Yes", "No"]:
                        filtered_animals = [animal for animal in filtered_animals if csv_column in animal and animal[csv_column].strip().lower() == expected_answer.lower()]

        if len(filtered_animals) == 0:
            messagebox.showinfo("No Matches Found", "No matches found.")
            self.ask_for_animal_name()
        
        elif len(filtered_animals) == 1:
            guessed_animal = filtered_animals[0]["Animal"]
            # Perry's Easter egg
            if guessed_animal.lower() == "platypus":
                response = messagebox.askyesno("Is it a Platypus?", "Is it a Platypus?")
                if response:
                    response_perry = messagebox.askyesno("Perry the Platypus?", "Perry the Platypus?")
                    if response_perry:
                        self.show_image("Perry.png", "PERRY THE PLATYPUS!")
                    else:
                        self.show_image("Platypus.png", "Just a regular platypus")
                else:
                    self.ask_for_animal_name()
            else:
                response = messagebox.askyesno("Is it your animal?", f"Is your animal a {guessed_animal}?")
                if response:
                    messagebox.showinfo("Guessed!", "I guessed it!")
                    self.root.quit()
                else:
                    self.ask_for_animal_name()

        else:
            random_animal = random.choice(filtered_animals)["Animal"]
            response = messagebox.askyesno("Not Sure", f"I'm not sure, but... is your animal a {random_animal}?")
            
            if response:
                messagebox.showinfo("Guessed!", "I guessed it!")
                self.root.quit()
            else:
                if self.guess_count == 1:
                    self.ask_for_animal_name()
                else:
                    self.guess_count += 1
                    self.ask_additional_questions()

    def ask_for_animal_name(self):
        #If no match is found, ask the user for the animal's name
        animal_name = simpledialog.askstring("Animal Name", "Please enter the name of your animal:")
        # Perry's Easter egg
        if animal_name and animal_name.lower() == "platypus":
            response = messagebox.askyesno("Is it Perry?", "Perry the Platypus?")
            if response:
                self.show_image("Perry.png", "PERRY THE PLATYPUS!")
            else:
                self.show_image("Platypus.png", "Just a regular platypus")
        else:
            animal_found = None
            for animal in self.animals:
                if animal["Animal"].lower() == animal_name.lower():
                    animal_found = animal
                    break

            if animal_found:
                messagebox.showinfo("Congratulations!", f"We found {animal_name} in the database! Try again and check your answers")
            else:
                messagebox.showinfo("Congratulations!", f"We didn't know that animal. We'll add it soon!")
            self.root.quit()

    def show_image(self, image_filename, title):
        # Display an image of the platypus or Perry
        new_window = tk.Toplevel(self.root)
        new_window.title(title)

        def on_close():
            self.root.quit()
            new_window.destroy()

        new_window.protocol("WM_DELETE_WINDOW", on_close)

        try:
            image = Image.open(image_filename)
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(new_window, image=photo)
            image_label.image = photo
            image_label.pack()

            label = tk.Label(new_window, text=title, font=("Arial", 14, "bold"))
            label.pack(pady=10)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

    def ask_additional_questions(self):
        # Add additional questions after the initial ones
        if self.summary_frame:
            self.summary_frame.pack_forget()

        if self.button_guess:
            self.button_guess.pack_forget()
        if self.button_save:
            self.button_save.pack_forget()

        self.questions.extend(self.additional_questions_map.keys())
        self.asking_additional_questions = True
        self.current_question = len(self.questions_map)
        self.label.config(text=self.questions[self.current_question])
        self.create_buttons()
        self.button_frame.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimalQuizApp(root)
    root.mainloop()
