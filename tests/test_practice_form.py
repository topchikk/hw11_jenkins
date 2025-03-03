from resource.users import new_user
from pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.remove_banner()

    # WHEN
    registration_page.fill_first_name(new_user.first_name)
    registration_page.fill_last_name(new_user.last_name)
    registration_page.fill_email(new_user.user_email)

    registration_page.select_gender(new_user.gender)

    registration_page.fill_phone(new_user.user_number)
    registration_page.fill_date_of_birth(new_user.month, new_user.year, new_user.day)

    registration_page.fill_subject(new_user.subjects)
    registration_page.select_hobbie(new_user.hobbies)

    registration_page.upload_picture(new_user.images)

    registration_page.fill_address(new_user.current_address)
    registration_page.fill_state(new_user.state)
    registration_page.fill_city(new_user.city)

    registration_page.click_submit()

    # THEN
    registration_page.should_registered_user_info_with(new_user.first_name, new_user.last_name, new_user.user_email,
                                                       new_user.gender, new_user.user_number, new_user.day,
                                                       new_user.month, new_user.year, new_user.subjects,
                                                       new_user.hobbies, new_user.images, new_user.current_address,
                                                       new_user.state,
                                                       new_user.city)
