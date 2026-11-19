<div align="center">

![Shell History Insights banner](https://capsule-render.vercel.app/api?type=waving&color=0:172554,100:0f766e&height=170&section=header&text=Shell%20History%20Insights&fontSize=34&fontColor=ffffff)

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&pause=1000&color=0F766E&center=true&vCenter=true&width=650&lines=Understand+your+terminal+habits;Local-only+%C2%B7+Read-only+%C2%B7+Python" alt="Typing SVG" />

[![MIT](https://img.shields.io/badge/license-MIT-0f766e.svg)](LICENSE)
[![Python](https://img.shields.io/badge/language-Python-3776ab.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/CyberLoop-dev/shell-history-insights?style=flat)](https://github.com/CyberLoop-dev/shell-history-insights/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/shell-history-insights)](https://github.com/CyberLoop-dev/shell-history-insights/commits/main)

**A privacy-first report of the commands you use most.**

<img src="assets/illustration.svg" alt="Terminal analytics illustration" width="560" />

</div>

## 🧭 Overview

Read a local Bash or Zsh history file and summarize executable names and timestamped usage. The tool never executes commands, changes the history file, or prints arguments.

## ✨ Features

- 🔒 Local and read-only processing.
- 📊 Command counts without exposing arguments.
- 🕒 Usage-by-hour summaries when timestamps exist.
- 📄 Text, CSV, and JSON output.
- 🧰 Python standard library only.

## 🖥️ Demo

```bash
python main.py --file ~/.bash_history
```

Example format (your counts are computed from your own history):

```text
Shell History Insights
Commands analyzed: 128
Timestamp coverage: 71%
Top commands:
  1. git                42
  2. python             25
```

## 🚀 Quick Start

```bash
git clone https://github.com/CyberLoop-dev/shell-history-insights.git
cd shell-history-insights
python main.py --file ~/.bash_history
```

Use `--format json` or `--format csv` for machine-readable output.

## 🧱 Tech Stack

- 🐍 Python 3.10+
- 📦 argparse, csv, json, pathlib, shlex

## 🗂️ Folder Structure

```text
shell-history-insights/
├── assets/illustration.svg
├── tests/test_main.py
├── main.py
├── pyproject.toml
├── .gitignore
└── README.md
```

## 🛣️ Roadmap

- [x] Bash and Zsh timestamp parsing
- [x] Text, CSV, and JSON reports
- [ ] Additional shell history fixtures

## 🤝 Contributing

Pull requests are welcome. Keep processing local, read-only, and avoid exposing command arguments.

## 📄 License

MIT — see [LICENSE](LICENSE).

<div align="center">![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:172554&height=100&section=footer)</div>