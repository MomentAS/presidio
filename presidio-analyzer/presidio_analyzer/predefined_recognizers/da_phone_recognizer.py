from typing import List, Optional

from presidio_analyzer import Pattern, PatternRecognizer


class DaPhoneRecognizer(PatternRecognizer):
    """
    Recognize Danish phone numbers using regex.

    Danish phone numbers typically follow these formats:
    - Mobile: +45 2X XX XX XX or 2X XX XX XX
    - Landline: +45 XX XX XX XX or XX XX XX XX
    - Service numbers: 8X XX XX XX
    - Compact formats: +452XXXXXXX or 2XXXXXXX

    :param patterns: List of patterns to be used by this recognizer
    :param context: List of context words to increase confidence in detection
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [

        Pattern(
            "Danish Phone",
            r"(?:(?:\+|00)45\s?(?:\(0\)\s?)?)?(?:[2-9]\d{1}\s?\d{2}\s?\d{2}\s?\d{2}|[2-9]\d{3}\s?\d{4}|[2-9]\d{7})",
            0.6,
        )
    ]

    CONTEXT = [
        "telefon",
        "mobil",
        "nummer",
        "telefonnummer",
        "mobilnummer",
        "tlf",
        "tlf.",
        "mob",
        "mob.",
        "ring",
        "ringer",
        "opkald",
        "telefonopkald",
        "telefonnummeret",
        "mobilnummeret",
        "tlfnr",
        "mobnr",
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        context: Optional[List[str]] = None,
        supported_language: str = "da",
        supported_entity: str = "DK_PHONE",
    ):
        patterns = patterns if patterns else self.PATTERNS
        context = context if context else self.CONTEXT
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        ) 