import pytest
from bank_app import transfer, calculate_interest

# -------- transfer() INTEGRATION TESTS --------

def test_transfer_valid():
    from_balance, to_balance = transfer(1000, 500, 300)
    assert from_balance == 700
    assert to_balance == 800


def test_transfer_full_balance():
    from_balance, to_balance = transfer(500, 1000, 500)
    assert from_balance == 0
    assert to_balance == 1500


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(400, 1000, 800)


def test_transfer_negative_amount():
    with pytest.raises(ValueError):
        transfer(1000, 500, -200)


# -------- Combined Workflow TEST --------

def test_transfer_then_interest_calculation():
    from_balance, to_balance = transfer(2000, 1000, 500)
    final_balance = calculate_interest(to_balance, 10, 1)
    # Floating point issue fix
    assert final_balance == pytest.approx(1650)
