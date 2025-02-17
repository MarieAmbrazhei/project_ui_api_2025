def test_header_title(home_page):
    home_page.open_page()
    assert home_page.check_title_is() == 'Home Page'
