#!/usr/bin/env python3
import random

cards = [
    {"name": "The Fool", "number": 0, "meaning": "New beginnings, spontaneity, free spirit"},
    {"name": "The Magician", "number": 1, "meaning": "Manifestation, resourcefulness, power"},
    {"name": "The High Priestess", "number": 2, "meaning": "Intuition, unconscious knowledge"},
    {"name": "The Empress", "number": 3, "meaning": "Fertility, beauty, nurturing"},
    {"name": "The Emperor", "number": 4, "meaning": "Authority, structure, fatherhood"},
    {"name": "Death", "number": 13, "meaning": "Transformation, endings, letting go"},
    {"name": "The Star", "number": 17, "meaning": "Hope, inspiration, renewal"},
    {"name": "The Moon", "number": 18, "meaning": "Illusion, fear, the subconscious"},
    {"name": "The Sun", "number": 19, "meaning": "Joy, success, vitality"},
    {"name": "The World", "number": 21, "meaning": "Completion, accomplishment, travel"}
]

llama_art = {
    "The Fool": r"""
      (o.o)
       >^<
    """,

    "The Magician": r"""
     /\_/\
    ( •_•)
     >⚡<
    """,

    "The High Priestess": r"""
     (\_/)
    ( •_•)
    /︿︿\
    """,

    "The Empress": r"""
    (•͡ᴗ•͡)
   <|:♕:|>
     | |
    """,

    "The Emperor": r"""
    (ò_ó)
    <|##|>
     / \
    """,

    "Death": r"""
    (x_x)
    /|💀|\
     / \
    """,

    "The Star": r"""
     ☆ﾟ.*･｡ﾟ
    (•‿•)
     /★\
    """,

    "The Moon": r"""
     🌙
    ( ._.)
    /|   |\
     / \
    """,

    "The Sun": r"""
     ☀️☀️
    (＾▽＾)
     \|/
     / \
    """,

    "The World": r"""
    (🌍)
    /|🌎|\
     / \
    """
}

# Draw a random card
card = random.choice(cards)
name = card["name"]
number = card["number"]
meaning = card["meaning"]
art = llama_art.get(name, "(no llama yet)")

# Build content lines
card_lines = [
    f"✨ {name} ✨",
    f"Card Number: {number}",
    "",
    *art.strip("\n").split("\n"),
    "",
    f"Meaning: {meaning}"
]

# Determine card width
max_width = max(len(line) for line in card_lines)
h_border = "+" + "-" * (max_width + 2) + "+"

# Print the "card" with a plain ASCII box
print()
print(h_border)
for line in card_lines:
    print(f"| {line.ljust(max_width)} |")
print(h_border)
print()

