from pathlib import Path

# A string representing a file name. By default “Scores.txt”
SCORES_FILE_NAME = open(Path("Scores.txt"), "x")

# A number representing a bad return code for a function.
BAD_RETURN_CODE = int(400)


# A function to clear the screen.
def _screen_cleaner():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
