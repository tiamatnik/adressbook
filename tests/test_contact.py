import random

def test_create_contact(app, login_admin):
    app.return_to_main()
    app.create_contact(address="1 street", name="11111", lastname ='22222', title="333333", company = '44444',
    mobile = '66666', home = '7777')
    app.return_to_main()


def test_update_contact(app, login_admin):
    app.return_to_main()
    app.update_contact(address="qwerty", name="qwerty", lastname ='qwerty', title="qwerty",
    company = 'qwerty',  mobile = 'qwerty', home = 'qwerty', id=1)
    app.return_to_main()


def test_delete_contact(app, login_admin):
    app.return_to_main()
    index = random.randrange(app.count_contacts())
    app.delete_contact_by_number(index)
    app.return_to_main()
