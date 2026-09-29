#!/usr/bin/env python3
# pylint: skip-file
"""
shitpost_generator.py
Generates the most brain-dead, uncivilized, and low-effort entries imaginable
to keep the GitHub grass green.
"""

import datetime
import random
import os

LEDGER_PATH = os.path.join(os.path.dirname(__file__), "SHITPOST.md")

ASCII_GRAVEYARD = [
    r"""
     (\__/)
     (•ㅅ•)  me touching virtual grass
    / 　 づ  so i never touch real grass
    """,
    r"""
       \  /
      .-""-.
    /  _  _  \   [BRAIN CELL NOT FOUND]
    | (o)(o) |   
    |   /\   |   OOG BOOG ME PUSH CODE
    \  =--=  /
     '-....-'
    """,
    r"""
    (╯°□°)╯︵ ┻━┻  (why write clean code when you can write trash)
    """,
    r"""
       /\_/\
      ( o.o )  <-- cat observing this dumpster fire
       > ^ <
    """,
    r"""
       [ 0% BRAIN USAGE DETECTED ]
       ===========================
         ( \ / )
         ( . .)   photosynthesis in progress...
         c(")(")
    """,
    r"""
         _________
        /         \
       /   REST    \
      /     IN      \
     /    PEACE      \
    |   CLEAN CODE    |
    |   2026 - 2026   |
    |                 |
    |_________________|
    """,
    r"""
    ( ͡° ͜ʖ ͡°)  another day, another green tile stolen from github
    """,
    r"""
       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
       █  SKIBIDI GIT  █
       █   GRASS FEED  █
       ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
              ||
           (  ಠ_ಠ )
    """
]

PHILOSOPHICAL_TRASH = [
    "If a commit is pushed to an empty forest and nobody reviews it, does it still turn the GitHub tile green? Yes. Yes it does.",
    "Why write 1000 lines of functional architecture when a single whitespace commit achieves the exact same green pixel?",
    "Today's intellectual epiphany: C++ stands for 'Crying ++'.",
    "Current status: 99.8% water, 0.2% caffeine, 100% uncivilized git streak addict.",
    "Real programmers optimize time complexity O(1). Legendary programmers optimize grass greenness O(daily).",
    "I hit the keyboard with a rock. Git accepted the patch. The CI pipeline approved. Society continues to crumble.",
    "Virtual grass touched. Sunlight avoided. Vitamin D deficiency secured.",
    "Doctors recommend 30 minutes of outdoor activity. I recommend 1 brain-dead push to main.",
    "Scientists confirm: pushing absolute garbage to GitHub stimulates the same dopamine receptors as finding clean water in prehistoric times.",
    "The repo is trash. The code is trash. But the streak? Immaculate.",
    "My code doesn't have bugs; it has surprise unplanned features with emotional issues.",
    "Today I breathed air, drank lukewarm water, and fed the green monster on my GitHub profile. Productive day.",
    "Archaeologists in the year 3050 will dig up this git log and classify our civilization as deeply confused.",
    "Caveman rule #1: Rock hard. Fire hot. Commit green.",
    "Commiting from the void. The void whispered back: 'Nice streak, bro'."
]

CAVEMAN_GRUNTS = [
    "OOG BOOG GRASS GREEN ME HAPPY",
    "UGGA CHUGGA GIT PUSH BRRRRRRR",
    "BONK KEYBOARD WITH SHARP STICK",
    "ME HUNGRY FOR GREEN SQUARE",
    "CLACK CLACK ENTER PUSH DONE ZZZZ",
    "BRAIN OFF. FINGERS FAST. TILE GREEN.",
    "OOF OOF AAH AAH MONKE CODE LEVEL ACHIEVED"
]

def generate_entry():
    now = datetime.datetime.now()
    timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
    
    ascii_art = random.choice(ASCII_GRAVEYARD).strip("\n")
    quote = random.choice(PHILOSOPHICAL_TRASH)
    grunt = random.choice(CAVEMAN_GRUNTS)
    brain_cells_left = random.randint(-100, 2)
    photosynthesis_rate = random.randint(9000, 99999)
    green_index = f"#{random.randint(10, 50):02x}{random.randint(180, 255):02x}{random.randint(10, 50):02x}"

    entry = f"""
### 🌿 Grass Feeding Session - {timestamp_str}

> **Caveman Verdict:** `{grunt}`  
> **Remaining Brain Cells:** `{brain_cells_left}` | **Photosynthesis Output:** `{photosynthesis_rate} lumens` | **Tile Color:** `{green_index}`

```text
{ascii_art}
```

**Deep Thoughts From The Dumpster:**
> *"{quote}"*

---
"""
    return entry

def main():
    if not os.path.exists(LEDGER_PATH):
        header = """# 🌿 The Sacred Brainrot Grass Ledger

Welcome to the bottom of the software engineering barrel.
This document exists for exactly one holy purpose: **to keep Heechan's GitHub grass aggressively green with the lowest effort humanly possible.**

No architectural reviews. No unit tests. No civilization. Only green tiles.

---
"""
        with open(LEDGER_PATH, "w", encoding="utf-8") as f:
            f.write(header)

    entry = generate_entry()
    with open(LEDGER_PATH, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"Generated new uncivilized shitpost entry at {datetime.datetime.now()}")

if __name__ == "__main__":
    main()
