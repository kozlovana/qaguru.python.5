from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

from qaguru_python_6.controls.datepicker import DatePicker
from qaguru_python_6.controls.dropdown import Dropdown
from qaguru_python_6.controls.tags_input import TagsInput
from tests.utils import get_resource_path
from qaguru_python_6.controls.nameplate import Nameplate


def given_opened_text_box():
    browser.open('/automation-practice-form').driver.maximize_window()

    (
        ss('[id^=google_ads][id$=container__]')
        .with_(timeout=10)
        .should(have.size_greater_than_or_equal(2))
        .perform(command.js.remove)
    )


def test_submit_form():
    given_opened_text_box()

    # Filling the form
    s('#firstName').type('Anastasia')
    s('#lastName').type('Kozlova')
    s('#userEmail').type('kozlova@gmail.com')
    s('[for=gender-radio-2]').click()
    s('#userNumber').type('8911911911')

    date_of_birth = DatePicker(browser.element('#dateOfBirthInput'))
    date_of_birth.select_year(1994)
    date_of_birth.select_month('September')
    date_of_birth.select_day(27)

    subjects = TagsInput(s('#subjectsInput'))
    subjects.tab_selection('Computer Science')
    subjects.autocomplete_selection('Maths')

    s('[for="hobbies-checkbox-3"]').click()

    s('#uploadPicture').send_keys(get_resource_path('girl.png'))

    s('#currentAddress').type('Podgorica')

    state = Dropdown(browser.element('#state'))
    state.select(option='Haryana')

    city = Dropdown(browser.element('#city'))
    city.autocomplete(option='Panipat')

    browser.element('#submit').press_enter()

    # Check
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    res_nameplate = Nameplate()
    res_nameplate.way_to(tr=1, td=2).should(have.text('Anastasia Kozlova'))
    res_nameplate.way_to(tr=2, td=2).should(have.text('kozlova@gmail.com'))
    res_nameplate.way_to(tr=3, td=2).should(have.text('Female'))
    res_nameplate.way_to(tr=4, td=2).should(have.text('8911911911'))
    res_nameplate.way_to(tr=5, td=2).should(have.text('27 September,1994'))
    res_nameplate.way_to(tr=6, td=2).should(have.text('Computer Science, Maths'))
    res_nameplate.way_to(tr=7, td=2).should(have.text('Music'))
    res_nameplate.way_to(tr=8, td=2).should(have.text('girl.png'))
    res_nameplate.way_to(tr=9, td=2).should(have.text('Podgorica'))
    res_nameplate.way_to(tr=10, td=2).should(have.text('Haryana Panipat'))
