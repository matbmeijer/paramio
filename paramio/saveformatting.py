class SaveFormatting(dict):
    """
    If you try to access a key that doesn't exist, it will return the key surrounded by curly braces
    """

    def __missing__(self, key):
        return "{" + key + "}"
