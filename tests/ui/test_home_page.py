from app.browser import Browser


def test_home_page_is_openable():
    expected_text = "Welcome to the-internet"
    main_title_text = Browser().to_home_page().main_title.text
    assert expected_text == main_title_text
