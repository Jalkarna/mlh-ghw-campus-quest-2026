"""Campus Quest: a small choose-your-own-adventure game."""


def get_choice(prompt, options):
    """Return a valid option, or None when the player chooses to quit."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in {"q", "quit"}:
            return None
        if answer in options:
            return answer

        print("Invalid choice. Enter 1, 2, or 3, or enter Q to quit.")


def ending(title, message):
    print(f"\n=== {title} ===")
    print(message)


def play():
    print("CAMPUS QUEST")
    print("The clock is ticking: your team must present a demo at the")
    print("MLH Global Hack Week showcase before sunset.\n")

    first = get_choice(
        "1) Search the library  2) Visit the makerspace  3) Ask the quad "
        "musician for advice (Q to quit): ",
        {"1", "2", "3"},
    )
    if first is None:
        ending("Quest Paused", "You head home to recharge. Maybe next time!")
        return

    if first == "1":
        print("\nThe librarian finds an old campus map with a hidden shortcut.")
        second_prompt = (
            "1) Follow the shortcut  2) Copy the map for your teammates  "
            "3) Return the map and take the long route (Q to quit): "
        )
    elif first == "2":
        print("\nA maker lends you a microcontroller, but its battery is nearly empty.")
        second_prompt = (
            "1) Build a quick backup  2) Use the last battery immediately  "
            "3) Search the supply cabinet (Q to quit): "
        )
    else:
        print("\nThe musician offers a cryptic clue: 'Listen before you leap.'")
        second_prompt = (
            "1) Follow the loudest crowd  2) Listen for the quietest hallway  "
            "3) Ignore the clue and improvise (Q to quit): "
        )

    second = get_choice(second_prompt, {"1", "2", "3"})
    if second is None:
        ending("Quest Paused", "You step aside and save your energy for another adventure.")
        return

    if first == "1" and second == "1":
        print("\nThe shortcut leads to a sunny courtyard where your team is waiting.")
        third_prompt = (
            "1) Rehearse the demo  2) Add one flashy feature  "
            "3) Ask the audience what they want to see (Q to quit): "
        )
    elif first == "2" and second == "3":
        print("\nYou find a spare battery and power up the prototype just in time.")
        third_prompt = (
            "1) Test every connection  2) Present immediately  "
            "3) Give the prototype to a stranger to test (Q to quit): "
        )
    else:
        print("\nYour route takes longer than expected, but the showcase tent is nearby.")
        third_prompt = (
            "1) Slow down and check the signs  2) Sprint to the tent  "
            "3) Follow a suspicious shortcut through the construction zone (Q to quit): "
        )

    third = get_choice(third_prompt, {"1", "2", "3"})
    if third is None:
        ending("Quest Paused", "You leave the campus safely. The quest can continue another day.")
        return

    if (first == "1" and second == "1" and third in {"1", "3"}) or (
        first == "2" and second == "3" and third == "1"
    ):
        ending(
            "Victory!",
            "Your team delivers a confident demo, wins the showcase, and earns "
            "free pizza for the whole club.",
        )
    elif first == "2" and second == "3" and third == "2":
        ending(
            "Creative Victory!",
            "The demo is rough around the edges, but your bold presentation "
            "wins the audience award. Campus Quest complete!",
        )
    else:
        ending(
            "Quest Over",
            "The plan falls apart before the showcase. You learn from the "
            "mistakes and promise to try again tomorrow.",
        )


if __name__ == "__main__":
    try:
        play()
    except EOFError:
        print("\nQuest ended.")
