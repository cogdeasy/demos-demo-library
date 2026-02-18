from demo_library.config import FeatureFlags


class Calculator:
    def add(self, a: float, b: float) -> float:
        if not FeatureFlags.is_enabled("addition"):
            raise RuntimeError("Addition feature is disabled")
        return a + b

    def subtract(self, a: float, b: float) -> float:
        if not FeatureFlags.is_enabled("subtraction"):
            raise RuntimeError("Subtraction feature is disabled")
        return a - b
