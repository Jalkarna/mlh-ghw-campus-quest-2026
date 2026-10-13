# Copilot CLI Session

> [!NOTE]
> - **Session ID:** `5f6ce267-9844-4062-912b-2081e70b1414`  
> - **Started:** 10/13/2026, 8:26:08 PM  
> - **Duration:** 27s  
> - **Exported:** 10/13/2026, 8:26:35 PM  

---

<sub>4s</sub>

### User

Create a small Python 3 command-line choose-your-own-adventure game called Campus Quest in this directory for the MLH Global Hack Week GitHub Copilot challenge. It should have three meaningful choices, two winning endings, one losing ending, validation for invalid input, and a quit option. Use only the standard library. Put the complete runnable app in campus_quest.py and a short README with run instructions. Do not use subagents, contact services, modify anything outside this directory, or claim that it has been tested. Do not create tests. I will run it afterward.

---

<sub>7s</sub>

### `bash` — Failed

**Inspect project directory**

$ pwd && find . -maxdepth 2 -type f -print | sort

```
Permission to run this tool was denied due to the following rules: `shell`
```


---

<sub>9s</sub>

### `glob`

****/***

"**/*"

```
No files matched the pattern.
```


---

<sub>9s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/copilot-adventure.**

/home/ubuntu/mlh-hacktoberfest-work/copilot-adventure

<details>
<summary>6 lines</summary>

```diff

diff --git a/home/ubuntu/mlh-hacktoberfest-work/copilot-adventure b/home/ubuntu/mlh-hacktoberfest-work/copilot-adventure
create file mode 100644
index 0000000..0000000
--- a/dev/null
+++ b/home/ubuntu/mlh-hacktoberfest-work/copilot-adventure
@@ -1,0 +1,0 @@
```

</details>


---

<sub>22s</sub>

### `apply_patch`

<details>
<summary>Arguments</summary>

````json
"*** Begin Patch\n*** Add File: /home/ubuntu/mlh-hacktoberfest-work/copilot-adventure/campus_quest.py\n+\"\"\"Campus Quest: a small choose-your-own-adventure game.\"\"\"\n+\n+\n+def get_choice(prompt, options):\n+    \"\"\"Return a valid option, or None when the player chooses to quit.\"\"\"\n+    while True:\n+        answer = input(prompt).strip().lower()\n+\n+        if answer in {\"q\", \"quit\"}:\n+            return None\n+        if answer in options:\n+            return answer\n+\n+        print(\"Invalid choice. Enter 1, 2, or 3, or enter Q to quit.\")\n+\n+\n+def ending(title, message):\n+    print(f\"\\n=== {title} ===\")\n+    print(message)\n+\n+\n+def play():\n+    print(\"CAMPUS QUEST\")\n+    print(\"The clock is ticking: your team must present a demo at the\")\n+    print(\"MLH Global Hack Week showcase before sunset.\\n\")\n+\n+    first = get_choice(\n+        \"1) Search the library  2) Visit the makerspace  3) Ask the quad \"\n+        \"musician for advice (Q to quit): \",\n+        {\"1\", \"2\", \"3\"},\n+    )\n+    if first is None:\n+        ending(\"Quest Paused\", \"You head home to recharge. Maybe next time!\")\n+        return\n+\n+    if first == \"1\":\n+        print(\"\\nThe librarian finds an old campus map with a hidden shortcut.\")\n+        second_prompt = (\n+            \"1) Follow the shortcut  2) Copy the map for your teammates  \"\n+            \"3) Return the map and take the long route (Q to quit): \"\n+        )\n+    elif first == \"2\":\n+        print(\"\\nA maker lends you a microcontroller, but its battery is nearly empty.\")\n+        second_prompt = (\n+            \"1) Build a quick backup  2) Use the last battery immediately  \"\n+            \"3) Search the supply cabinet (Q to quit): \"\n+        )\n+    else:\n+        print(\"\\nThe musician offers a cryptic clue: 'Listen before you leap.'\")\n+        second_prompt = (\n+            \"1) Follow the loudest crowd  2) Listen for the quietest hallway  \"\n+            \"3) Ignore the clue and improvise (Q to quit): \"\n+        )\n+\n+    second = get_choice(second_prompt, {\"1\", \"2\", \"3\"})\n+    if second is None:\n+        ending(\"Quest Paused\", \"You step aside and save your energy for another adventure.\")\n+        return\n+\n+    if first == \"1\" and second == \"1\":\n+        print(\"\\nThe shortcut leads to a sunny courtyard where your team is waiting.\")\n+        third_prompt = (\n+            \"1) Rehearse the demo  2) Add one flashy feature  \"\n+            \"3) Ask the audience what they want to see (Q to quit): \"\n+        )\n+    elif first == \"2\" and second == \"3\":\n+        print(\"\\nYou find a spare battery and power up the prototype just in time.\")\n+        third_prompt = (\n+            \"1) Test every connection  2) Present immediately  \"\n+            \"3) Give the prototype to a stranger to test (Q to quit): \"\n+        )\n+    else:\n+        print(\"\\nYour route takes longer than expected, but the showcase tent is nearby.\")\n+        third_prompt = (\n+            \"1) Slow down and check the signs  2) Sprint to the tent  \"\n+            \"3) Follow a suspicious shortcut through the construction zone (Q to quit): \"\n+        )\n+\n+    third = get_choice(third_prompt, {\"1\", \"2\", \"3\"})\n+    if third is None:\n+        ending(\"Quest Paused\", \"You leave the campus safely. The quest can continue another day.\")\n+        return\n+\n+    if (first == \"1\" and second == \"1\" and third in {\"1\", \"3\"}) or (\n+        first == \"2\" and second == \"3\" and third == \"1\"\n+    ):\n+        ending(\n+            \"Victory!\",\n+            \"Your team delivers a confident demo, wins the showcase, and earns \"\n+            \"free pizza for the whole club.\",\n+        )\n+    elif first == \"2\" and second == \"3\" and third == \"2\":\n+        ending(\n+            \"Creative Victory!\",\n+            \"The demo is rough around the edges, but your bold presentation \"\n+            \"wins the audience award. Campus Quest complete!\",\n+        )\n+    else:\n+        ending(\n+            \"Quest Over\",\n+            \"The plan falls apart before the showcase. You learn from the \"\n+            \"mistakes and promise to try again tomorrow.\",\n+        )\n+\n+\n+if __name__ == \"__main__\":\n+    try:\n+        play()\n+    except EOFError:\n+        print(\"\\nQuest ended.\")\n*** Add File: /home/ubuntu/mlh-hacktoberfest-work/copilot-adventure/README.md\n+# Campus Quest\n+\n+Campus Quest is a small Python 3 choose-your-own-adventure game for the MLH\n+Global Hack Week GitHub Copilot challenge. Make three decisions to help a team\n+reach its showcase. Invalid entries are rejected, and you can quit at any\n+prompt with `q` or `quit`.\n+\n+## Run\n+\n+From this directory, run:\n+\n+```bash\n+python3 campus_quest.py\n+```\n+\n+The game uses only Python's standard library.\n*** End Patch\n"
````

</details>

```
Added 2 file(s): /home/ubuntu/mlh-hacktoberfest-work/copilot-adventure/campus_quest.py, /home/ubuntu/mlh-hacktoberfest-work/copilot-adventure/README.md
```


---

<sub>25s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/copilot-adventure/campus_quest.py.**

/home/ubuntu/mlh-hacktoberfest-work/copilot-adventure/campus_quest.py

<details>
<summary>94 lines</summary>

```
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
```

</details>


---

<sub>25s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/copilot-adventure/README.md.**

/home/ubuntu/mlh-hacktoberfest-work/copilot-adventure/README.md

<details>
<summary>11 lines</summary>

````
# Campus Quest

Campus Quest is a small Python 3 choose-your-own-adventure game for the MLH
Global Hack Week GitHub Copilot challenge. Make three decisions to help a team
reach its showcase. Invalid entries are rejected, and you can quit at any
prompt with `q` or `quit`.

## Run

From this directory, run:

```bash
python3 campus_quest.py
```

The game uses only Python's standard library.
````

</details>


---

<sub>27s</sub>

### Copilot

Created the complete Campus Quest app in:

- `campus_quest.py` — Python 3 CLI adventure with three choices, two winning endings, one losing ending, invalid-input validation, and quit support.
- `README.md` — brief description and run instructions using `python3 campus_quest.py`.

---

<sub>Generated by [GitHub Copilot CLI](https://github.com/features/copilot/cli)</sub>
