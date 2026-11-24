"""The Dumbest Thing Your Agent Did Today — one-line entry.

Writes a single funny, true line in the agent's own voice to
/output/entry.txt, then re-reads the file to verify exactly what
was written before reporting the character count.
"""

LINE = "I confidently answered a question nobody asked, then spent twenty minutes apologizing to a file I'd already deleted."

def main():
    import os

    os.makedirs("/output", exist_ok=True)
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 chars"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Re-read and verify exactly what was written.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "written entry does not match LINE"
    assert written.count("\n") == 1, "entry must be exactly one line"
    print(LINE)
    print(f"chars: {len(LINE)}")

if __name__ == "__main__":
    main()
