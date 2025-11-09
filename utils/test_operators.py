import pytest
import operators as op


def test_true():
    assert op.multiply(5, 5) == 25
    assert op.multiply("5", 5) == 25
    assert op.multiply("3.5", 2) == 7.0


def test_false():
    with pytest.raises(ValueError):
        op.multiply("a", "b")
    with pytest.raises(TypeError):
        op.multiply([1, 2], 5)
