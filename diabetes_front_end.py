import tkinter as tk


#def predict():


def create_gui():
    root = tk.Tk()
    root.title("Diabetes Prediction")

    # Set background color
    root.configure(bg="#FFEDDB")

    # Create header label with custom text color
    header_label = tk.Label(root, text="Diabetes Prediction", bg="#E3B7A0", fg="#BF9270", font=("Arial", 16, "bold"))
    header_label.pack(fill="x", padx=10, pady=10)  # Fill horizontally across the whole window

    # Create input labels and text entry boxes
    input_frame = tk.Frame(root, bg="#FFEDDB")
    input_frame.pack(padx=10, pady=10)

    tk.Label(input_frame, text="Pregnancies:", bg="#FFEDDB").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    pregnancies_entry = tk.Entry(input_frame)
    pregnancies_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Glucose:", bg="#FFEDDB").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    glucose_entry = tk.Entry(input_frame)
    glucose_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Blood Pressure:", bg="#FFEDDB").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    blood_pressure_entry = tk.Entry(input_frame)
    blood_pressure_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Skin Thickness:", bg="#FFEDDB").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    skin_thickness_entry = tk.Entry(input_frame)
    skin_thickness_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create Predict button with custom color
    predict_button = tk.Button(root, text="Predict", bg="#EDCDBB")#command=predict)
    predict_button.pack(pady=10)

    # Your remaining GUI elements and logic here...

    # Run the GUI
    root.mainloop()


if __name__ == "__main__":
    create_gui()

