# 🩺 JSON Doctor

**A lightweight Python CLI tool for diagnosing and validating JSON files.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)
![JSON](https://img.shields.io/badge/Format-JSON-black?logo=json)

JSON Doctor helps developers identify JSON syntax errors and inspect malformed files directly from the command line. It provides clear error messages to make debugging faster and easier.

## ✨ Features

- 🔍 **JSON Validation** — Check whether JSON files contain valid syntax.
- 🚨 **Error Detection** — Identify syntax errors and report their locations.
- 📄 **File Handling** — Read and process JSON files using simple CLI commands.
- 💬 **Clear Error Messages** — Make JSON debugging easier with readable feedback.
- ⚡ **Lightweight** — Built entirely with Python's standard library.

## 🛠️ Built With

- **Python** — Core programming language.
- **argparse** — Command-line argument parsing.
- **json** — JSON parsing and validation.
- **pathlib** — File and path handling.

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/void-syntax/JSON-Doctor.git
```

Navigate to the project directory:

```bash
cd JSON-Doctor
```

No external dependencies are required.

## 🚀 Usage

Run the program:

```bash
python main.py
```

Validate a JSON file:

```bash
python main.py data.json
```

> Note: Adjust the command examples to match the actual arguments implemented in `main.py`.

## 📂 Project Structure

```text
JSON-Doctor/
├── main.py
├── result.json
├── README.md
├── LICENSE.txt
├── .gitignore
└── .gitattributes
```

## 🎯 Project Goals

JSON Doctor is a small command-line project focused on practical Python development, including:

- Working with files and directories.
- Handling exceptions.
- Parsing command-line arguments.
- Processing JSON data.
- Building useful developer tools.

## 📜 License

This project is licensed under the MIT License. See [LICENSE.txt](LICENSE.txt) for details.

---

**Made with Python by [void-syntax](https://github.com/void-syntax).**
