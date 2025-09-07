# Cafe CLI App – Week 2  

## Table of Contents  

- [Project Background](#-project-background)  
- [Client Requirements](#-client-requirements)  
- [How to Run the App](#️-how-to-run-the-app)  
- [Unit Testing](#-unit-testing)  
- [Project Structure](#-project-structure)  

---

## Project Background  

The goal of this project is to create a **CLI-based cafe management app** with a clear and simple user interface. The app takes relevant inputs, produces meaningful outputs, and ensures that data persists over time.  

The project is developed iteratively, with **weekly client requirements** shaping its growth and complexity.  

This README reflects the state of the project at the end of **Week 2**.  

---

## Client Requirements – Week 2  

- Create a product or order and add it to the relevant list  
- View all products or orders  
- _STRETCH_ Update or delete a product or order  

Orders are now stored as **dictionaries** containing customer details and status, while products remain stored as simple strings.  

---

## How to Run the App  

1. Install required packages (if any):
  ``` bash
   py -m pip install -r requirements.txt
  ```
2. Navigate to the source directory:
  ``` bash
   cd src
  ```
3. Run the main program:
  ``` bash
   python3 masterLoop_module.py
  ```
4. Follow the onscreen prompts.
---

## Project Structure  

```plaintext
cafe_cli_app/
  notes/
    mini_project_week_2.md     # Weekly development notes
  src/
    data_module.py             # Data handling logic for lists & orders
    error_checking_module.py   # Input validation functions
    input_output_module.py     # Handles input/output
    loops_module.py            # Core menu loops
    masterLoop_module.py       # Main app loop entry point
    order_menu_module.py       # Handles order menu actions
    product_menu_module.py     # Handles product menu actions
    stringVariable_module.py   # Stores string constants
  .gitignore
  LICENSE
  cafe_cli_project_overview.md
  README.md
  requirements.txt
```