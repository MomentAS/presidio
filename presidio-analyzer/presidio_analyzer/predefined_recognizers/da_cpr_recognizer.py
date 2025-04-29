from typing import List, Optional
from presidio_analyzer import Pattern, PatternRecognizer

class DaCprRecognizer(PatternRecognizer):
    """
    Recognize Danish CPR (Central Person Register) numbers using regex.

    The CPR number is a 10-digit number with the format DDMMYY-XXXX where:
    - DDMMYY is the date of birth
    - XXXX is a 4-digit sequence number
    - The last digit is a check digit

    :param patterns: List of patterns to be used by this recognizer
    :param context: List of context words to increase confidence in detection
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [
        Pattern(
            "CPR (Medium)",
            r"\b(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])(\d{2})-?(\d{4})\b",
            0.5,
        ),
    ]

    CONTEXT = [
        "cpr",
        "cpr-nummer",
        "personnummer",
        "fødselsdato",
        "fødselsnummer",
        "personnummer",
        "cpr nummer",
        "cprnr",
        "cpr nr",
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        context: Optional[List[str]] = None,
        supported_language: str = "da",
        supported_entity: str = "DK_CPR",
    ):
        patterns = patterns if patterns else self.PATTERNS
        context = context if context else self.CONTEXT
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )

