# Cafe CLI App

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

---

## Client Requirements 

- Create a product and add it to a list  
- View all products  
- Update or delete a product  

---

## How to Run the App  

1. Install required packages (if any):
  ``` bash
   py -m pip install -r requirements.txt
  ```
2. Navigate to the source directory:
  ``` bash
   cd source
  ```
3. Run the main program:
  ``` bash
   python3 app.py
  ```
4. Follow the onscreen prompts.
---

## Project Structure  

```plaintext
cafe_cli_app/
  data/
    products.txt               # Stores product list data
    couriers.txt               # (placeholder for later weeks)
    orders.txt                 # (placeholder for later weeks)
  notes/
    mini_project_week_1.md     # Weekly development notes
  source/
    app.py                     # Main program entry point
  tests/
    __init__.py
    test_app.py                # Unit tests for input handling
  .gitignore
  LICENSE
  cafe_cli_project_overview.md
  README.md
  requirements.txt
```