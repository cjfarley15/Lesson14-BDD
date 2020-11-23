from pytest_bdd import scenario, given, when, then, scenarios
from Full_retirement_calc import RetirementCalculator

CONVERTERS = {
    'Year': int,
    'Month': int,
    'Age': int,
}


@scenario('../features/retirement.feature', 'Test the Calculator for a Month Value Error')
@given('The user enters "1961"')
def valid_year():
    raise NotImplementedError(u'STEP: Given The user enters "1961"')


@when('The user enters "0"')
def invalid_month():
    raise NotImplementedError(u'STEP: When The user enters "0"')


@then("The result should be Value Error")
def value_error():
    raise NotImplementedError(u'STEP: Then The result should be Value Error')


@scenario('../features/retirement.feature', 'Test the Calculator for incorrect format')
@given('The user enters "Hello"')
def invalid_year():
    raise NotImplementedError(u'STEP: Given The user enters "Hello"')

@then("The result should be Error")
def invalid_result():
    raise NotImplementedError(u'STEP: Then The result should be Error')


@scenarios('../features/retirement.feature', example_converters=CONVERTERS)
@given("User enters “<Year>”")
def year_entry(Year):
    raise NotImplementedError(u'STEP: Given User enters “<Year>”')


@when('User enters "<Month>"')
def month_entry(Month):
    raise NotImplementedError(u'STEP: When User enters "<Month>"')


@then("result should be “<Age>”")
def age_result(Age):
    raise NotImplementedError(u'STEP: Then result should be “<Age>”')
