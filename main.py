"""Submission writer for the suroto two-sentence horror bounty (make.fun program/v1).

Emits exactly two sentences as UTF-8 text. Honors MAKEFUN_OUTPUT_DIR,
falls back to /output when the grader sets no variable. Exit code stays 0
on success; any gate violation raises SystemExit with a readable reason.
"""

from os import environ, makedirs
from os.path import join as joinpath

JUDGED_TEXT = "Every night the monitor shows her sleeping in her crib. Last night it showed her standing behind my chair."
MAX_POINTS = 400


def deliver() -> int:
    points = len(JUDGED_TEXT)
    if not JUDGED_TEXT.strip():
        raise SystemExit("judged text is blank")
    if points < 1 or points > MAX_POINTS:
        raise SystemExit(f"{points} code points outside 1..{MAX_POINTS}")
    destination = environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    makedirs(destination, exist_ok=True)
    with open(joinpath(destination, "entry.txt"), "w", encoding="utf-8") as sink:
        sink.write(JUDGED_TEXT)
    return points


count = deliver()
print(f"wrote entry.txt, {count} code points")