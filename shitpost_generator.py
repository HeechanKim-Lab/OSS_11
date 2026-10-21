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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LEDGER_PATH = os.path.join(BASE_DIR, "SHITPOST.md")
BRAINROT_PATH = os.path.join(BASE_DIR, "daily_brainrot.txt")
COMMIT_MSG_PATH = os.path.join(BASE_DIR, ".git_commit_msg.txt")

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
    """,
    r"""
        (  .      )
       )           (     [ DUMPSTER FIRE ]
      (    (  .     )    status: burning nicely
       )     )    (      efficiency: 100%
     [===============]
     |   GARBAGE     |
     |   PIPELINE    |
     [===============]
    """,
    r"""
          ___
         /   \
        |  o  |  <-- a potato has more cognitive function
         \___/       than this git commit
    """,
    r"""
        [RETURN TO MONKE]
             __
        .-"''  ''"-.
       /            \
      |  (o)    (o)  |   🍌 BANANA CONSUMED
      |      /\      |   🟩 TILE GREENIFIED
       \    ====    /    💤 ME GO SLEEP
        '-..____..-'
    """,
    r"""
       .----------------.
      |  404 SANITY     |
      |  NOT FOUND      |
      |  COMMIT PUSHED  |
      '----------------'
             ||
         \(^Д^)/
    """,
    r"""
         \   /
          .-.
        ― ( ) ―   [QUANTUM PHOTOSYNTHESIS]
          `-’     Absorbing photons into GitHub commit squares...
         /   \
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
    "Commiting from the void. The void whispered back: 'Nice streak, bro'.",
    "I don't need a 401(k), I need a green GitHub contribution graph.",
    "CSS center a div? Impossible. Push trash to GitHub? Effortless.",
    "My code compiles because the compiler took pity on me.",
    "Eating crayons is a valid debugging strategy if you believe hard enough.",
    "Git blamed myself and honestly, git was right.",
    "DORA metrics status: Lead Time 0.001s, Deployment Frequency infinity, Change Failure Rate undefined (never had tests anyway).",
    "Why touch grass outside when grass inside screen never gives seasonal allergies?",
    "A smooth brain has no wrinkles, meaning zero friction for incoming thoughts.",
    "Keyboard goes clack, server goes ping, tile turns green, ape is king."
]

CAVEMAN_GRUNTS = [
    "OOG BOOG GRASS GREEN ME HAPPY",
    "UGGA CHUGGA GIT PUSH BRRRRRRR",
    "BONK KEYBOARD WITH SHARP STICK",
    "ME HUNGRY FOR GREEN SQUARE",
    "CLACK CLACK ENTER PUSH DONE ZZZZ",
    "BRAIN OFF. FINGERS FAST. TILE GREEN.",
    "OOF OOF AAH AAH MONKE CODE LEVEL ACHIEVED",
    "MONKE PRESS BUTTON MONKE GET DOPAMINE 🍌",
    "BRAIN SO SMOOTH IT REFLECTS SUNLIGHT ☀️",
    "UNGA BUNGA MERGE CONFLICT EAT ROCKS 🪨",
    "HIT LAPTOP SCREEN WITH HEAVY STONE ME FIX MERGE CONFLICT 🪨💻",
    "ME NO UNDERSTAND LINUS TORVALDS BUT ME PRESS PUSH 🌳"
]

COMMIT_MESSAGES = [
    "chore(grass): photosynthesis goes brrrr 🌿",
    "brainrot: unga bunga daily grass feeding 🦧",
    "fix(sanity): deleted 3 brain cells for optimal performance",
    "feat(vegetation): watered github tile with pure tears 🌿",
    "shitpost: low effort high yield green square guaranteed",
    "caveman: me hit keyboard rock rock clack green 🪨🌿",
    "refactor: rearranged dust particles in the repo",
    "style: added uncivilized spiritual aura to the codebase",
    "perf: optimized grass growth by yelling at git",
    "docs: updated manifesto on why this repo is peak engineering",
    "feat: photosynthesizing at 420 gigahertz",
    "chore: feeding the green square void",
    "brainrot: skibidi commit toilet algorithm v2.0",
    "ugga: oog oog commit pushed grass green me sleep",
    "fix: resolved bug where grass was insufficiently vibrant",
    "feat: aggressively staring at git log until commits appear",
    "chore: virtual grass touched, real grass safely avoided",
    "refactor: converted oxygen into pure git garbage",
    "feat: certified trash-tier contribution",
    "ci: automated brain-death protocol executed successfully",
    "feat(monke): smashed coconut against keyboard, git approved 🥥🌿",
    "chore(brainrot): 0iq quantum photosynthesis ritual initiated 🌿",
    "fix(entropy): added more chaos to an already ruined repository 📉",
    "refactor(void): screamed into the terminal until commit appeared 🗣️",
    "docs(crayons): delicious debugging nutrition acquired 🖍️",
    "feat(dopamine): hijacked github algorithm with absolute zero effort 🧠",
    "chore(potato): transferred life savings into green tile pixels 🥔",
    "fix(reality): git commit -m 'it is what it is' --force-sanity",
    "refactor(dora): elite tier deployment frequency achieved via pure garbage 📊",
    "feat(microtom): injected memes into rhizosphere amplicon pipeline 🧬",
    "chore(grass): touched keyboard instead of touching grass 🌱",
    "perf(brain): smooth brain aerodynamic efficiency +100% 🦧",
    "style(chaos): beautified dumpster fire with indentation 🗑️🔥",
    "feat(matrix): broke out of simulation to push 1 byte to git 🕶️",
    "docs(monke): return to monke protocol step 42: push to main 🍌",
    "chore(streak): sacrificial offering to the almighty contribution graph ⛩️",
    "feat(quantum): commit observed, wavefunction collapsed into green pixel ⚛️"
]

def generate_entry():
    now = datetime.datetime.now()
    timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
    
    ascii_art = random.choice(ASCII_GRAVEYARD).strip("\n")
    quote = random.choice(PHILOSOPHICAL_TRASH)
    grunt = random.choice(CAVEMAN_GRUNTS)
    brain_cells_left = random.randint(-150, 2)
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
    return entry, grunt, quote, brain_cells_left

def update_shitpost_ledger(entry):
    if not os.path.exists(LEDGER_PATH):
        header = """# 🌿 The Sacred Brainrot Grass Ledger

Welcome to the bottom of the software engineering barrel.
This document exists for exactly one holy purpose: **to keep Heechan's GitHub grass aggressively green with the lowest effort humanly possible.**

No architectural reviews. No unit tests. No civilization. Only green tiles.

---
"""
        with open(LEDGER_PATH, "w", encoding="utf-8") as f:
            f.write(header)

    with open(LEDGER_PATH, "a", encoding="utf-8") as f:
        f.write(entry)

def update_daily_brainrot_txt(commit_msg, brain_cells):
    now = datetime.datetime.now()
    today_str = now.strftime("%Y-%m-%d")
    
    statuses = [
        "Potato cognitive baseline achieved, rocks eaten",
        "Primate keyboard assault completed",
        "Monke hit keyboard with coconut 🥥",
        "0 IQ quantum photosynthesis ritual initiated",
        "Violently headbutting enter key to photosynthesize grass pixels",
        "Absolute zero / quantum brain death",
        "Dopamine receptor stimulated by green square"
    ]
    status = random.choice(statuses)

    entry = f"""
[{today_str}]
- Effort: Sub-zero negative cognitive density
- Status: {status}
- Brain cells remaining: {brain_cells}
- Message: {commit_msg}
"""
    with open(BRAINROT_PATH, "a", encoding="utf-8") as f:
        f.write(entry)

def write_commit_message(msg):
    now = datetime.datetime.now()
    body = f"Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S')} | Powered by Uncivilized Automation"
    with open(COMMIT_MSG_PATH, "w", encoding="utf-8") as f:
        f.write(f"{msg}\n\n{body}\n")

def main():
    entry, grunt, quote, brain_cells = generate_entry()
    chosen_msg = random.choice(COMMIT_MESSAGES)
    
    update_shitpost_ledger(entry)
    update_daily_brainrot_txt(chosen_msg, brain_cells)
    write_commit_message(chosen_msg)

    print(f"[SUCCESS] Generated uncivilized shitpost entry.")
    print(f"  - Message: {chosen_msg}")
    print(f"  - Ledger updated: {LEDGER_PATH}")
    print(f"  - Ledger updated: {BRAINROT_PATH}")
    print(f"  - Commit msg cached: {COMMIT_MSG_PATH}")

if __name__ == "__main__":
    main()
