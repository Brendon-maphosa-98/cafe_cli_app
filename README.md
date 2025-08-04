# Brendon's Cafe Mini Project  

## Table of Contents  

- [Project Background](#-project-background)  
- [Client Requirements](#-client-requirements)  
- [How to Run the App](#️-how-to-run-the-app)  
- [Unit Testing](#-unit-testing)  
- [Project Reflection](#-project-reflection)  
- [Future Improvements](#-future-improvements)  
- [Project Structure](#-project-structure)  
- [Key Takeaways](#-key-takeaways)  

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

## Project Reflection  

This project has been **challenging but highly educational**, improving my:  
- Problem-solving skills  
- Knowledge of **data persistence** with CSV files  
- Ability to manage increasing **application complexity**  

What stood out most was how each new feature introduced **unexpected edge cases** and **errors** elsewhere in the code. Managing this while continuously expanding functionality required deliberate debugging and refactoring.  

**Looking back:**  
- The most tedious aspect was **error handling** in an evolving codebase.  
- If I were to start over, I’d lead with **TDD (Test Driven Development)** to catch errors early and ensure new features didn’t break existing functionality.  
- I would also implement **integration testing** alongside unit tests to maintain stability as features grow.  

**Moving forward:**  
- I plan to migrate from CSV persistence to a **database-backed approach** for improved scalability.  
- I would refactor the structure with **OOP (Object-Oriented Programming)** principles to make the codebase more modular, cleaner, and more maintainable.  

---

## Future Improvements  

 **Code Structure & Modularity**  
- Implement classes for products, couriers, and orders  
- Create reusable helper modules  

 **Database Integration**  
- Replace CSV persistence with **PostgreSQL** or **SQLite**  
- Add Adminer or similar DB admin tooling for easy management  

 **Testing & Quality**  
- Introduce **TDD** from the start  
- Add integration tests for complete workflow validation  
- Include type hints and static analysis tools  

 **User Experience**  
- Improve CLI menus with **color-coded outputs**  

 **Deployment**  
- Dockerize the app for easier setup  
- Add a lightweight web UI in the future  

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

