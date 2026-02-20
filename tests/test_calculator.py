import pytest

from demo_library import Calculator, FeatureFlags


@pytest.fixture(autouse=True)
def reset_flags():
    FeatureFlags.reset()
    yield
    FeatureFlags.reset()


class TestAddition:
    def test_add_positive_numbers(self):
        calc = Calculator()
        assert calc.add(2, 3) == 5

    def test_add_negative_numbers(self):
        calc = Calculator()
        assert calc.add(-1, -2) == -3

    def test_add_floats(self):
        calc = Calculator()
        assert calc.add(1.5, 2.5) == 4.0


class TestSubtraction:
    def test_subtract_disabled_by_default(self):
        calc = Calculator()
        with pytest.raises(RuntimeError, match="Subtraction feature is disabled"):
            calc.subtract(5, 3)

    def test_subtract_when_enabled(self):
        FeatureFlags.enable("subtraction")
        calc = Calculator()
        assert calc.subtract(5, 3) == 2

    def test_subtract_negative_result(self):
        FeatureFlags.enable("subtraction")
        calc = Calculator()
        assert calc.subtract(3, 5) == -2

    def test_subtract_floats(self):
        FeatureFlags.enable("subtraction")
        calc = Calculator()
        assert calc.subtract(5.5, 2.5) == 3.0


class TestFeatureFlags:
    def test_addition_enabled_by_default(self):
        assert FeatureFlags.is_enabled("addition") is True

    def test_subtraction_disabled_by_default(self):
        assert FeatureFlags.is_enabled("subtraction") is False

    def test_enable_subtraction(self):
        FeatureFlags.enable("subtraction")
        assert FeatureFlags.is_enabled("subtraction") is True

    def test_disable_addition(self):
        FeatureFlags.disable("addition")
        assert FeatureFlags.is_enabled("addition") is False

    def test_unknown_feature(self):
        with pytest.raises(ValueError, match="Unknown feature"):
            FeatureFlags.enable("multiplication")

    def test_reset(self):
        FeatureFlags.enable("subtraction")
        FeatureFlags.reset()
        assert FeatureFlags.is_enabled("subtraction") is False
        assert FeatureFlags.is_enabled("addition") is True
