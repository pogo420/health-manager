"""Definition of test data"""
from health_manager.user.schemas import Gender


class ValidUserDataFromServer:
    user_id = "345566"
    user_name = "sam bam"
    gender = Gender.Male.value
    height = 123
    birth_year = 1340
