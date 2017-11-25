def test_change_group(app, login_admin, verify_group):

    app.open_group_page()
    app.change_group_by_number(1,name="qqqqqqq", header="wwwwww", footer="eeee")
    # TODO: verification of message
    app.return_to_group_page()

