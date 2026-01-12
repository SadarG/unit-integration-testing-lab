# test_integration.py
import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest

def test_transfer_valid():
    balance_from, balance_to = transfer(1000, 500, 300)
    assert balance_from == 700
    assert balance_to == 800

def test_transfer_insufficient():
    with pytest.raises(ValueError):
        transfer(100, 500, 200)

def test_transfer_and_interest():
    # Transfer first
    balance_from, balance_to = transfer(2000, 1000, 500)
    # Then calculate interest on new balance_to
    interest = calculate_interest(balance_to, 5, 1)
    assert balance_from == 1500
    assert balance_to == 1500
    assert interest == 1500 * 1.05
