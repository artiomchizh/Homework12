from pathlib import Path
from selene import have
from selene.support.shared import browser
from homework9.data.users import User, user

expected_gender = user.gender.value
class RegistrationPage:
    def __init__(self):
        self.register_info = browser.element('.table').all('td').even
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.mobile_number = browser.element('#userNumber')
        self.subject = browser.element('#subjectsInput')
        self.file = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')

    def open(self):
        browser.config.timeout = 10
        browser.driver.set_window_size(1920, 1080)
        browser.open('https://demoqa.com')
        browser.element('a[href="/forms"]').click()
        browser.element('a[href="/automation-practice-form"]').click()


    def register(self, user:User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        if expected_gender == "Male":
            browser.element('[for="gender-radio-1"]').click()
        elif expected_gender == "Female":
            browser.element('[for="gender-radio-2"]').click()
        else:
            browser.element('[for="gender-radio-3"]').click()
        self.email.type(user.email)
        self.mobile_number.type(user.mobile_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select') \
            .all('option').element_by(have.text(str(user.date_of_birth.year))).click() \
            .click()
        month_name = user.date_of_birth.strftime("%B")
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select') \
            .all('option').element_by(have.text(month_name)) \
            .click()
        browser.element(f'.react-datepicker__day--0{user.date_of_birth.day}').click()
        self.subject.type(user.subject)
        browser.element('.subjects-auto-complete__menu').element('div').click()
        if user.hobbies == "Sports":
            browser.element('[for="hobbies-checkbox-1"]').click()
        elif user.hobbies == "Reading":
            browser.element('[for="hobbies-checkbox-2"]').click()
        else: browser.element('[for="hobbies-checkbox-3"]').click()
        file_path = (
                Path(__file__).parent.parent.parent / "image/_.jpeg")
        self.file.send_keys(
            str(file_path.resolve()))
        self.address.type(user.address)
        browser.element('#react-select-3-input').type(user.state)
        browser.element('[id^="react-select-3-option-"]').click()
        browser.element('#react-select-4-input').type(user.city)
        browser.element('[id^="react-select-4-option-"]').click()
        return self

    def submit(self):
        browser.element('#submit').click()

    def should_registered_user_with(self, user:User):
        expected_hobby = user.hobbies.value
        expected_date = user.date_of_birth.strftime("%d %B,%Y")
        self.register_info.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                expected_gender,
                user.mobile_number,
                expected_date,
                user.subject,
                expected_hobby,
                '_.jpeg',
                user.address,
                f'{user.state} {user.city}',
            )
        )
