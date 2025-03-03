from selene import browser, have, command, be, by

from resource import resources


class RegistrationPage:

    def __init__(self):
        '''
        Для подхода Assertion free PageObjects
        self.registered_user_data = browser.element('.table').all('td').even
        '''
        self.table_responsive = browser.element('.table-responsive')

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][if$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][if$=container__]').perform(command.js.remove)

    def remove_banner(self):
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, first_name):
        browser.element('#firstName').should(be.blank).type(first_name)

    def fill_last_name(self, last_name):
        browser.element('#lastName').should(be.blank).type(last_name)

    def fill_email(self, email):
        browser.element('#userEmail').should(be.blank).type(email)

    def select_gender(self, value):
        browser.element('#genterWrapper').element(by.text(value)).click()

    def fill_phone(self, phone):
        browser.element('#userNumber').should(be.blank).type(phone)

    def fill_date_of_birth(self, mm, yyyy, dd):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(mm)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(yyyy)).click()
        if len(dd) == 1:
            dd = '0' + dd
        browser.element(f'.react-datepicker__day--0{dd}').click()

    def fill_subject(self, subject_1):
        browser.element('#subjectsInput').type(subject_1).press_enter()

    def select_hobbie(self, value):
        browser.element('#hobbiesWrapper').element(by.text(value)).click()

    def upload_picture(self, file_name):
        browser.element('#uploadPicture').set_value(resources.resource_path(file_name))

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)

    def fill_state(self, state):
        browser.element('#state').click().element(by.text(state)).click()

    def fill_city(self, city):
        browser.element('#city').click().element(by.text(city)).click()

    def click_submit(self):
        browser.element('#submit').click()

    def should_registered_user_info_with(self, first_name, last_name, user_mail, user_male, user_phone,
                                         day, month, year, user_subjects, user_hobbies, user_photo, user_address,
                                         user_state,
                                         user_city):
        browser.element('.modal-header').should(have.exact_text('Thanks for submitting the form'))

        self.table_responsive.should(have.text(f'{first_name} {last_name}'))
        self.table_responsive.should(have.text(f'{user_mail}'))
        self.table_responsive.should(have.text(f'{user_male}'))
        self.table_responsive.should(have.text(f'{user_phone}'))
        self.table_responsive.should(have.text(f'{day} {month},{year}'))
        self.table_responsive.should(have.text(f'{user_subjects}'))
        self.table_responsive.should(have.text(f'{user_hobbies}'))
        self.table_responsive.should(have.text(f'{user_photo}'))
        self.table_responsive.should(have.text(f'{user_address}'))
        self.table_responsive.should(have.text(f'{user_state}'))
        self.table_responsive.should(have.text(f'{user_city}'))
