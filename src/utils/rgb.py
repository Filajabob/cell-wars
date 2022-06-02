from .constants import CONSTANTS


def rgb(r, g, b):
    if CONSTANTS["COLORS_ENABLED"]:
        return f"\u001b[38;2;{r};{g};{b}m"
    else:
        return ""
