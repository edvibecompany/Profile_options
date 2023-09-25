from selene import browser, have, be


def test_check_account_options(login):
    # Переход в настройки через меню аккаунта
    browser.element('.user-popover .iconedv-Arrow-More-Down').click()
    browser.element('.tir-option:nth-child(1)').click()
    browser.element('.tir-popover_content').should(be.not_.visible)
    browser.element('.content_layout-content-title').should(have.exact_text('Настройки'))
    browser.element('.elements .title:nth-child(1)').should(have.css_class('is-active'))

    # Переход в тарифы через меню аккаунта
    browser.element('.user-popover .iconedv-Arrow-More-Down').click()
    browser.element('.tir-option:nth-child(2)').click()
    browser.element('.tir-popover_content').should(be.not_.visible)
    browser.element('.content_layout-content-title').should(have.exact_text('Настройки'))
    browser.element('.elements .title:nth-child(2)').should(have.css_class('is-active'))

    # Выход из аккаунта
    browser.element('.user-popover .iconedv-Arrow-More-Down').click()
    browser.element('.tir-option:nth-child(3)').click()
    browser.should(have.url('https://stage.progressme.ru/'))
