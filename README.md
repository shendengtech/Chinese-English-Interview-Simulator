# Interview Simulator - Chinese/English (macOS System "say" Voice Reading)

This is a GUI-based interview question simulator built with `tkinter`, designed for macOS. It supports both Chinese and English question banks, standard answer display, question bank management (add/delete), automatic reading using the macOS `say` command (with multiple voices for selection), and local saving of the question bank. It is suitable for self-interview practice and oral exam training.

## Features

- Supports switching between Chinese and English question banks
- Allows custom adding/deleting of interview questions and standard answers
- The question bank is saved locally in `questions.json`
- One-click display of standard answers
- Uses the macOS `say` command to read questions and answers aloud (multiple voices available, supporting both Chinese and English)
- Friendly and intuitive GUI
- Automatic saving of the question bank; data is saved when the window is closed

## Environment

- OS: **macOS**
- Python 3.x
- Dependencies: `tkinter`

> **Note:**
> - The reading function depends on the macOS `say` command.
> - Windows and Linux users cannot use the voice reading feature.

## Quick Start

1. **Download the source code**  
   ```
   git clone https://github.com/your_username/interview-simulator.git
   cd interview-simulator
   ```

2. **Run the program**  
   ```
   python3 main.py
   ```
   > `main.py` refers to the code file above. Please adjust the filename based on how you saved it.

3. **Usage Instructions**  
   - By default, the program loads the `questions.json` question bank in the same directory. Sample questions will be generated on first use.
   - You can add new questions through the interface, supporting both Chinese and English.
   - After selecting the reading language and voice, click "Read Question" or "Read Standard Answer" to hear the audio.
   - You can delete the current question at any time.
   - Adding and deleting questions will be saved automatically.

## Example Screenshot

<img width="639" alt="截屏2025-05-19 下午10 30 00" src="https://github.com/user-attachments/assets/fdeb1168-987e-4d72-b68c-da5053b35386" />

## Question Bank Format

The question bank file is `questions.json`, formatted as follows:

```json
[
  {
    "question": "What is the difference between lists and tuples in Python?",
    "answer": "Lists are mutable, tuples are immutable."
  },
  {
    "question": "Python 中的列表和元组有什么区别？",
    "answer": "列表是可变的，元组是不可变的。"
  }
]
```

## License

This project is licensed under the [Apache License 2.0](LICENSE).

---

> **Contributions and suggestions are welcome!**
