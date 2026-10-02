from main import calculate_average, get_result


def test_calculate_average():
    assert calculate_average([80, 90, 70]) == 80


def test_get_result():
    assert get_result(90) == "Отлично"