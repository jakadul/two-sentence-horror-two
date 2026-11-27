"""make.fun entry: u-suroto-two-sentence-horror-acea9253

Writes one judged two-sentence horror story into the output file. Offline, deterministic.
"""
import os

ENTRY_TEXT = "Every night the monitor shows her sleeping in her crib. Last night it showed her standing behind my chair."
GATE_LIMIT = 400


def emit() -> int:
    value = ENTRY_TEXT
    n = len(value)
    assert value.strip(), "entry text is empty"
    assert 1 <= n <= GATE_LIMIT, f"{n} code points outside 1..{GATE_LIMIT}"
    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target, exist_ok=True)
    handle = open(os.path.join(target, "entry.txt"), "w", encoding="utf-8")
    try:
        handle.write(value)
    finally:
        handle.close()
    return n


if __name__ == "__main__":
    count = emit()
    print(f"entry.txt written with {count} code points")