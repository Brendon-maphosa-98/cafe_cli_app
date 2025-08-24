# Brendon's Cafe Mini Project  

## Table of Contents  

- [Project Background](#-project-background)  
- [Client Requirements](#-client-requirements)  
- [How to Run the App](#️-how-to-run-the-app)  
- [Unit Testing](#-unit-testing)   
- [Project Structure](#-project-structure)   

---

## Project Background  

The goal of this project is to create a **CLI-based cafe management app** with a clear and simple user interface. The app takes relevant inputs, produces meaningful outputs, and ensures that data persists over time.  

The project was developed iteratively, with **weekly client requirements** shaping its growth and complexity.  

---

## Client Requirements  

**Week 1**  
- Create a product and add it to a list  
- View all products  
- Update or delete a product  

**Week 2**  
- Extend functionality to include orders  
- Create, view, update, and delete products or orders  

**Week 3**  
- Add couriers in addition to products and orders  
- Update the status of an order  
- Persist product and courier data to txt files
- Update or delete a product, order, or courier  

**Week 4**  
- Persist **all data** (products, couriers, and orders) to CSV files  
- View orders filtered by **assigned courier** or **order status**  
- Full CRUD (Create, Read, Update, Delete) for products, couriers, and orders  

---

## How to Run the App  
download required packages
$py -m pip install -r requirements.txt

1. Navigate to the **Week 4 App Package** directory:  

   cd mini-project/week4/source/AppPackage_Week4
2. Run the main programe
   python3 masterLoop_module.py
3. Follow the onscreen prompts

---

## Unit Testing  

Unit tests are located in `test_app.py`.  
Currently, they focus on validating **user input functions**, ensuring that the app handles different types of user input reliably.  

In future, **more robust tests** could be added, including:  
- Integration tests  
- Database persistence tests  
- Automated CLI navigation tests  

---
## Project Structure

```plaintext
mini-project/
  week4/
    source/
      AppPackage_Week4/
        masterLoop_module.py         # Main app loop
        input_output_module.py       # Handles input/output
        data_module.py               # Data persistence logic connecting to the data files
        test_app.py                  # Unit tests
        products.csv                 # Data file for products menu
        couriers.csv                 # Data file for couriers menu
        orders.csv                   # Data file for orders menu
        loops_module.py              # Handles app loop around various menus and the main menu
        error_checking_module.py     # Input validation functions used throughout the app

