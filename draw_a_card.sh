#!/bin/bash

cards=(
  "🌞 The Sun — Clarity, optimism, and vitality shine on your day."
  "🌚 The Moon — Trust your intuition, but beware illusion."
  "🃏 The Fool — A new journey begins. Embrace the unknown."
  "⚖️ Justice — Fairness and truth will guide your choices."
  "🪦 Death — Transformation awaits. Shed the old."
  "💀 The Tower — Expect the unexpected. Rebuild stronger."
  "🌿 The Empress — Nurture creativity. Growth is near."
  "🧙 The Magician — You have all the tools. Time to act."
  "🧘 The Hermit — Seek solitude. Answers lie within."
  "🎡 Wheel of Fortune — Things are changing. Ride the wave."
)

card_index=$((RANDOM % ${#cards[@]}))

echo
echo "🔮 You draw a card from the deck..."
sleep 1.5
echo
echo "${cards[$card_index]}"
echo

