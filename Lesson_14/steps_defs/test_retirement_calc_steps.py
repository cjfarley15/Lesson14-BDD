

from pytest_bdd import scenarios, given, when, then, parsers
from Full_retirement_calcs import RetirementCalculator


CONVERTERS = {
    'Year': int,
    'Month': int,
    'Age': int,
}


@scenarios('../features/retirement.feature', example_converters=CONVERTERS)

@given("User enters “<Year>”")
def year():
    assert

@when('User enters "<Month>"')
def month():



@then("result should be “<Age>”")
def age(Age):
    assert RetirementCalculator(current_m = )






