

def test_invalid_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('mary@gmail.com', '123456ttt')
    actual_alert_message = login_page.check_error_alert_text_is()
    expected_alert_message = (
        'The account sign-in was incorrect or your account is disabled '
        'temporarily. Please wait and try again later.'
    )
    assert actual_alert_message == expected_alert_message, (f'Expected alert message '
                                                            f'{expected_alert_message}, but got {actual_alert_message}')


def test_valid_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('mary@hello.com', 'Kapuza123')
    assert login_page.check_title_is_logined_in() == 'My Account'
