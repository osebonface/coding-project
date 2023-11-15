import kivy
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout()
        # Create a label for the title of the form
        title_label = Label(text="Registration Form", font_size=20)
        layout.add_widget(title_label)
        # Create an input field for first name
        fname_input = TextInput(hint_text='First Name')
        layout.add_widget(fname_input)
        # Create an input field for last name
        lname_input = TextInput(hint_text='Last Name')
        layout.add_widget(lname_input)
        # Create an input field for email address
        email_input = TextInput(hint_text='Email Address', multiline=False, password=True)
        layout.add_widget(email_input)
        # Create an input field for phone number
        pnum_input = TextInput(hint_text='Phone Number', multiline=False, password=True)
        layout.add_widget(pnum_input)
        # Create a submit button to register user
        submit_button = Button(text='Register User', background_color=[1, 1, 1, .5])
        layout.add_widget(submit_button)
        return layout
    if __name__ == '__main__':
        RegistrationApp().run()