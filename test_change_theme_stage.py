from selene import browser, have


def test_change_account_theme(login):
    # Смена темы на темную
    browser.element('.user-popover .iconedv-Arrow-More-Down').click()
    browser.element('.theme-block_button:nth-child(3)').click()
    browser.element('.theme-block_button:nth-child(3)').should(have.css_class('activeTheme'))

    # Смена темы на светлую
    browser.element('.theme-block_button:nth-child(5)').click()
    browser.element('.theme-block_button:nth-child(5)').should(have.css_class('activeTheme'))

    # Смена темы на системную
    browser.element('.theme-block_button:nth-child(1)').click()
    browser.element('.theme-block_button:nth-child(1)').should(have.css_class('activeTheme'))
