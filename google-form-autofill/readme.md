# 📝 Google Form Filling Automation

Automated Google Form filler built with **Python** and **Selenium**.  

>Developed by **Weber Developer** 🚀

This script automates the process of filling out Google Forms by randomly 
selecting multiple-choice/checkbox options with full support for forms that 
include selectable answers. 

If a question requires a written text response, 
a placeholder text `"answer"` will be submitted. To avoid irrelevant inputs, 
the script intelligently skips the last option when a question has more than 
two options (as this is usually the **"Other"** choice). 

It also supports 
**multi-page forms** and can run in both **visible browser** or **headless mode**.

---

## 📌 Features
- ✅ Automatically detects **multiple-choice** and **checkbox** inputs.  
- ✅ Handles **text inputs** and **textarea fields** with placeholder `"answer"`.  
- ✅ Skips "Other" option (last option when >2 choices).  
- ✅ Supports **multi-page forms** with "Next" navigation.  
- ✅ Runs multiple iterations (`loops`) for repeated submissions.  
- ✅ Headless mode for running without displaying the browser.  

## ⚙️ Requirements

Make sure you have the following installed:

1. **Python**: Version 3.7 or higher → [Download Python](https://www.python.org/downloads/)  
2. **Google Chrome Browser** → [Download Chrome](https://www.google.com/chrome/)  
3. **ChromeDriver**: Must match your installed Chrome version → [Get ChromeDriver](https://chromedriver.chromium.org/downloads)  
4. **Selenium Library**: Install via pip:
   ```bash
   pip install selenium


## 🚀 Usage Instructions

1. Clone this repository or save the script into a file named `form_filler.py`.

2. Open a terminal or command prompt in the project directory.

3. Run the script:
   ```bash
   python form_filler.py
   
- #### Example Run

    ```bash
    Enter google form url: https://sample-google-form-link.com
    Enter number of times to run: 1000  
    Show browser: (y / n): n  
  

## ‍💻 Developer

**Weber Developer**

- 💡 Passionate about automation, backend systems, and scalable applications.
- 📧 Contact: (add your preferred contact here if you want)