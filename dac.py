#!/usr/bin/env python3
import random

cards = [
    {"name": "The Fool", "number": 0},
    {"name": "The Magician", "number": 1},
    {"name": "The High Priestess", "number": 2},
    {"name": "The Empress", "number": 3},
    {"name": "The Emperor", "number": 4},
    {"name": "The Hierophant", "number": 5},
    {"name": "The Lovers", "number": 6},
    {"name": "The Chariot", "number": 7},
    {"name": "Strength", "number": 8},
    {"name": "The Hermit", "number": 9},
    {"name": "Wheel of Fortune", "number": 10},
    {"name": "Justice", "number": 11},
    {"name": "The Hanged Man", "number": 12},
    {"name": "Death", "number": 13},
    {"name": "Temperance", "number": 14},
    {"name": "The Devil", "number": 15},
    {"name": "The Tower", "number": 16},
    {"name": "The Star", "number": 17},
    {"name": "The Moon", "number": 18},
    {"name": "The Sun", "number": 19},
    {"name": "Judgement", "number": 20},
    {"name": "The World", "number": 21}
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

    "The Lovers": r"""
    (♥‿♥) (♥‿♥)
     / ♥ \
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
    """
}

# Draw a random card
card = random.choice(cards)
name = card["name"]
number = card["number"]
art = llama_art.get(name, "(No llama yet!)")

# Build card content lines
card_lines = [
    f"✨ {name} ✨",
    "",
    *art.strip("\n").split("\n"),
    "",
    f"Card Number: {number}"
]

# Determine card width
max_width = max(len(line) for line in card_lines)
horizontal_border = f"┌{'─' * (max_width + 2)}┐"
bottom_border =    f"└{'─' * (max_width + 2)}┘"

# Print the card with a border
print()
print(horizontal_border)
for line in card_lines:
    print(f"│ {line.ljust(max_width)} │")
print(bottom_border)
print()

