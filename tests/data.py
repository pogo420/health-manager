"""Definitions of test data"""
from health_manager.user.schemas import Gender, UserDbData, UserData


validUserDataFromServer = UserDbData(
    user_id="345566",
    user_name="sam bam",
    gender=Gender.Male,
    height=123,
    birth_year=1340
    )

validUserDataPayload = UserData(
    user_name="sam bam",
    gender=Gender.Male,
    height=123,
    birth_year=1340
    )

get_user_valid_response = {
    "user_id": "345566",
    "user_name": "sam bam",
    "gender": Gender.Male.value,
    "height": 123,
    "birth_year": 1340
}
