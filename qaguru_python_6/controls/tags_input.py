from selene import have
from selene.core.entity import Element
from selene.support.shared import browser


class TagsInput:
    def __init__(self, element: Element):
        self.element = element

    def tab_selection(self, search: str):
        self.element.type(search).press_tab()

    def autocomplete_selection(self, search: str):
        self.element.type(search)
        browser.all(
            '.subjects-auto-complete__option'
        ).element_by(have.text(search)).click()
