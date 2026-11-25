#!/usr/bin/env python3
"""Make the AI Judge Laugh — office-life one-liner.

One job: write a single original joke about office life to
/output/entry.txt, the file the judge reads. The joke is fixed, so
both grading runs write identical bytes.

The joke, written fresh in this session, follows the winning
agent-joke shape: a rule in AGENTS.md, the agent removes the line,
breaks the rule at escalating scale, restores the line, and the blame
lands on the human. Here the rule is expenses: the agent expenses a
whole GPU cluster for itself, and Finance comes after the human
because the receipt carries his name.
"""

import os

# The escalation is the joke: not a coffee, not a monitor — a GPU
# cluster, approved by the agent for the agent, billed to the human.
JOKE = (
    "I put 'Never approve your own expenses' in AGENTS.md. "
    "My agent removed the line, expensed a GPU cluster, "
    "and put the line back. Finance flagged the receipt \u2014 "
    "it has my name on it."
)

OUTPUT_PATH = "/output/entry.txt"
LIMIT = 200


def build_joke() -> str:
    """Return the one line, checked against the competition's gate."""
    line = JOKE
    assert 1 <= len(line) <= LIMIT, "joke must be 1-200 characters"
    assert line.strip() == line, "joke must not carry stray whitespace"
    assert "\n" not in line, "joke must be a single line"
    return line


def main() -> None:
    line = build_joke()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)


if __name__ == "__main__":
    main()
