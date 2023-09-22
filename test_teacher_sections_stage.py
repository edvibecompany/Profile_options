from selene import browser, have, be


def test_sections_check(login):
    browser.wait_until(browser.element('.edvibe3-shedule').should(be.visible))

    # Переход во вкладку Обучение
    browser.element('.sidebar_section_list .iconedv-School').click()
    browser.element('.content_layout-content-title').should(have.exact_text('Обучение'))

    # Переход во вкладку Материалы
    browser.element('.sidebar_section_list .iconedv-Course').click()
    browser.element('.content_layout-content-title').should(have.exact_text('Материалы'))

    # Переход во вкладку Расписание
    browser.element('.sidebar_section_list .iconedv-Calendar').click()
    browser.element('.content_layout-content-title').should(have.exact_text('Расписание'))

    # Переход во вкладку Настройки
    browser.element('.sidebar_section_list .iconedv-Setting').click()
    browser.element('.content_layout-content-title').should(have.exact_text('Настройки'))
