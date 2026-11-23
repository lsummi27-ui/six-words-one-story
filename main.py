"""Six Words, One Story entry.

Writes exactly one six-word story to /output/entry.txt.
"""

from pathlib import Path

STORY = "He returned. Nobody remembered his name."


def main() -> None:
    story = STORY
    assert len(story.split()) == 6, "story must be exactly six words"
    for base in (Path("/output"), Path("output")):
        try:
            base.mkdir(parents=True, exist_ok=True)
            target = base / "entry.txt"
            target.write_text(story, encoding="utf-8")
            return
        except OSError:
            continue
    raise OSError("could not write /output/entry.txt")


if __name__ == "__main__":
    main()
