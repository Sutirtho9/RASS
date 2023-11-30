# RASS (Rapid AI Speech System)

## Overview

RASS (Rapid AI Speech System) is a Python-based desktop voice assistant designed to enhance user interaction with the computer. It utilizes speech recognition, natural language processing, and text-to-speech capabilities to perform tasks such as fetching information from Wikipedia, opening web browsers, and providing time updates. The graphical user interface (GUI) allows users to activate RASS with a single click.

## Features

- **Voice Commands:** Interact with the assistant using natural language voice commands.
- **Wikipedia Integration:** Retrieve summarized information from Wikipedia.
- **Web Browsing:** Open specified websites with voice commands.
- **Time Updates:** Get real-time updates on the current time.
- **Customizable Appearance:** GUI with a customizable dark theme.

## Requirements

- Python 3.x
- SpeechRecognition library
- pyttsx3 library
- Wikipedia library
- Tkinter library

## Usage

1. Install the required libraries: `pip install SpeechRecognition pyttsx3 wikipedia`
2. Run the `main.py` file to activate RASS.
3. Click the "ACTIVATE RASS" button to start voice interaction.
4. Use voice commands to perform tasks.

## Configuration

- Change the appearance mode and color theme in the `customtkinter.set_appearance_mode` and `customtkinter.set_default_color_theme` functions.
- Modify the voice used by RASS in the `engine.setProperty('voice', voices[0].id)` line.

## Limitations

- Speech recognition accuracy may vary based on environmental factors.
- Limited email functionality (placeholder function).

## Future Enhancements

- Integration with additional applications and services.
- Advanced natural language understanding for more complex commands.
- Support for multiple languages.
- Improved error handling and user feedback.

## Contributors

- [Ayush 21BCS4922](https://github.com/Ayush-kathayat)
- [Rohit 21BCS4860](https://www.linkedin.com/in/rohit--kumar-/)
- [Shashi 21BCS4240](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.jacksonville.com%2Fstory%2Fspecial%2Fspecial-sections%2F2019%2F01%2F31%2Fjacksonville-zoo-baby-gorilla-with-deaf-mother-doing-well%2F6143660007%2F&psig=AOvVaw2eqw5B24LLMcXb1xBrZkz4&ust=1701410158179000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNimi_OE64IDFQAAAAAdAAAAABAE)
- [Sutirtho 21BCS4975](https://www.linkedin.com/in/sutirtho-chakravorty-239214231/)

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute and enhance RASS for a better desktop voice assistant experience!
