#!/usr/bin/env python3
import random
import textwrap
import re
from colorama import init, Fore, Style
from wcwidth import wcswidth
import time
import itertools
import sys

init(autoreset=True)

spinner = itertools.cycle(["🔮", "✨", "🌙", "🌟", "🪄"])
for _ in range(20):
    sys.stdout.write("\rDrawing your card... " + next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
# print("\nYour card has been drawn!")

# Strip ANSI codes for alignment calculations
def strip_ansi(text):
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', text)

def visible_width(text):
    return wcswidth(strip_ansi(text))


textwrap.strip_ansi = strip_ansi  # Monkey-patch for convenience

cards = [
    {"name": "The Fool",
     "number": 0, "meaning": "Beginnings, possibilities, impulsiveness, innocence, a free spirit",
     "card_text": "The Fool rests on the pinnacle of a decision. She is ready to dive out of her "
                  "subconscious and into the physical world. To transform from an animal into a human. "
                  "She is carefree and excited by a new life, regardless of warnings.",
     "inspiration": "The Little Mermaid",
     "location": "Denmark",
     "source":"Danish Fairy Tale"},
    {"name": "The Magician",
     "number": 1, "meaning": "Originality, self-confidence, skill, a breakthrough, resourcefulness",
     "card_text": "The Magician is a helping hand. She has the ability to change raw materials into "
                  "something wonderful, and dreaming into doing. But she is only the helping hand; "
                  "it is up to the protagonist to use her support, moving forward to do the right thing.",
     "inspiration": "The Fairy Godmother",
     "location": "France",
     "source": "French Fairy Tale"},
    {"name": "The High Priestess",
     "number": 2, "meaning": "Wisdom, intuition, dreams, meandering, an enigma",
     "card_text": "The High Priestess is a keeper of vast knowledge. With a story for every situation. "
                  "Scheherazade asks the listener to focus on what their subconscious tells them, "
                  "encouraging them to form their own conclusions. Her power is vast yet subtle, "
                  "her answers always mysterious.",
     "inspiration": "Scheherazade",
     "location": "Turkey",
     "source": "Arabic Folk Tale"},
    {"name": "The Empress",
     "number": 3, "meaning": "Fertility, nurturing, accomplishment, nature, abundance",
     "card_text": "The Empress is a loving and protective mother. She cares for and wishes to "
                  "defend all of her children even if a mother's love can sometimes be smothering. "
                  "The world feels bright and everything blooms around her.",
     "inspiration": "Our Lady of Guadalupe",
     "location": "Mexico",
     "source": "Catholic Saint"},
    {"name": "The Emperor",
     "number": 4, "meaning": "Stability, leadership, bravery, bold action, structure",
     "card_text": "The Emperor is the ideal father figure. A warrior and a conqueror. "
                  "King Arthur rules over his kingdom and his sometimes unruly knights with "
                  "a just and firm hand. He unifies the fractious, defends the weak, and lends "
                  "his knowledge and understanding to all his subjects.",
     "inspiration":"King Author",
     "location": "Britain",
     "source": "Celtic Legend"},
    {"name":"The Hierophant",
     "number": 5,
     "meaning": "Conformity, compassion, social approval, tradition, legacy",
     "card_text": "The Hierophant is a divine figure and teacher who shares the rules, "
                  "rites and rituals to follow as a community. There is a place fore everyone, "
                  "and everyone in their place. She encourages the comfort and support of the group, "
                  "the path well-trodden.",
     "inspiration": "White Buffalo Woman",
     "location": "North Dakota",
     "source":"Lakota Deity"},
    {"name":"The Lovers",
     "number": 6,
     "meaning": "Love, harmony, trust, a leap of faith, choice",
     "card_text": "The Lovers card represents romance, opposites attracting. The duality and balance "
                  "of carnality, physicality and fire versus spirituality, emotion, and water. "
                  "Their pair emphasize the importance of communication and herald and important crossroads.",
     "inspiration": "The Beauty and the Beast",
     "location": "China",
     "source":"Danish Fairy Tale"},
    {"name":"The Chariot",
     "number": 7,
     "meaning": "A journey, perseverance, rushed decisions, vengence, victory",
     "card_text": "The Chariot is about harnessing emotions and charging down a straight, clear path. "
                  "Where the prince may have floundered before, he has learned from his mistakes and "
                  "now blazes forward confidently.",
     "inspiration": "The Three Princesses of Whiteland",
     "location": "Norway",
     "source":"Norwegian Fairy Tale"},
    {"name":"Strength",
     "number": 8,
     "meaning": "Courage, conviction, control, determination, patience",
     "card_text": "The Strength card is about willpower and determination. Focus, persistence and "
                  "the ability to confidently stare any challenge in the face and overcome it. "
                  "This is not physical strength, but a purity of heart and purpose",
     "inspiration": "Tam Lin",
     "location": "Scotland",
     "source":"Scottish Fairy Tale"},
    {"name":"The Hermit",
     "number": 9,
     "meaning": "Introspection, withdrawal, prudence, insight, meditation",
     "card_text": "The Hermit card represents solitude and leaving responsibilities behind to "
                  "focus inward. In the celtic myth, the elusive White Stag encourages people to "
                  "drop everything and pursue spirituality",
     "inspiration": "Druid and White Stag",
     "location": "Ireland",
     "source":"Celtic Legend"},
    {"name":"The Wheel of Fortune",
     "number": 10,
     "meaning": "Fortune, an unexpected windfall, karma, destiny, cycles",
     "card_text": "The Wheel of Fortune is endlessly running, spun by a trickster god. What was once luck "
                  "is now misfortune; what was hopeless is now joyous. These acts may seem random, "
                  "but all fates are part of an interconnected web of repercussions.",
     "inspiration": "Ahansi",
     "location": "Ghana",
     "source":"Akan Mythology"},
    {"name":"Justice",
     "number": 11,
     "meaning": "Harmony, balance, equality, virtue, honor",
     "card_text": "Justice is power wielded with both intelligence and impartiality. It is making decisions "
                  "with all of the facts ad accepting the consequences of any choice made. It is punishment "
                  "of the corrupt and promotion of the deserving.",
     "inspiration": "Amhaeng-Eosa",
     "location": "Korea",
     "source":"Korean Legend"},
    {"name":"The Hanged Man",
     "number": 12,
     "meaning": "Suspension, restriction, sacrifice, readjustment, improvement",
     "card_text": "The Hanged Man ceases forward momentum to avoid disaster ad instead favors reflection. "
                  "Sleeping Beauty is a symbol of stasis; with the options of sleep or death, "
                  "she chooses to wait for more favorable conditions",
     "inspiration": "Sleeping Beauty",
     "location": "Italy",
     "source":"Italian Fairy Tale"},
    {"name": "Death",
     "number": 13, "meaning": "Metamorphosis, evolution, lo0ss, transition, change",
     "card_text": "Death is a huge upheaval, potentially representing the death of one way of life and the start "
                  "of a new one. Life changes irrevocably, and there is no way to go back -- change is necessary. "
                  "The death of childhood is important in order to grow up. ",
     "inspiration": "White Bear King Valemon",
     "location": "Norway",
     "source": "Norwegian Fairy Tale"},
    {"name":"Temperance",
     "number": 14,
     "meaning": "Moderation, harmony, purpose, good influence, reconciliation",
     "card_text": "Temperance is about balance and mediation. It is being mutable recognizing when to "
                  "change with the times and when to change the situation itself. The Bodhisattva "
                  "Avalokiteshvara identities are fluid, but their goodwill remains constant",
     "inspiration": "Bodhisattva Avalokiteshvara",
     "location": "India",
     "source":"Buddhist Bodhisattva"},
    {"name":"The Devil",
     "number": 15,
     "meaning": "Greed, controversy, violence, strange experiences, addiction",
     "card_text": "The Devil gives into the ego, lusting for unnecessary or harmful things, "
                  "unwilling to leave negative situation. It is a dragon sitting upon a pile of gold "
                  "it does not need, a person setting a forest on fire for their own gain.",
     "inspiration": "Boitata",
     "location": "Brazil",
     "source":"Brazilian Mythology"},
    {"name":"The Tower",
     "number": 16,
     "meaning": "Massive change, upheaval, catastrophe, rebuilding, revelation",
     "card_text": "The Tower is about geeling safe and secure before everything is suddenly upended. "
                  "Beliefs are shattered, understandings ruptured, and everything is destroyed right "
                  "down to the very foundation. Perhaps the foundation was flawed to begin with.",
     "inspiration": "Rapunzel",
     "location": "Germany",
     "source":"German Fairy Tale"},
    {"name": "The Star",
     "number": 17,
     "meaning": "Hope, serenity, inspiratio, insight, spirituality",
     "card_text": "The Star is a symbol of hope after a disaster. The need to remain positive after "
                  "misfortune, to remember that things can get better again. It is staying calm and "
                  "open to future possibilities seeing your situation with open eyes, mind and heart.",
     "inspiration": "Sister Alyonushka and Brother Ivanushka",
     "location": "Russia",
     "source": "Russian Fairy Tale"},
    {"name": "The Moon",
     "number": 18,
     "meaning": "Trickery, melancholy, anguish, illusion, insecurity",
     "card_text": "The Moon is the subconscious and all its illusions, potential, pitfalls, and the "
                  "possibility of self-deception. Here, two tanukis -- shape-shifting racoon-like animals "
                  "-- each stare at a different moon, though it is not clear which is teh real one",
     "inspiration": "Princess Kaguya",
     "location": "Japan",
     "source" : "Japanese Fairy Tale"},
    {"name": "The Sun",
     "number": 19,
     "meaning": "Satisfaction, accomplishment, joy, luck, vitality",
     "card_text": "The Sun is success, birth, confidence after passing through difficult times. "
                  "Egyptian Sun God Ra proves everything is illuminated with optimism and enthusiasm "
                  "for the path ahead",
     "inspiration": "Sun God Ra",
     "location": "Egypt",
     "source": "Egyptian Deity"},
    {"name":"Judgement",
     "number": 20,
     "meaning": "Improvement, forgiveness, a change of perspective, absolution, rebirth",
     "card_text": "Judgement is the reckoning, an ending before the start of a new journey. "
                  "Past actions and decisions determine future events. If you haven't learned "
                  "your lessons you are doomed to repeat your mistakes over and over.",
     "inspiration": "Sun Wukong, The Monkey King",
     "location": "China",
     "source":"Chinese Mythology"},
    {"name": "The World",
     "number": 21,
     "meaning": "Completion, recognition, fulfillment, triumph, celebration",
     "card_text": "The World is the happily-ever-after ending following a difficult journey. "
                  "Hinemoa and Tutanekai represent the victorious conclusion, a positive outcome "
                  "most desired. However, a conclusion also herals the start of a new journey.",
     "inspiration": "Hinemoa and Tutanekai",
     "location": "New Zealand",
     "source": "Maori Legend"}
]
# Emoji art per card
emoji_art = {
    "The Fool": "🃏😄🎒🐕",
    "The Magician": "✨🧙‍♀️🪄🧠",
    "The High Priestess": "🌙👸📚💫",
    "The Empress": "🌸👑🤰🌿",
    "The Emperor": "🛡️👑🗡️🏛️",
    "The Hierophant": "📜🙏👨‍🏫🕊️",
    "The Lovers": "💑❤️🌹💫",
    "The Chariot": "🛻🏁🏹🏇",
    "Strength": "🦁💪🧘‍♀️🧡",
    "The Hermit": "🏞️🧙‍♂️🕯️🧘",
    "Wheel of Fortune": "🎡🔄🍀🎲",
    "Justice": "⚖️👩‍⚖️📏🧠",
    "The Hanged Man": "🙃⏸️🌳✨",
    "Death": "💀🦋🌑🌱",
    "Temperance": "⚗️🧘‍♂️🌈🏞️",
    "The Devil": "😈🔥🪤🍷",
    "The Tower": "🌩️🏰🔥💥",
    "The Star": "🌟🌌✨🕊️",
    "The Moon": "🌕🌙😵🌀",
    "The Sun": "🌞🌻👶🎉",
    "Judgement": "🎺⚰️🌅👼",
    "The World": "🌍🌐🎊🕊️"
}

def draw_card_back(width, height=10, pattern="🔮✨"):
    lines = []
    h_border = "+" + "-" * (width - 2) + "+"
    lines.append(h_border)
    for i in range(height - 2):
        # Alternate pattern to fill inside
        content = (pattern * ((width // len(pattern)) + 1))[:width - 2]
        lines.append("|" + content + "|")
    lines.append(h_border)
    return lines

def animate_flip(card_lines, back_lines, steps=5, delay=0.1):
    import os
    # card_lines = full card content (list of strings)
    # back_lines = back face (list of strings)
    max_width = max(len(line) for line in card_lines)
    height = len(card_lines)

    for step in range(steps):
        os.system('clear')
        # Calculate width shrink (goes down to 1)
        shrink_width = max_width - (step * (max_width // steps))
        if shrink_width < 1:
            shrink_width = 1
        # Print back face shrinking
        for i in range(height):
            line = back_lines[i]
            # Center crop line to shrink_width
            line_content = line[1:-1]  # remove border chars
            if shrink_width < 2:
                # Minimal width, print just borders
                print("|" + " " * (shrink_width - 2) + "|")
            else:
                start = (len(line_content) - shrink_width + 2) // 2
                cropped = line_content[start:start + shrink_width - 2]
                print("|" + cropped + "|")

        time.sleep(delay)

    # Expand back to full card (actual content)
    for step in range(steps):
        os.system('clear')
        expand_width = (step + 1) * (max_width // steps)
        if expand_width > max_width:
            expand_width = max_width
        for i in range(height):
            line = card_lines[i]
            # Crop or pad the line content to expand_width
            content = line[1:-1]
            if expand_width < 2:
                print("|" + " " * (expand_width - 2) + "|")
            else:
                start = max(0, (len(content) - expand_width + 2) // 2)
                cropped = content[start:start + expand_width - 2]
                print("|" + cropped.ljust(expand_width - 2) + "|")
        time.sleep(delay)

    # Finally print full card to ensure full display
    os.system('clear')
    for line in card_lines:
        print(line)


def draw_tarot_card(cards, wrap_width=60):
    card = random.choice(cards)

    name = card["name"]
    number = card["number"]
    meaning = card["meaning"]
    card_text = card["card_text"]
    inspiration = card["inspiration"]
    location = card["location"]
    source = card["source"]
    emoji_line = emoji_art.get(name, "🔮✨")

    # Center title
    title_line = f"{name} (Card #{number})".center(wrap_width)

    # Wrap and center meaning and text
    wrapped_meaning = [line.center(wrap_width) for line in textwrap.wrap(meaning, wrap_width)]
    wrapped_text = [line for line in textwrap.wrap(card_text, wrap_width)]

    # Footer
    footer_lines = [
        "",
        Fore.LIGHTMAGENTA_EX + f"Inspiration: {inspiration}",
        Fore.LIGHTMAGENTA_EX + f"Location: {location}",
        Fore.LIGHTMAGENTA_EX + f"Source: {source}"
    ]
def build_card_lines(name, number, meaning_lines, card_text_lines, footer_lines, emoji_line, width):
    lines = []
    h_border = "+" + "-" * (width - 2) + "+"
    lines.append(h_border)
    lines.append(f"|{name.center(width - 2)}|")
    lines.append("|" + " " * (width - 2) + "|")
    lines.append(f"|{emoji_line.center(width - 2)}|")
    lines.append("|" + " " * (width - 2) + "|")

    for line in meaning_lines:
        lines.append(f"|{line.ljust(width - 2)}|")
    lines.append("|" + " " * (width - 2) + "|")
    for line in card_text_lines:
        lines.append(f"|{line.ljust(width - 2)}|")
    lines.append("|" + " " * (width - 2) + "|")
    for line in footer_lines:
        lines.append(f"|{line.ljust(width - 2)}|")
    lines.append(h_border)
    return lines


def draw_tarot_card(cards, wrap_width=60):
    card = random.choice(cards)

    name = f"{card['name']} (Card #{card['number']})"
    meaning = card["meaning"]
    card_text = card["card_text"]
    inspiration = f"Inspiration: {card['inspiration']}"
    location = f"Location: {card['location']}"
    source = f"Source: {card['source']}"
    emoji_line = emoji_art.get(card["name"], "🔮✨")

    wrapped_meaning = textwrap.wrap(meaning, wrap_width)
    wrapped_card_text = textwrap.wrap(card_text, wrap_width)
    footer_lines = [inspiration, location, source]

    # Compute max width for card box
    max_content_width = max(
        [len(name), len(emoji_line)] +
        [len(line) for line in wrapped_meaning] +
        [len(line) for line in wrapped_card_text] +
        [len(line) for line in footer_lines]
    )
    width = max(wrap_width, max_content_width) + 4  # add padding for borders

    # Build card face lines
    card_lines = build_card_lines(name, 0, wrapped_meaning, wrapped_card_text, footer_lines, emoji_line, width)

    # Build card back lines
    back_lines = draw_card_back(width, height=len(card_lines), pattern="🔮✨")

    # Animate the flip
    animate_flip(card_lines, back_lines, steps=6, delay=0.08)


if __name__ == "__main__":
    draw_tarot_card(cards)

