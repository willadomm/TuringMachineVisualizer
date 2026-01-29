# Turing Machine Visualizer

A Python-based interactive visualizer for Turing Machines that allows you to step through computational processes and understand how these theoretical machines accept or reject strings.

## Overview

This project implements a Turing Machine simulator with a step-by-step visualization interface. It comes with four pre-configured machines that recognize different formal languages, making it an excellent educational tool for understanding computation theory.

## Features

- **Interactive step-through execution** - Watch each state transition in real-time
- **Fast-forward modes** - Skip ahead by a specific number of steps or jump to the end
- **Visual tape representation** - See the tape contents and read/write head position
- **Four example machines** - Pre-built Turing Machines for common languages
- **Input validation** - Ensures strings are in the correct alphabet
- **User-controlled pacing** - Press enter to advance or use fast-forward commands

## Available Turing Machines

### 1. At Least One '1' Machine
**Language:** Any string over the alphabet {0, 1}* that contains at least one '1'

**Example accepted strings:** `1`, `01`, `110`, `00100`  
**Example rejected strings:** `0`, `00`, `000`

### 2. a^n b^n c^n Machine
**Language:** Strings of the form a^n b^n c^n (equal numbers of a's, b's, and c's in that order)

**Example accepted strings:** `abc`, `aabbcc`, `aaabbbccc`  
**Example rejected strings:** `aabbc`, `abcc`, `bac`

### 3. Power of 2 Machine
**Language:** Strings where 'a' is repeated 2^n times (powers of 2)

**Example accepted strings:** `a`, `aa`, `aaaa`, `aaaaaaaa`  
**Example rejected strings:** `aaa`, `aaaaa`, `aaaaaa`

### 4. Palindrome Machine
**Language:** Any palindrome over the alphabet {a, b}*

**Example accepted strings:** `a`, `b`, `aba`, `abba`, `aabaa`, `babbab`  
**Example rejected strings:** `ab`, `aab`, `abab`, `aaab`

## Installation

1. Ensure you have Python 3.10+ installed
2. Clone or download this repository
3. No external dependencies required - uses only Python standard library

## Usage

Run the main program:

```bash
python main.py
```

### Basic Commands

When the visualizer starts:
- Press **Enter** to step through one transition at a time
- Type **C** to halt execution early
- Type **ff** to fast-forward to the end (use cautiously with non-halting inputs)
- Type **ff [number]** to fast-forward through a specific number of transitions (e.g., `ff 10`)

### Example Session

```
Welcome to the Turing Machine Visualizer. Enter the corresponding number to visualize that TM.
1. L = any string in the alphabet {0, 1}˟ that contains at least one 1.
2. L = any string of the form aⁿbⁿcⁿ.
3. L = a repeated a power of two times.
4. L = any palindrome in the language of {a, b}˟.
Type Here: 1

Please enter the string to be determined by the machine: 0101

Initial Tape:
|-0101
  ^

Press enter to begin:
[Press Enter to step through each transition]
```

## File Structure

- **`main.py`** - Entry point and menu interface
- **`turingmachine.py`** - Core Turing Machine class implementation
- **`machinecreation.py`** - Definitions of the four example machines
- **`customtm.py`** - (Work in progress) Custom Turing Machine builder

## How It Works

### Turing Machine Components

Each Turing Machine consists of:
- **States** - A finite set of states including start, accept, and reject states
- **Tape alphabet** - Symbols that can appear on the tape
- **Input alphabet** - Valid symbols for input strings
- **Transition function** - Rules for state changes based on current state and symbol
- **Tape** - An infinite (simulated) tape with a read/write head

### Transition Format

Transitions are defined as: `[current_state, read_symbol, next_state, write_symbol, direction]`

Example: `["q0", "1", "q1", "1", "R"]` means:
- In state `q0`, reading symbol `1`
- Transition to state `q1`
- Write symbol `1`
- Move head Right

## Implementation Details

- The tape is implemented as a Python list with automatic expansion
- Blank symbol: `_`
- Left end marker: `|-`
- Right end marker: `-|` (added when needed)
- Head position tracking with visual indicator (`^`)

## Known Limitations

- Non-total machines (machines that may not halt on all inputs) require manual termination with the 'C' command
- Tape visualization trims trailing blanks for readability
- Very long computations may take significant time even in fast-forward mode

## Educational Use

This visualizer is ideal for:
- Computer Science students learning about Turing Machines
- Understanding the Church-Turing thesis
- Visualizing formal language recognition
- Debugging custom Turing Machine designs

## Contributing

Feel free to add your own Turing Machines by creating new functions in `machinecreation.py` following the existing patterns.

## License

This project is open source and available for educational purposes.

## Author

Created as an educational tool for understanding computational theory and Turing Machines.
