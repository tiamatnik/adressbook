Feature: Group CRUD
  Description

  Scenario Outline: Add new group
    Given a group list
    Given a new group <name>, <header>, <footer>
    When add this group
    Then a new groul list is equal to old with this new group

    Examples:
    | name | header | footer |
    | qwerty | HGHG | fhiefh |
    | ршыва  | овшмоыв | jhdcj |
    | ^&878  |         |       |
