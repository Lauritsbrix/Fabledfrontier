import tkinter as tk
from tkinter import PhotoImage

def character_selection_screen():
    text_label.pack_forget()
    continue_button.pack_forget()

    character_label = tk.Label(root, text="Character Selection", font=("Helvetica", 18))
    character_label.pack(pady=20)

    race_frame = tk.Frame(root)
    race_frame.pack()

    def select_race(race):
        print("You selected:", race)

    def create_clickable_image(image, race, x, y):
        # Create a clickable image on the canvas
        image_id = canvas.create_image(x, y, anchor="nw", image=image)
        canvas.tag_bind(image_id, "<Button-1>", lambda event, race=race: select_race(race))

    canvas_width = 1000  # Adjust the width as needed
    canvas_height = 600  # Adjust the height as needed
    canvas = tk.Canvas(race_frame, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Load and scale images
    human_img = PhotoImage(file=r"C:\Users\sebzz\Pictures\human.png").subsample(2)
    elf_img = PhotoImage(file=r"C:\Users\sebzz\Pictures\elf.png").subsample(2)
    dwarf_img = PhotoImage(file=r"C:\Users\sebzz\Pictures\dwarf.png").subsample(2)

    # Calculate the width of each image on the canvas
    image_width = canvas_width // 3

    # Create clickable images on the canvas
  
    create_clickable_image(human_img, "Human",0,0)
    create_clickable_image(elf_img, "Elf",250,0)
    create_clickable_image(dwarf_img, "Dwarf", 500, 8)
    

    # Position the images on the canvas
    canvas.coords(canvas.find_all(), [(i * image_width, 0) for i in range(3)])

def continue_to_character_selection():
    continue_button.pack_forget()
    text_label.pack_forget()
    character_selection_screen()

root = tk.Tk()
root.title("Simple RPG")
root.geometry("800x600")

text_label = tk.Label(root, text="Welcome to Simple RPG!", font=("Helvetica", 18))
text_label.pack(pady=20)

continue_button = tk.Button(root, text="Continue", command=continue_to_character_selection)
continue_button.pack()

root.mainloop()
