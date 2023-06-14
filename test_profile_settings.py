from selene import browser, have, be

def test_settings_check():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('div.auth-form.auth-container > form > button:nth-child(4)').should(be.visible))
    browser.element('div.auth-form.auth-container > form > button:nth-child(4)').click()
    browser.wait_until(have.url('https://edvibe.com/TeacherAccount/lessons'))
    browser.element('div.profile > div > div > div.box-avatar').click()
    browser.element('div.options > div:nth-child(2) > span').should(have.text('Настройки профиля'))
    browser.element('div.box-dropdown.default.animation-up.open.advent > div.options > div:nth-child(2)').click()
    browser.element('.page-settings').should(be.visible)

