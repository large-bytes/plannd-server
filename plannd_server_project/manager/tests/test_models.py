import pytest
from manager.models import Roster


@pytest.fixture
def create_Roster():
    staff_1 = (
        Roster.objects.create(
            id=1,
            name="test name",
            email="testemail@gmail.com",
            position="test-cafe role",
            contact_number="07000000000",
            # todo ... user password
        ),
    )
    staff_2 = Roster.objects.create(
        id=2,
        name="test name 2",
        email="testemail2@gmail.com",
        position="test-cafe role 2",
        contact_number="07111111111",
    )
    staff_3 = Roster.objects.create(
        id=3,
        name="test name 3",
        email="testemail3@gmail.com",
        position="test-cafe role 3",
        contact_number="07222222222",
    )
    return [staff_1, staff_2, staff_3]


@pytest.mark.django_db
def test_create_Roster(create_Roster):
    assert create_Roster[0][0].id == 1
    assert create_Roster[0][0].name == "test name"
    assert create_Roster[0][0].email == "testemail@gmail.com"
    assert create_Roster[0][0].position == "test-cafe role"
    assert create_Roster[0][0].contact_number == "07000000000"


"""
We can compare two identical roster entries
And have them be equal
"""


@pytest.mark.django_db
def test_roster_entries_can_be_equal(create_Roster):
    roster1 = create_Roster[0]
    roster2 = create_Roster[0]
    assert roster1 == roster2


"""
# Test Roster model constructs and it can be created in the database and retrieved
# """


@pytest.mark.django_db
def test_retrieves_all_staff_members_from_db(create_Roster):

    all_staff = Roster.objects.all()
    assert len(all_staff) == 3


"""
Test that an individual staff member can be selected
"""


@pytest.mark.django_db
def test_retrieves_an_individual_staff_member(create_Roster):
    staff_member2 = Roster.objects.filter(pk=2)
    staff_member3 = Roster.objects.filter(pk=3)

    assert staff_member2[0] == create_Roster[1]
    assert staff_member3[0] == create_Roster[2]


"""
Test that an individual staff member can be deleted
"""


@pytest.mark.django_db
def test_deletes_an_individual_staff_member(create_Roster):
    Roster.objects.filter(pk=2).delete()
    all_staff = Roster.objects.all()

    assert len(all_staff) == 2
    assert all_staff[0].id == 1
    assert all_staff[1].id == 3


"""
Test that staff member details can be edited 
"""


@pytest.mark.django_db
def test_updates_an_individual_staff_member(create_Roster):
    Roster.objects.filter(pk=1).update(name="Orson Welles")
    Roster.objects.filter(pk=3).update(email="new@geemail.com")

    staff1 = Roster.objects.filter(pk=1)
    staff3 = Roster.objects.filter(pk=3)

    assert staff1[0].name == "Orson Welles"
    assert staff3[0].email == "new@geemail.com"
