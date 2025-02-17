def test_fill_valid_data(create_page):
    create_page.open_page()
    create_page.fill_registration_form()
    assert (create_page.check_successful_registration_title_is() ==
            'Thank you for registering with Main Website Store.')
