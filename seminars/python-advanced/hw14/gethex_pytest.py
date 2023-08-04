import pytest
from hw14.gethex import get_hex


def test_zero():
    assert get_hex(0) == '0'


def test_values():
    assert get_hex(10) == 'a'
    assert get_hex(16) == '10'
    assert get_hex(255) == 'ff'
    assert get_hex(1024) == '400'


def test_exception():
    with pytest.raises(TypeError):
        get_hex('hello')


if __name__ == '__main__':
    pytest.main(['-v'])
