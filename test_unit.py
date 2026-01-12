import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility


# -------- deposit() UNIT TESTS --------

def test_deposit_valid_amount():
    assert deposit(1000, 500) == 1500


def test_deposit_boundary_zero():
    with pytest.raises(ValueError):
        deposit(1000, 0)


def test_deposit_negative_amount():
    with pytest.raises(ValueError):
        deposit(1000, -200)


# -------- withdraw() UNIT TESTS --------

def test_withdraw_valid_amount():
    assert withdraw(1000, 300) == 700


def test_withdraw_boundary_equal_balance():
    assert withdraw(1000, 1000) == 0


def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(500, 1000)


def test_withdraw_negative_amount():
    with pytest.raises(ValueError):
        withdraw(1000, -100)


# -------- calculate_interest() UNIT TESTS --------

def test_calculate_interest_valid():
    result = calculate_interest(1000, 10, 1)
    assert result == 1100


def test_calculate_interest_zero_years():
    result = calculate_interest(1000, 10, 0)
    assert result == 1000


def test_calculate_interest_negative_balance():
    with pytest.raises(ValueError):
        calculate_interest(-1000, 10, 1)


def test_calculate_interest_negative_rate():
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 1)


# -------- check_loan_eligibility() UNIT TESTS --------

def test_loan_eligible():
    assert check_loan_eligibility(6000, 750) is True


def test_loan_not_eligible_low_balance():
    assert check_loan_eligibility(3000, 750) is False


def test_loan_not_eligible_low_credit_score():
    assert check_loan_eligibility(6000, 650) is False


def test_loan_negative_balance():
    with pytest.raises(ValueError):
        check_loan_eligibility(-5000, 750)
