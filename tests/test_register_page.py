def test_fill_valid_data(register_page):
    register_page.open_page()
    register_page.fill_registration_form()
    assert (register_page.check_successful_registration_title_is() ==
            'Thank you for registering with Main Website Store.')
