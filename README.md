# Install Python and Playwright on Linux Mint

## Prerequisites
Ensure your system is up to date:

```bash
sudo apt update && sudo apt upgrade -y
```

## 1. Install Python
Linux Mint typically comes with Python preinstalled. Check your version:

```bash
python3 --version
```

If Python is missing or outdated, install it:

```bash
sudo apt install python3 python3-pip -y
```

Verify `pip` installation:

```bash
pip3 --version
```

If `pip` is missing, install it:

```bash
sudo apt install python3-pip -y
```

## 2. Create a Virtual Environment 
To avoid dependency conflicts, create a virtual environment:

```bash
python3 -m venv playwright_env
source playwright_env/bin/activate
```

## 3. Install Playwright
Use `pip` to install Playwright:

```bash
pip install playwright
```

## 4. Install Playwright Browsers
Playwright requires browser binaries. Install them with:

```bash
playwright install
```

To install only Chromium (to save space):

```bash
playwright install chromium
```

## 5. Verify Installation
Run the following command to check if Playwright is installed correctly:

```bash
python -c "from playwright.sync_api import sync_playwright; print('Playwright installed successfully!')"
```

If no errors appear, the installation was successful.

## 6. (Optional) Install Playwright for Pytest
If you're using Pytest to run Playwright tests, install the Playwright plugin:

```bash
pip install pytest-playwright
```

Then, configure Playwright within your Pytest framework.

---

You're now ready to use Playwright on Linux Mint! 🚀

---

To run tests in parallel:

pip install pytest-xdist
then

```bash
pytest --numprocesses=4
```

---

install reporter 
pip install pytest-html

generate report with:
pytest --html=report.html
