# 🐞 Live Website Testing & Interactive Bug Viewer

Welcome to the **Live Website Testing & Interactive Bug Viewer** repository. This project showcases a complete Software Quality Assurance (SQA) workflow, combining rigorous manual testing of a live digital platform with a custom-built desktop automation tool to organize and analyze test results efficiently.

## 🎯 Project Scope & Workflow
The workflow of this project is divided into two major phases:
1. **Live Platform Analysis:** Conducted a thorough functional, UI/UX, and responsiveness analysis on the live website `supportersframe.com`. A detailed, professional bug report was generated in Excel (`.xlsx`) format, mapping out critical system vulnerabilities, dead links, layout distortions, and functional failures.
2. **Desktop Application Development:** Built a standalone GUI tool in Python to act as a dynamic internal dashboard. Instead of viewing raw Excel rows, QA engineers or developers can load, sort, and inspect the documented bugs interactively.

## ✨ Core Features
* **Live Testing Dataset:** Powered by a real-world, structured bug report (`Bug_Report_Tamim.xlsx`) containing detailed steps to reproduce, expected vs. actual results, and severity mappings.
* **Interactive Data Table:** Displays bugs in a clean, professional grid with full support for column sorting (e.g., clicking the **Severity** header automatically bubbles up High-priority items first).
* **Deep-Dive Detail View:** Double-clicking any row launches a responsive pop-up modal displaying the full text wrapped beautifully for easy reading.
* **Smart Hyperlinks:** Embedded Google Drive screenshot links inside the pop-up modal are fully interactive; clicking them instantly launches the evidence in the system's default web browser.
* **Standalone Executable:** Compiled using absolute path handling into a single `.exe` file that runs seamlessly on any Windows environment without requiring a local Python setup.

## 🛠️ Technology Stack
* **Core Language:** Python 3.11
* **Graphical User Interface (GUI):** Tkinter & TTK
* **Data Engineering:** Pandas & Openpyxl (for seamless Excel dataset parsing)
* **Binary Compilation:** PyInstaller (configured with `--onefile` and `--windowed` arguments for optimized standalone distribution)

## 🚀 How to Run Locally

### Prerequisites
Ensure you have Python installed, then install the necessary dependencies via terminal:
```bash
pip install pandas openpyxl

git clone https://github.com/tamimshah/QA-Bug-Reporter-App

python Bug_Report_Tamim.py
