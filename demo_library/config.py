class FeatureFlags:
    _flags = {
        "addition": True,
        "subtraction": False,
    }

    @classmethod
    def is_enabled(cls, feature: str) -> bool:
        return cls._flags.get(feature, False)

    @classmethod
    def enable(cls, feature: str) -> None:
        if feature not in cls._flags:
            raise ValueError(f"Unknown feature: {feature}")
        cls._flags[feature] = True

    @classmethod
    def disable(cls, feature: str) -> None:
        if feature not in cls._flags:
            raise ValueError(f"Unknown feature: {feature}")
        cls._flags[feature] = False

    @classmethod
    def reset(cls) -> None:
        cls._flags = {
            "addition": True,
            "subtraction": False,
        }
