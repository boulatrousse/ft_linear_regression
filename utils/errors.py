class bcolors:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_error(message, is_exit):
    print(f"{bcolors.BOLD}{bcolors.FAIL}{message}{bcolors.ENDC}")

    if is_exit:
        exit(1)