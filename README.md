# Interview Simulator Pro (中英双语面试模拟器)

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)
![Last Updated](https://img.shields.io/badge/last%20updated-2025--05--19-brightgreen.svg)

A professional bilingual (Chinese/English) interview simulator for self-training, supporting real-time question addition/removal, standard answer display, and macOS system voice reading ("say" command), with persistent local storage and a user-friendly GUI.

![Application Screenshot](screenshots/app_screenshot.png)

## Features

- **Bilingual Support**: Switches seamlessly between Chinese and English interview question sets
- **macOS Voice Reading**: Uses the native `say` command for question/answer reading with multiple voice options
- **Easy Question Management**: Add and delete questions and standard answers with just a click
- **Persistent Storage**: All questions and answers are saved automatically to `questions.json`
- **Professional UI**: Clean, intuitive interface built with Tkinter
- **Instant Standard Answers**: One-click display of reference answers
- **Auto Save & Recovery**: Automatically saves your progress and question bank

## Requirements

- macOS (for voice function support)
- Python 3.7 or higher
- Required Python packages:
  ```
  tkinter (standard with Python on macOS)
  ```
  *No additional packages required for core features.*

## Installation

1. Clone the repository:
```bash
git clone https://github.com/shendengtech/Chinese-English-Interview-Simulator/blob/main/interview-simulator.py
```

2. (Optional but recommended) Create and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate (not recommended, voice not supported)
```

3. Run the application:
```bash
python3 interview-simulator.py
```

## Usage

- On first launch, the app will create a sample `questions.json` if none exists.
- Select your preferred language (Chinese/English) and voice.
- Add new questions and answers in either language.
- Use the "Read Question" and "Read Standard Answer" buttons for macOS system voice reading.
- Display standard answers instantly or delete current questions as needed.
- All changes are saved automatically.

## Configuration

- The question bank is stored in `questions.json` in the app directory.
- Default voices for Chinese: Tingting, Shanshan, Meijia, Sinji, etc.
- Default voices for English: Samantha, Daniel, Moira, Tessa, etc.
- Add or update voices in the `self.voice_options` dictionary in `main.py`.
- Maximum number of questions is unlimited.

## Technical Details

### Technology Stack
- Python 3.x
- Tkinter for GUI
- `say` command for macOS voice synthesis
- JSON for local storage

### Voice Synthesis
- Uses `subprocess.Popen` to call `say` with selected voice
- Supports adjustable speed and interruption (stop button)
- Only available on macOS

### Data Storage
- All questions and answers are saved in `questions.json`, UTF-8 encoded
- Automatic save on every add/delete and when closing the window

### Error Handling
- User input validation for empty questions/answers
- Friendly warnings and confirmations for deletion
- Graceful recovery from file read/write errors

## Contributing

1. Fork the repository
2. Create a new feature branch:
```bash
git checkout -b feature/your-feature
```
3. Commit your changes:
```bash
git commit -am 'Add your feature'
```
4. Push to your branch:
```bash
git push origin feature/your-feature
```
5. Submit a pull request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Voice technology provided by macOS `say`
- Built with Python and Tkinter

## Author

[shendengtech](https://github.com/shendengtech)

## Support

For support:
1. Check the [Issues](https://github.com/your_username/interview-simulator/issues) page
2. Open a new issue if your problem is not listed
3. Please include error messages and relevant environment details

---

*Last updated: 2025-05-19*
