

from pytest_bdd import scenarios, given, when, then, parsers
from Full_retirement_calc import RetirementCalculator

CONVERTERS = {
    'Year': int,
    'Month': int,
    'Age': int,
}


@scenarios('../features/retirement.feature', example_converters=CONVERTERS)

@given("User enters “<Year>”")
def year(Year):


@when('User enters "<Month>"')
def step_impl():
    raise NotImplementedError(u'STEP: When User enters "<Month>"')


@then("result should be “<Age>”")
def step_impl():
    raise NotImplementedError(u'STEP: Then result should be “<Age>”')
