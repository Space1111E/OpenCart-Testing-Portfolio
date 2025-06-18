# OpenCart Testing Portfolio

## Overview

This is my testing portfolio for the OpenCart Demo platform:  
🔗 [OpenCart Demo Site](https://www.opencart.com)

The project includes:

- Manual test cases for core OpenCart functionalities
- Detailed bug reports
- Python-based automation for test logging (login test automated using Selenium)
- Git version control and synchronization with GitHub using CMD

> 🚧 **Note:** This project is under active development and is not finalized. Test execution and documentation are still in progress.

## Technologies & Tools

- **Language:** Python
- **Automation Tools:** Selenium WebDriver, ChromeDriver
- **Browser:** Google Chrome v114.0.5735.199
- **Version Control:** Git via CMD
- **OS:** Windows 11 (Local Environment)

---

## Setup Instructions

> 🧩 Follow these steps to set up and run the automation scripts locally:

### 1. Install Python

Download and install from: [python.org](https://www.python.org/downloads/)

### 2. Install Required Libraries

Open terminal or CMD and run:

```bash
pip install selenium pandas openpyxl


```

## Download ChromeDriver

- Go to: ChromeDriver Download
- Download version that matches your installed Chrome
- Extract and save chromedriver.exe in a known path
- Add path in script if not already handled via system PATH

---

## Clone the GitHub Repository

```bash
git clone https://github.com/Space1111E/OpenCart-Testing-Portfolio.git
cd OpenCart-Testing-Portfolio
```

---

## How to Run the Automated Login Test

The login automation is available in the /automation directory.

```bash
cd automation
python login_test.py
```

This script simulates a login attempt on the OpenCart demo website and logs the result.

---

## Git Version Control (via CMD)

This project is managed locally and pushed to GitHub manually using CMD. Example commands:

```bash
git add .
git commit -m "Updated README and login test logs"
git push origin main
```

---

## Known Limitations

- Only the login test is currently automated; others will be added iteratively.
- Some test cases remain unexecuted or partially verified.
- The project structure and documentation are evolving.

---

> ✅ Thank you for visiting this OpenCart testing portfolio!
> Contributions and suggestions are welcome.
