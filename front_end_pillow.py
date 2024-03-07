from tkinter import *
import numpy as np
from tensorflow import keras
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from keras.layers import Dense
from keras.layers import Dense
from keras import Sequential
#from PIL import Image, ImageTk


root = Tk()
root.geometry('200x200')

#image = Image.open()
#image = image.resize((20, 20))
photo = PhotoImage(file = "build_img.png")
#image = ImageTk.PhotoImage(image)
def predict():
    print("iam in")
def build_click():
    #print("iam in")
    df = pd.read_csv("diabetes.csv")
    X_train, X_test, y_train, y_test = train_test_split(df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                                                            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']],
                                                        df.Outcome, test_size=0.2, random_state=25)
    X_train_scaled = X_train.copy()
    X_train_scaled = StandardScaler().fit_transform(X_train_scaled)

    X_test_scaled = X_test.copy()
    X_test_scaled = StandardScaler().fit_transform(X_test_scaled)
    print(X_test_scaled)
    global model = Sequential()
    model.add(Dense(16, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1,
                    activation='sigmoid'))  # this is output layer - should have as many neurons as there are outputs to the classification problem.

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.fit(X_train_scaled, y_train, epochs=500)
    accuracy = model.evaluate(X_test_scaled, y_test)
    print(accuracy[0])
    #add a text box in th gui to display accuracy
    #print(df.head())
def openNewWindow():
        # Toplevel object which will
        # be treated as a new window
        newWindow = Toplevel(root)

        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")

        # sets the geometry of toplevel
        newWindow.geometry("200x200")

        # A Label widget to show in toplevel
        #labels and text boxes of the 8 attributes and the predict button
        button1= Button(newWindow,width=100, height=20, image=photo, command=predict())
        button1.pack()

button = Button(width=100, height=20, image=photo, command=openNewWindow)
button.pack(padx=20, pady=50)
root.mainloop()