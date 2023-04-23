from solution import truncate


def test():
    assert truncate('текст', 3) == 'тек...'
    assert truncate('и пошла вода', 5) == 'и пош...'