from selene import browser, have, be


def test_switch_account(login):
    browser.wait_until(browser.element('.edvibe3-shedule').should(be.visible))

    # Переход в марафоны
    browser.element('.menu-toggle').click()
    browser.element('.sections_menu-items .section_card:nth-child(2)').click()
    browser.should(have.url_containing('/cabinet/teacher/marathons/marathons'))

    # Переход в аккаунт академии
    browser.element('.menu-toggle').click()
    browser.element('.sections_menu-items .section_card:nth-child(3)').click()
    browser.should(have.url_containing('/cabinet/teacher/academy/main'))

    # Переход в аккаунт ученика
    browser.element('.menu-toggle').click()
    browser.element('.sections_menu-items .section_card:nth-child(4)').click()
    browser.should(have.url_containing('/cabinet/student/lessons'))

    # Переход в аккаунт учителя
    browser.element('.menu-toggle').click()
    browser.element('.sections_menu-items .section_card:nth-child(1)').click()
    browser.should(have.url_containing('/cabinet/teacher/lessons/schdule'))
