import tkinter as tk

FONT = font=("Arial", 14, "normal")

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

def calculate():
    miles = float(miles_input.get())
    km_result = miles * 1.609
    result.config(text=km_result)

#First column
is_equal_to= tk.Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=1)

#Second column
miles_input = tk.Entry(width=7, font=FONT)
miles_input.grid(column=1, row=0)

result = tk.Label(text="0", font=FONT)
result.grid(column=1, row=1)

button = tk.Button(text="Calculate", font=FONT, command=calculate)
button.grid(column=1, row=2)

#Third column
miles = tk.Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)

km = tk.Label(text="Km", font=FONT)
km.grid(column=2, row=1)

window.mainloop()