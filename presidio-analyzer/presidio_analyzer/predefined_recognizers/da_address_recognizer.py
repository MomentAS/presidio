from typing import List, Optional

from presidio_analyzer import Pattern, PatternRecognizer


class DaAddressRecognizer(PatternRecognizer):
    """
    Recognize Danish street addresses using regex.

    Danish addresses typically follow this format:
    - Street name + number
    - Optional floor/apartment
    - Postal code (4 digits) + city

    :param patterns: List of patterns to be used by this recognizer
    :param context: List of context words to increase confidence in detection
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [
        # Pattern for street address with postal code
        Pattern(
            "Danish Address (Medium)",
            r"\b([A-ZÆØÅ][a-zæøå]+(?:\s[A-ZÆØÅ][a-zæøå]+)*)\s+(\d+[A-Z]?)(?:\s*,\s*(\d+\.\s*)?)?\s*(\d{4})\s+([A-ZÆØÅ][a-zæøå]+(?:\s[A-ZÆØÅ][a-zæøå]+)*)(?:\s+[ØNVSØ])?\b",
            0.7,
        ),
        # Pattern for just postal code and city
        Pattern(
            "Danish Postal Code (Medium)",
            r"\b(\d{4})\s+([A-ZÆØÅ][a-zæøå]+(?:\s[A-ZÆØÅ][a-zæøå]+)*)(?:\s+[ØNVSØ])?\b",
            0.5,
        ),
    ]

    CONTEXT = [
        "adresse",
        "gade",
        "vej",
        "alle",
        "plads",
        "torv",
        "bynavn",
        "postnummer",
        "postnr",
        "by",
        "adresse",
        "gadenavn",
        "vejnavn",
        "adressen",
        "gaden",
        "vejen",
        "alleen",
        "pladsen",
        "torvet",
        "bynavnet",
        "postnummeret",
        "postnret",
        "byen",
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        context: Optional[List[str]] = None,
        supported_language: str = "da",
        supported_entity: str = "DK_ADDRESS",
    ):
        patterns = patterns if patterns else self.PATTERNS
        context = context if context else self.CONTEXT
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        ) 