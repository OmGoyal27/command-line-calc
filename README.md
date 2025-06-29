# Command Line Calculator

A lightweight, feature-rich calculator that runs directly in your command line. Perfect for quick mathematical calculations without leaving your terminal.

## ✨ Features

- ✅ **Basic Arithmetic**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- ✅ **Advanced Operations**: Power (^), Modulo (%), Square Root (sqrt)
- ✅ **PowerShell Integration**: Run calculations using `=calc <equation>`
- ✅ **Calculation History**: Automatic tracking of all calculations
- ✅ **Interactive Mode**: Run calculations in a continuous session
- ✅ **Error Handling**: Division by zero and invalid input protection

## 📺 Demo

https://github.com/user-attachments/assets/6dff66c8-b3e7-45b5-9ac4-3a3e562bfac9

## 🚀 Quick Start

### Method 1: Direct Python Execution
```bash
# Interactive mode
python main.py

# Single calculation
python main.py "5 + 3"
```

### Method 2: PowerShell Integration
1. Follow the setup guide in [`Add to Powershell.md`](Add%20to%20Powershell.md)
2. Use anywhere in PowerShell:
```powershell
=calc 5 + 3
=calc 2^8  
=calc sqrt 16
=calc history
```

## 💻 Usage Examples

### Basic Operations
```bash
python main.py "10 + 5"     # Addition: 15
python main.py "20 - 8"     # Subtraction: 12
python main.py "6 * 7"      # Multiplication: 42
python main.py "15 / 3"     # Division: 5
```

### Advanced Operations
```bash
python main.py "2^10"       # Power: 1024
python main.py "17 % 5"     # Modulo: 2
python main.py "sqrt 25"    # Square root: 5
```

### History Tracking
```bash
python main.py "history"    # View all previous calculations
```

## 🛠️ Installation

1. **Clone or download** this repository
2. **Navigate** to the project directory:
   ```bash
   cd "Command line calculator"
   ```
3. **Run** the calculator:
   ```bash
   python main.py
   ```

### PowerShell Setup (Optional)
For seamless PowerShell integration, follow the detailed instructions in [`Add to Powershell.md`](Add%20to%20Powershell.md).

## 📁 Project Structure

```
Command line calculator/
├── main.py              # Core calculator logic
├── run.ps1              # PowerShell wrapper script
├── history.txt          # Calculation history (auto-generated)
├── Add to Powershell.md # PowerShell integration guide
├── README.md            # This file
├── license.txt          # MIT License
├── .gitignore          # Git ignore rules
└── docs/
    └── demo.mp4        # Demo video
```

## 🎯 Supported Operations

| Operation | Syntax | Example |
|-----------|--------|---------|
| Addition | `a + b` | `5 + 3` |
| Subtraction | `a - b` | `10 - 4` |
| Multiplication | `a * b` | `6 * 7` |
| Division | `a / b` | `15 / 3` |
| Power | `a^b` | `2^8` |
| Modulo | `a % b` | `17 % 5` |
| Square Root | `sqrt a` | `sqrt 25` |

## 🔮 Roadmap

- [x] Basic math equations
- [x] PowerShell integration via `=calc` command  
- [x] Power operations (x^y)
- [x] Modulo and square root operations
- [x] Calculation history tracking
- [ ] **AI Integration**: Advanced problem solving via Groq API
- [ ] **Scientific Functions**: Trigonometric and logarithmic functions
- [x] **Variable Storage**: Save and reuse values
- [ ] **Expression Parsing**: Support for complex expressions with parentheses

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [`license.txt`](license.txt) file for details.

## 👤 Author

**Om Goyal** - 2025

---

*Made with ❤️ for quick terminal calculations*