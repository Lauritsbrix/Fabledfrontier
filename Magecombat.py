#Præcisions mønster i forskellige patterns, der skal klikkes inden for et spænd af 2 sec, før der kommer et nyt.
import combat
import tkinter as tk
import random
from stats import stats
from character import character


def generate_combination():
    return random.sample(range(1, 10), 3)

def button_click(button_id):
    damage = 1
    global current_combination
    combat.dealdamage(damage,enemy)
    npc_health_label.config(text=enemy.stats.health)
    if button_id in current_combination:
        label.config(text=f"You hit button {button_id}!")
        damage += 1  # Adjust damage as needed
    else:
        label.config(text="Missed!")

def update_combination():
    global current_combination
    current_combination = generate_combination()
    pattern_label.config(text=f"Current Pattern: {current_combination}")
    root.after(2000, update_combination)

def root_destroyed():
    try:
        root.winfo_exists()
        return False
    except tk.TclError:
        return True

def on_closing():
    root.destroy()

root = tk.Tk()
root.title("Combat System - Numlock Grid")

label = tk.Label(root, text="Click the correct pattern to deal damage!")
label.grid(row=0, column=0, columnspan=3)


pattern_label = tk.Label(root, text="")
pattern_label.grid(row=1, column=0, columnspan=3)

buttons = []
for i in range(1, 10):
    row = (i - 1) // 3 + 3
    col = (i - 1) % 3
    button = tk.Button(root, text=str(i), command=lambda i=i: button_click(i), width=10, height=4)
    button.grid(row=row, column=col, padx=5, pady=5)
    buttons.append(button)

player_damage = 1
npc_health = 10
current_combination = generate_combination()
update_combination()

enemystats = stats(10)
enemy = character("enemy","orc","orc","warrior",enemystats)

npc_health_label = tk.Label(root, text= str(enemy.stats.health))
npc_health_label.grid(row=2, column=0, columnspan=3)

window_width = 640
window_height = 320
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()