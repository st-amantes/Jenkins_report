import allure

@allure.step('wan')
def test_failed1():
    assert False


@allure.step('wan')
def test_failed2():
    assert False