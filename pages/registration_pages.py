import os

import allure
from selene import  have, command


class RegistrationPage:
    def __init__(self, browser):
        self.browser = browser

    def remove_block(self):
        self.browser.driver.execute_script(
            'document.querySelector("#fixedban").remove()'
        )

    def __init1__(self):
        self.state = browser.all('[id^=react-select][id*=option]')
        self.adress = browser.element('#currentAddress')

    @allure.step("Открытие файла")
    def choice_pictures(self, filename):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), f'../tests/resources/{filename}'))

    @allure.step("Заполнение имени")
    def fill_first_name(self, value):
        browser.element('#firstName').send_keys(value)

    @allure.step("Заполнение фамилии")
    def fill_last_name(self, value):
        browser.element('#lastName').send_keys(value)

    @allure.step("Заполнение email")
    def fill_email(self, value):
        browser.element('#userEmail').send_keys(value)

    @allure.step("Заполнение номера телефона")
    def fill_number(self, value):
        browser.element('#userNumber').send_keys(value)

    @allure.step("Выбор пола")
    def choice_gender(self, value):
        browser.element('[name = gender][value = Male]+label').click()

    @allure.step("Дата рождения")
    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element(f'.react-datepicker__day--0{day}').click()

    @allure.step("Выбор предмета")
    def choice_subject(self, value):
        browser.element('#subjectsInput').send_keys(value).press_enter()

    @allure.step("Увлечения")
    def choice_hobbies(self, value):
        browser.all('[for = hobbies-checkbox-1]').element_by(have.exact_text(value)).click()

    @allure.step("Увлечения")
    def choice_hobbies_more(self, value):
        browser.all('[for = hobbies-checkbox-2]').element_by(have.exact_text(value)).click()

    def choice_hobbies_more_more(self, value):
        browser.all('[for = hobbies-checkbox-3]').element_by(have.exact_text(value)).click()

    @allure.step("Проверка формы регистрации")
    def assert_register_user_info(self, full_name,
                                  email, gender,
                                  number, day_brith,
                                  subject, hobbies,
                                  picture, adress, city):
        browser.all('tbody tr').should(have.exact_texts(
            f'Student Name {full_name}',
            f'Student Email {email}',
            f'Gender {gender}',
            f'Mobile {number}',
            f'Date of Birth {day_brith}',
            f'Subjects {subject}',
            f'Hobbies {hobbies}',
            f'Picture',
            f'Address {adress}',
            f'State and City {city}',
        ))

    @allure.step("Адрес")
    def fill_adress(self, adress):
        self.adress.perform(command.js.scroll_into_view)
        self.adress.send_keys(adress)
        browser.element('#state').click()

    @allure.step("Штат")
    def fill_state(self, state):
        self.state.element_by(have.exact_text(state)).click()
        browser.element('#city').click()

    @allure.step("Город")
    def fill_city(self, city):
        self.state.element_by(have.exact_text(city)).click()
        browser.element('#submit').perform(command.js.click)
