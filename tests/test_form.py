import allure

from homework9.pages.registration_page import RegistrationPage

@allure.title("Successful fill form")
def test_automation_form():
    registration_page = RegistrationPage()

    with allure.step("Open registration form"):
        registration_page.open()
    with allure.step("Fill form"):
        registration_page.fill_first_name('Олег')
        registration_page.fill_last_name('Олегович')
        registration_page.fill_email('oleg.olegovich@example.com')
        registration_page.fill_gender('Male')
        registration_page.fill_mobile_number('1234567890')
        registration_page.fill_date_of_birth('2000','July','10')
        registration_page.fill_subject('Maths')
        registration_page.fill_hobbies('Sports')
        registration_page.download_file()
        registration_page.fill_current_address('г. Москва, ул. 9-мая, д. 1')
        registration_page.fill_state('NCR')
        registration_page.fill_city('Delhi')
        registration_page.submit()

    with allure.step("Check form results"):
        registration_page.should_registered_user_with('Олег Олегович','oleg.olegovich@example.com','Male','1234567890','10 July,2000',
                'Maths','Sports','_.jpeg','г. Москва, ул. 9-мая, д. 1','NCR Delhi'
                )


