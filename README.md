# 🔢 Number Sum Project

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)
![License](https://img.shields.io/badge/License-Practice%20Project-yellow.svg)

> A simple and educational Python project for practicing coding skills that calculates the sum of individual digits in any given value.

## 📝 Description

This is a **beginner-friendly** Python project created as a learning exercise to understand string manipulation, list comprehensions, and mathematical operations. The project demonstrates how to extract and sum individual digits from any input value while excluding zeros.

Perfect for those starting their journey in **Python programming** and **algorithmic thinking**! 🐍

## 🎯 Purpose

This project was developed to:

- 📚 **Learn** string manipulation techniques in Python
- 🔍 **Practice** list comprehensions and filtering
- 🧮 **Understand** digit extraction from mixed data
- 🎓 **Master** basic function definition and usage

## ✨ Features

- 🔄 Converts any input to string format for processing
- 🔢 Extracts only numeric digits from the input
- 🚫 Excludes zero digits from the calculation
- ➕ Returns the sum of all non-zero digits
- 📊 Works with strings, numbers, and mixed character inputs

## 📁 Project Structure

```
number-sum/
├── 🐍 main.py              # Main Python script with the digit sum function
└── 📖 README.md            # This documentation file
```

## 🛠️ Requirements

![Python Version](https://img.shields.io/badge/Python-3.x-brightgreen)

### Core Dependencies:
- 🐍 **Python 3.x** - No additional packages required!

This project uses only **built-in Python functions** - perfect for beginners! 🎉

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/juansilvadesign/numberSum.git
cd numberSum
```

### 2️⃣ Navigate to Project Directory
```bash
cd "c:\xampp\htdocs\GitHub Projects\Personal\number-sum"
```

### 3️⃣ Ready to Use!
No additional installation required - just run the Python file! 🎯

## 💻 Usage

### 1️⃣ Import the Function
```python
from main import sum_single_digits
```

### 2️⃣ Use with Different Input Types
```python
# Example with string numbers
result = sum_single_digits("123456")
print(result)  # Output: 21 (1+2+3+4+5+6)

# Example with integers
result = sum_single_digits(789)
print(result)  # Output: 24 (7+8+9)

# Example with mixed characters
result = sum_single_digits("abc123def")
print(result)  # Output: 6 (1+2+3)

# Example with zeros (excluded)
result = sum_single_digits("10203")
print(result)  # Output: 6 (1+2+3, zeros ignored)
```

### 3️⃣ Run the Demo
```bash
python main.py
```

## 🔧 How it Works

The `sum_single_digits()` function follows these steps:

```python
def sum_single_digits(cell_value):
    # 1️⃣ Convert input to string
    cell_string = str(cell_value)
    
    # 2️⃣ Extract non-zero digits using list comprehension
    digits = [int(char) for char in cell_string if char.isdigit() and int(char) != 0]
    
    # 3️⃣ Calculate and return the sum
    return sum(digits)
```

**Step-by-step process:**
1. 🔄 **Converts** any input to string format
2. 🔍 **Filters** characters to find only digits
3. 🚫 **Excludes** zero digits from calculation
4. 🔢 **Converts** valid digits to integers
5. ➕ **Returns** the sum of all filtered digits

## 📋 Sample Output

When you run `main.py`, you'll see:

```
21
```

**Breakdown:**
- **Input:** "123456"
- **Process:** 1 + 2 + 3 + 4 + 5 + 6
- **Output:** 21 ✅

## 🎓 Learning Outcomes

Through this project, you can learn:

- 🔤 **String manipulation** in Python
- 📝 **List comprehensions** for data filtering
- 🔍 **Character type checking** with `.isdigit()`
- 🔄 **Type conversion** between strings and integers
- 🎯 **Function definition** and parameter handling
- 🚫 **Conditional filtering** in list comprehensions

## 🚀 Next Steps

To extend this project, you could:

- 🔢 Add support for decimal numbers
- 📊 Create a GUI interface
- 📈 Add statistical analysis of digits
- 🔄 Implement digit multiplication instead of sum
- ⚠️ Add input validation and error handling
- 📝 Create unit tests for the function
- 🎮 Build an interactive digit game

## 📌 Key Features Explained

> 🔍 **Digit Extraction:** Uses `char.isdigit()` to identify numeric characters  
> 🚫 **Zero Exclusion:** Filters out zeros with `int(char) != 0`  
> 📝 **List Comprehension:** Combines filtering and conversion in one line  
> 🔄 **Type Flexibility:** Works with any input type through string conversion

## 👨‍💻 Author

**Created by:** Juan Pablo  
**Purpose:** Personal coding practice and skill development  
**Date:** January 2023  
**Repository:** [numberSum](https://github.com/juansilvadesign/numberSum)

---

### 🌟 If you found this helpful for learning Python, please give it a star! ⭐

---

*Happy coding and keep practicing! 🎉*