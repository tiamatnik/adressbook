from pytest_bdd import given, when, then
from models.group import Group

@given('a group list')
def old_group_list(db):
    return db.get_groups

@given ('a new group <name>, <header>, <footer>')
def group(name, header, footer):
    return group(name, header, footer)

@when('add this group')
def add_group(app, login_admin, group):
    app.open_group_page()
    app.create_group(group)
    app.return_to_group_page()

@then('a new groul list is equal to old with this new group')
def verify_group_creation(db, old_group_list, group):
    new_list = db.get_groups()
    assert len(new_list) == len(old_group_list) + 1
    assert group == new_list[-1]

