from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def given_opened_text_box():
    browser.open('/automation-practice-form').driver.maximize_window()

    (
        ss('[id^=google_ads][id$=container__]')
        .with_(timeout=10)
        .should(have.size_greater_than_or_equal(2))
        .perform(command.js.remove)
    )

#    browser.execute_script("$('body').css('zoom', 0.5);") позволяет увидеть кнопку submit но рушит код


def test_submit_form():
    given_opened_text_box()


# Filling in form
    s('#firstName').type('Anastasia')
    s('#lastName').type('Kozlova')
    s('#userEmail').type('kozlova@gmail.com')
    s('[for=gender-radio-2]').click()
    s('#userNumber').type('8911911911')gi

    s('#dateOfBirthInput').click()
    s('[value="1994"]').click()
    s('[value="3"]').click()
    s('[aria-label="Choose Wednesday, April 27th, 1994"]').click()

    s('#subjectsInput').type('Computer Science').press_enter()
    s('#subjectsInput').type('Maths').press_enter()

    s('[for="hobbies-checkbox-3"]').click()
    s('#uploadPicture').type('/Users/anastasiakozlova/PycharmProjects/qaguru.python.5/tests/girl.png')
    s('#currentAddress').type('Podgorica')
    s('#react-select-3-input').type('Rajasthan').press_enter()
    s('#react-select-4-input').type('Jaipur').press_enter().press_tab()

    s('#submit').perform(command.js.click)


# Check
    browser.all("tbody tr").should(have.texts(
        'Student Name Anastasia Kozlova',
        'Student Email kozlova@gmail.com',
        'Gender Female',
        'Mobile 8911911911',
        'Date of Birth 27 April,1994',
        'Subjects Computer Science, Maths',
        'Hobbies Music',
        'Picture girl.png',
        'Address Podgorica',
        'State and City Rajasthan Jaipur'
    ))