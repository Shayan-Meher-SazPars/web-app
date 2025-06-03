# Minimal Python Browser with PyQt5

This is a simple Python desktop browser built with PyQt5 and QtWebEngineWidgets.  
It loads a fixed URL on startup and does not include any URL input or navigation controls.

---

## Features

- Loads a fixed webpage (`https://www.google.com`) on launch
- No URL input bar or navigation buttons — just a clean browser window
- Built using PyQt5 and QtWebEngine

---

## Requirements

- Python 3.6+
- PyQt5
- PyQtWebEngine

---

## Installation

```bash
pip install PyQt5 PyQtWebEngine
```

---

## Usage

Run the `browser.py` script:

```bash
python browser.py
```

---

## Customization

To change the startup URL, edit this line in `browser.py`:

```python
self.browser.setUrl(QUrl("https://www.google.com"))
```

Replace the URL with your desired webpage.

---

## License

This project is open source and free to use.
