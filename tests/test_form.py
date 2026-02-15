

from homework9.data.users import user

from homework9.pages.registration_page import RegistrationPage

def test_automation_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(user).submit()
    registration_page.should_registered_user_with(user)
