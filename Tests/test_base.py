import pytest


# @pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("login")
class BaseTest:
    pass