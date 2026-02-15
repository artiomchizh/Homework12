from pathlib import Path

import allure
from selene import have, browser
from homework9.data.users import User, user

class RegistrationPage:
    def __init__(self):
        pass

    @allure.step("Open url /automation-practice-form")
    def open(self):
        browser.config.timeout = 5
        browser.open('https://demoqa.com')
        browser.element('a[href="/forms"]').click()
        browser.element('a[href="/automation-practice-form"]').click()

    @allure.step("Fill first name")
    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    @allure.step("Fill last name")
    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    @allure.step("Fill gender")
    def fill_gender(self, gender):
        if gender == "Male":
            browser.element('[for="gender-radio-1"]').click()
        elif gender == "Female":
            browser.element('[for="gender-radio-2"]').click()
        else:
            browser.element('[for="gender-radio-3"]').click()

    @allure.step("Fill email")
    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    @allure.step("Fill mobile number")
    def fill_mobile_number(self, number):
        browser.element('#userNumber').type(number)

    @allure.step("Fill date of birth")
    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select') \
            .all('option') \
            .element_by(have.text(year)) \
            .click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select') \
            .all('option') \
            .element_by(have.text(month)) \
            .click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        browser.execute_script("window.scrollBy(0, 500)")

    @allure.step("Fill subject")
    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value)
        browser.element('.subjects-auto-complete__menu').element('div').click()

    @allure.step("Fill hobbies")
    def fill_hobbies(self, value):
        if value == "Sports":
            browser.element('[for="hobbies-checkbox-1"]').click()
        elif value == "Reading":
            browser.element('[for="hobbies-checkbox-2"]').click()
        else:
            browser.element('[for="hobbies-checkbox-3"]').click()

    @allure.step("Fill file")
    def download_file(self):
        file_path = (
                Path(__file__).parent.parent.parent / "image/_.jpeg")
        browser.element("#uploadPicture").send_keys(
            str(file_path.resolve()))

    @allure.step("Fill current address")
    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)

    @allure.step("Fill state")
    def fill_state(self, value):
        browser.element('#react-select-3-input').type(value)
        browser.element('[id^="react-select-3-option-"]').click()

    @allure.step("Fill city")
    def fill_city(self, city):
        browser.element('#react-select-4-input').type(city)
        browser.element('[id^="react-select-4-option-"]').click()

    @allure.step("Click submit button")
    def submit(self):
        browser.element('#submit').click()

    def should_registered_user_with(self, full_name, email, gender, mobile_number, date_of_birth, subject, hobbies, file,
                                address, city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile_number,
                date_of_birth,
                subject,
                hobbies,
                file,
                address,
                city,
            )
        )

# expected_gender = user.gender.value
#
# class RegistrationPage:
#     def __init__(self):
#         self.register_info = browser.element('.table').all('td').even
#         self.first_name = browser.element('#firstName')
#         self.last_name = browser.element('#lastName')
#         self.email = browser.element('#userEmail')
#         self.mobile_number = browser.element('#userNumber')
#         self.subject = browser.element('#subjectsInput')
#         self.file = browser.element('#uploadPicture')
#         self.address = browser.element('#currentAddress')
#
#     def open(self):
#         browser.config.timeout = 10
#         browser.driver.set_window_size(1920, 1080)
#         browser.open('https://demoqa.com')
#         browser.element('a[href="/forms"]').click()
#         browser.element('a[href="/automation-practice-form"]').click()
#
#
#     def register(self, user:User):
#         self.first_name.type(user.first_name)
#         self.last_name.type(user.last_name)
#         if expected_gender == "Male":
#             browser.element('[for="gender-radio-1"]').click()
#         elif expected_gender == "Female":
#             browser.element('[for="gender-radio-2"]').click()
#         else:
#             browser.element('[for="gender-radio-3"]').click()
#         self.email.type(user.email)
#         self.mobile_number.type(user.mobile_number)
#         browser.element('#dateOfBirthInput').click()
#         browser.element('.react-datepicker__year-select').click()
#         browser.element('.react-datepicker__year-select') \
#             .all('option').element_by(have.text(str(user.date_of_birth.year))).click() \
#             .click()
#         month_name = user.date_of_birth.strftime("%B")
#         browser.element('.react-datepicker__month-select').click()
#         browser.element('.react-datepicker__month-select') \
#             .all('option').element_by(have.text(month_name)) \
#             .click()
#         browser.element(f'.react-datepicker__day--0{user.date_of_birth.day}').click()
#         browser.execute_script("window.scrollBy(0, 500)")
#         self.subject.type(user.subject)
#         browser.element('.subjects-auto-complete__menu').element('div').click()
#         if user.hobbies == "Sports":
#             browser.element('[for="hobbies-checkbox-1"]').click()
#         elif user.hobbies == "Reading":
#             browser.element('[for="hobbies-checkbox-2"]').click()
#         else: browser.element('[for="hobbies-checkbox-3"]').click()
#         file_path = (
#                 Path(__file__).parent.parent.parent / "image/_.jpeg")
#         self.file.send_keys(
#             str(file_path.resolve()))
#         self.address.type(user.address)
#
#         browser.element('#react-select-3-input').type(user.state)
#         browser.element('[id^="react-select-3-option-"]').click()
#
#         browser.element('#react-select-4-input').type(user.city)
#         browser.element('[id^="react-select-4-option-"]').click()
#         return self
#
#     def submit(self):
#
#         browser.element('#submit').click()
#
#     def should_registered_user_with(self, user:User):
#         expected_hobby = user.hobbies.value
#         expected_date = user.date_of_birth.strftime("%d %B,%Y")
#         self.register_info.should(
#             have.exact_texts(
#                 f'{user.first_name} {user.last_name}',
#                 user.email,
#                 expected_gender,
#                 user.mobile_number,
#                 expected_date,
#                 user.subject,
#                 expected_hobby,
#                 '_.jpeg',
#                 user.address,
#                 f'{user.state} {user.city}',
#             )
#         )
