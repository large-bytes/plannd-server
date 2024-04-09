import pytest
from manager.models import Roster

@pytest.mark.django_db
def test_create_Roster():
    roster_member = Roster.objects.create(
        id=1,
        name="test name",
        email="testemail@gmail.com",
        position="test-cafe role",
        contact_number="07111222323",
    )
    assert roster_member.id == 1
    assert roster_member.name == "test name"
    assert roster_member.email == "testemail@gmail.com"
    assert roster_member.position == "test-cafe role"
    assert roster_member.contact_number == "07111222323"


# @pytest.fixture
# def create_Roster():
#     return Roster.objects.create(
#         id=1,
#         name="test name",
#         email="testemail@gmail.com",
#         position="test-cafe role",
#         contact_number="071112223232",
#         # todo ... user password
#     )


# """
# Test Roster model constructs and it can be created in the database and retrieved
# """

# @pytest.mark.django_db
# def test_Roster
