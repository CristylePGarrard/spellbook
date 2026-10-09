#!/bin/zsh

affirmations=(
  "You are the compiler of your destiny 🧵"
  "You refactor reality with every keystroke 🔥"
  "Bugs fear your breakpoint gaze 🐞"
  "Your logic is elegant, your flow unbreakable 🧠"
  "The terminal listens, and the code obeys ✨"
)

random=$(( $RANDOM % ${#affirmations[@]} ))
echo "\n🔮 ${affirmations[$random]}\n"
