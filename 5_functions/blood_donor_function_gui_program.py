import tkinter
from tkinter import messagebox

# to donate blood, you must be 16 or older, and weight must be 110 lbs or greater.
# A graphical user interface program.


class BloodDonorApplication(tkinter.Frame):

    """ Represents the graphical application.
    Everything in this block of code sets up the graphical user interface
    and enables the functionality - like what happens when a button is clicked """

    def __init__(self, master):
        """ Calls tkinter library code methods to create the window for the application
        and then calls the custom method to create window components """
        super().__init__(master)
        self.pack()
        self.create_components()

    def create_components(self):
        """ Creates the text entry, label and button components. Also
        configures what function to call when each button is pressed """
        self.age_entry = tkinter.Entry(self)
        self.age_label = tkinter.Label(self, text="Enter age, in years")
        self.weight_entry = tkinter.Entry(self)
        self.weight_label = tkinter.Label(self, text="Enter weight, in pounds")
        self.check_eligible_button = tkinter.Button(self, text='Check eligibility', command=self.get_data_and_check_eligible)
        self.quit = tkinter.Button(self, text='Quit', command=self.master.destroy)

        self.age_label.grid(row=1, column=1)
        self.age_entry.grid(row=1, column=2)
        self.weight_label.grid(row=2, column=1)
        self.weight_entry.grid(row=2, column=2)
        self.check_eligible_button.grid(row=3, column=1)
        self.quit.grid(row=4, column=1)

    def get_data_and_check_eligible(self):
        """ Reads data from the two data entry fields, validates, and displays error message for invalid input
        If input is valid, calls a function to check eligibility and displays the eligibility in a message box. """
        age_text = self.age_entry.get()
        weight_text = self.weight_entry.get()

        try:
            age = validate_number_in_range(age_text, 0, 130)
            weight = validate_number_in_range(weight_text, 0, 1000)

            eligible = check_donor_eligibility(age, weight)

            if eligible:
                # This shows a message box - it replaces similar code that prints a message in previous version
                tkinter.messagebox.showinfo('Eligible!', 'You are eligible to donate blood')
            else:
                tkinter.messagebox.showinfo('Not Eligible', 'You are not eligible to donate blood')

        except ValueError as e:
            tkinter.messagebox.showerror('Error', 'Please enter numbers\n'
                                                  'Age must be between 0 and 130\n'
                                                  'Weight must be between 0 and 1000.')


def validate_number_in_range(string, min, max):
    """ If a string represents a number within the range given by min and max (inclusive)
    convert number to float and return it.
    If string does not represent a number or the number is outside the range given, raise a ValueError """
    number = float(string)
    if number < min or number > max:
        raise ValueError('number outside of range')
    return number


# The same function from the previous program!
def check_donor_eligibility(age, weight):
    if age >= 16 and weight >= 110:
        return True  # indicates yes, user is eligible
    else:
        return False  # indicates no, not eligible


def main():
    # Create a tkinter graphical application and start it running
    root = tkinter.Tk()
    app = BloodDonorApplication(root)
    app.mainloop()


main()
