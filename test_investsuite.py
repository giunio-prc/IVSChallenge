import pytest

from invesuite import number_of_digit


@pytest.mark.parametrize(
    "in_, out",
    [
        (100, 3),
        (10, 2),
        pytest.param(1e04, 5, id="float exp format"),
        pytest.param("1e+04", 5, id="float string"),
        (3.1415, 1),
        pytest.param(0, 1, id="zero integer"),
        ("123", 3),
        ("13.00", 2),
        pytest.param("0.0", 1, id="zero in str"),
        pytest.param("000", 1, id="special zero in str"),
        (10j, 1),
        (13 + 4j, 2),
        (-1, 2),
        (-13 + 4j, 3),
    ],
)
def test_number_of_digit(in_, out):
    assert number_of_digit(in_) == out


@pytest.mark.parametrize("in_", ["Just a random string", "134Almost right"])
def test_exceptions(in_):
    with pytest.raises(ValueError) as valueerror:
        number_of_digit(in_)

    assert valueerror.value.args[0].endswith("malformed string")
