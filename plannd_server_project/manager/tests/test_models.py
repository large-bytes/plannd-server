import pytest
from manager.models import Roster



@pytest.fixture
def create_roster():

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
def test_create_Roster(create_roster):
    assert create_roster[0][0].id == 1
    assert create_roster[0][0].name == "test name"
    assert create_roster[0][0].email == "testemail@gmail.com"
    assert create_roster[0][0].position == "test-cafe role"
    assert create_roster[0][0].contact_number == "07000000000"


@pytest.mark.django_db
def test_roster_entries_can_be_equal(create_roster):
    """
    We can compare two identical roster entries
    And have them be equal
    """
    roster1 = create_roster[0]
    roster2 = create_roster[0]
    assert roster1 == roster2


@pytest.mark.django_db
def test_retrieves_all_staff_members_from_db(create_roster):
    """
    Test Roster model constructs and it can be created in the database and retrieved
    """
    
    all_staff = Roster.objects.all()
    print(all_staff)
    assert len(all_staff) == 3


@pytest.mark.django_db
def test_retrieves_an_individual_staff_member(create_roster):
    """
    Test that an individual staff member can be selected
    """
    staff_member2 = Roster.objects.filter(pk=2)
    staff_member3 = Roster.objects.filter(pk=3)

    assert staff_member2[0] == create_roster[1]
    assert staff_member3[0] == create_roster[2]


@pytest.mark.django_db
def test_deletes_an_individual_staff_member(create_roster):
    """
    Test that an individual staff member can be deleted
    """
    Roster.objects.filter(pk=2).delete()
    all_staff = Roster.objects.all()

    assert len(all_staff) == 2
    assert all_staff[0].id == 1
    assert all_staff[1].id == 3


@pytest.mark.django_db
def test_updates_an_individual_staff_member(create_roster):
    """
    Test that staff member details can be edited
    """
    Roster.objects.filter(pk=1).update(name="Orson Welles")
    Roster.objects.filter(pk=3).update(email="new@geemail.com")

    staff1 = Roster.objects.filter(pk=1)
    staff3 = Roster.objects.filter(pk=3)

    assert staff1[0].name == "Orson Welles"
    assert staff3[0].email == "new@geemail.com"
