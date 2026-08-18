# colors.py

# RESET
RESET = "\033[m"

# TEXTO
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# FUNDO
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_PURPLE = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# ESTILOS
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
INVERT = "\033[7m"


def color_print(text, color="", bg="", style=""):
    """
    Imprime texto colorido.
    """
    print(f"{style}{color}{bg}{text}{RESET}")


# FUNÇÕES RÁPIDAS


def red(text):
    color_print(text, RED)


def green(text):
    color_print(text, GREEN)


def blue(text):
    color_print(text, BLUE)


def yellow(text):
    color_print(text, YELLOW)


def purple(text):
    color_print(text, PURPLE)


def cyan(text):
    color_print(text, CYAN)


def bold(text):
    color_print(text, style=BOLD)


def error(text):
    color_print(f"[ERROR] {text}", RED, style=BOLD)


def success(text):
    color_print(f"[SUCCESS] {text}", GREEN, style=BOLD)


def warning(text):
    color_print(f"[WARNING] {text}", YELLOW, style=BOLD)


def info(text):
    color_print(f"[INFO] {text}", CYAN)


def custom(text, color=WHITE, bg="", style=""):
    color_print(text, color, bg, style)
