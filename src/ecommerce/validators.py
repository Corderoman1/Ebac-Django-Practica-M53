from django.core.exceptions import ValidationError



BLOQUED_WORDS = [
    "barato",
    "grátis",
    "malo"
]


def validate_blocked_words(value):
    init_string = f'{value}'.lower()
    unique_words = set(init_string.split())
    blocked_words = set(BLOQUED_WORDS)
    invalid_words = (unique_words & blocked_words)
    has_error = len(invalid_words) > 0
    if has_error:
        errors = []
        for invalid_word in invalid_words:
            msg = f'palabra "{invalid_word}" no permitida'
            errors.append(msg)
        raise ValidationError(errors)
    return value
