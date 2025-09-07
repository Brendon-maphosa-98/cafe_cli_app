# Cafe CLI App – Week 4  

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

## Client Requirements – Week 4  

- Create a product, courier, or order (as a dictionary) and add it to a list  
- View all products, couriers, or orders  
- Update the status of an order  
- Persist all data to `.csv` files  
- _STRETCH_ Update or delete a product, order, or courier  
- _BONUS_ List orders by status or courier  

Products, couriers, and orders are now stored as **dictionaries**, and all data is persisted to CSV files for reliability. Orders include a list of product indexes and a courier index.  

---

## How to Run the App  

1. Install required packages (if any):  
   ```bash
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
  data/
    products3.csv              # Stores product dictionaries
    couriers3.csv              # Stores courier dictionaries
    orders3.csv                # Stores order dictionaries
  notes/
    mini_project_week_4.md     # Weekly development notes
  src/
    courier_menu_module.py     # Handles courier menu actions
    data_module.py             # Data persistence logic (CSV)
    error_checking_module.py   # Input validation functions
    input_output_module.py     # Handles input/output
    loops_module.py            # Core menu loops
    masterLoop_module.py       # Main app loop entry point
    order_menu_module.py       # Handles order menu actions
    product_menu_module.py     # Handles product menu actions
  tests/
    test_app.py                # Unit tests for input handling
  .gitignore
  LICENSE
  cafe_cli_project_overview.md
  README.md
  requirements.txt

```