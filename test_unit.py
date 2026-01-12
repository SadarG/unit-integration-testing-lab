# test_unit.py
import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility

# deposit tests
def test_deposit_valid():
    assert deposit(1000, 500) == 1500

def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, -100)

# withdraw tests
def test_withdraw_valid():
    assert withdraw(1000, 500) == 500

def test_withdraw_insufficient():
    with pytest.raises(ValueError):
        withdraw(1000, 1500)

def test_withdraw_invalid():
    with pytest.raises(ValueError):
        withdraw(1000, -100)

# calculate_interest tests
def test_calculate_interest_valid():
    assert calculate_interest(1000, 5, 2) == 1000 * (1 + 5/100) ** 2

def test_calculate_interest_negative_balance():
    with pytest.raises(ValueError):
        calculate_interest(-1000, 5, 2)

def test_calculate_interest_negative_rate():
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 2)

# check_loan_eligibility tests
def test_check_loan_eligibility_eligible():
    assert check_loan_eligibility(6000, 750) == True

def test_check_loan_eligibility_not_eligible():
    assert check_loan_eligibility(4000, 650) == False

def test_check_loan_eligibility_negative_balance():
    with pytest.raises(ValueError):
        check_loan_eligibility(-1000, 750)
