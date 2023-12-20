import mysql.connector
from mysql.connector import Error
import bcrypt

def execute_query(sql, val=None):
    """Executes a SQL query and returns the results."""
    cursor = connection.cursor()
    try:
        cursor.execute(sql, val)
        connection.commit()
        results = cursor.fetchall()
        return True, results
    except Error as e:
        print(f"Error: {e}")
        return False, None
    finally:
        cursor.close()


    
#defining functions:

#--------------------------------LOGIN METHOD---------------------------------------------
def admin_login():
    username = input("Username: ")
    password = input("Password: ")

    sql = f"""
        SELECT * FROM admin
        WHERE Username = %s AND Password = %s
    """

    try:
        success, results = execute_query(sql, (username, password))

        if success and results:
            # Login successful
            print("Welcome, admin!")
            # ... perform subsequent actions
        else:
            print("Incorrect username or password!")
    except Error as e:
        print(f"Error: {e}")


def employee_login():
    username = input("Username: ")
    password = input("Password: ")

    # Hash the entered password
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    sql = """
        SELECT * FROM employee_resume
        WHERE Username = %s
    """

    try:
        # Use prepared statement
        success, results = execute_query(sql, (username,))

        if success and results:
            # Get user information from the first result
            user_data = results[0]

            # Compare hashed passwords
            if bcrypt.checkpw(password.encode(), user_data["Password"]):
                # Successful login
                print(f"Welcome, {user_data['FirstName']}!")
                # ... perform subsequent actions with user data
            else:
                print("Incorrect password!")
        else:
            print("Username not found!")
    except Error as e:
        print(f"Error: {e}")

def employee_login():
    username = input("Username: ")
    password = input("Password: ")

    # Hash the entered password
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    sql = """
        SELECT * FROM employee_resume
        WHERE Username = %s
    """

    try:
        # Use prepared statement
        success, results = execute_query(sql, (username,))

        if success and results:
            # Get user information from the first result
            user_data = results[0]

            # Compare hashed passwords
            if bcrypt.checkpw(password.encode(), user_data["Password"]):
                # Successful login
                print(f"Welcome, {user_data['FirstName']}!")
                # ... perform subsequent actions with user data
            else:
                print("Incorrect password!")
        else:
            print("Username not found!")
    except Error as e:
        print(f"Error: {e}")



def company_login():
    username = input("Username: ")
    password = input("Password: ")

    # Hash the entered password
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    sql = """
        SELECT * FROM company_details
        WHERE Username = %s
    """

    try:
        # Use prepared statement
        success, results = execute_query(sql, (username,))

        if success and results:
            # Get user data from the first result
            company_data = results[0]

            # Compare hashed passwords
            if bcrypt.checkpw(password.encode(), company_data["Password"]):
                # Successful login
                company_name = company_data["company_name"]
                print(f"Welcome, {company_name}!")
                # ... perform subsequent actions with company data
            else:
                print("Incorrect password!")
        else:
            print("Username not found!")
    except Error as e:
        print(f"Error: {e}")


#----------------------REGISTRATION METHOD------------------------------------------------------
def reg_employee():
    UserN = input("Enter username: ")
    UserP = input("Enter password: ")

    sql = """
        INSERT INTO employee_resume (Username, Password)
        VALUES (%s, %s)
    """

    val = (UserN, UserP)

    execute_query(sql, val)


def reg_comapany():
    UserN = input("Enter username: ")
    UserP = input ("Enter password: ")
    orgN = input("Enter company name: ")
    orgBriefDescription = input ("Enter a brief description about the comapny: ")
    orgvacancy = input("Enter number of job vacancies: ")
    orgContact = input("Company contact details: ")

    sql = """
        INSERT INTO company_details (Username, Password, company_name, brief-description, job_vacancy, contact)
        VALUES (%s, %s)
    """

    val = (UserN, UserP, orgN, orgBriefDescription, orgvacancy, orgContact)

    execute_query(sql, val)

#ACTION FOR THE MAIN SYSTEM
#-------------------view for employee and company-----------------------------------------------------
def employee_view():
    sql = """
        SELECT company_name, brief_description, job_vacancy, contact, possible-questions
        FROM company_details
        WHERE ... """
    val = None
    success, results = execute_query(sql, val)

    if success:
        if results:
            print("List of companies:")
            for company in results:
                print(f"\tCompany Name: {company[0]}")
                print(f"\tBrief Description: {company[1]}")
                print(f"\tJob Vacancies: {company[2]}")
                print(f"\tContact: {company[3]}")
                print(f"\tPossible Interview Questions: {company[4]}")
                print("---")
        else:
            print("No companies found matching your criteria.")
    else:
        print("Error retrieving company information. Please try again later.")

def company_view():
    sql = """
        SELECT Address, Age, Gender, background, contact_details
        FROM employee_resume
        WHERE ... """
    val = None
    success, results = execute_query(sql, val)
    if success:
            if results:
                # Process the retrieved data and present it to the company
                # e.g., display candidate profiles in a table or list format
                print("List of potential candidates:")
                for candidate in results:
                    print(f"\tAddress: {candidate[0]}")
                    print(f"\tAge: {candidate[1]}")
                    print(f"\tGender: {candidate[2]}")
                    print(f"\tBackground: {candidate[3]}")
                    print(f"\tContact Details: {candidate[4]}")
                    print("---")
            else:
                print("No candidates found matching your search criteria.")
    else:
        print("Error retrieving candidate information. Please try again later.")

def employee_profile():
    sql = """
    SELECT * FROM Username, LastName, FirstName, MiddleName, Address, Age, Gender, background, contact_details
    FROM employee_details
    """

def company_vacancy():
    sql = """
        SELECT Company_name, location, vacancy, classifications, salary, requirements
        FROM company_job_vacancy
        WHERE ... """
    val = None
    success, results = execute_query(sql, val)
    if success:
            if results:
                # Process the retrieved data and present it to the company
                # e.g., display candidate profiles in a table or list format
                print("List of potential candidates:")
                for candidate in results:
                    print(f"\tCompany Name: {candidate[0]}")
                    print(f"\tLocation: {candidate[1]}")
                    print(f"\tVacancy: {candidate[2]}")
                    print(f"\tClassifications: {candidate[3]}")
                    print(f"\tSalary: {candidate[4]}")
                    print(f"\tRequirements: {candidate[5]}")
                    print("---")
            else:
                print("No candidates found matching your search criteria.")
    else:
        print("Error retrieving candidate information. Please try again later.")

#search for a company----------------------------------------------
def employee_search():

    employee_search = input("Enter keywords: ")

    # Validate the product search term.
    if not employee_search:
        print("Please try again.")
        return

    # Define search fields and their comparison methods.
    search_fields = {
        "Company_name": "LIKE",  # Case-insensitive search
        "location": "LIKE",
        "vacancy": "LIKE",
        "classifications": "LIKE",  # Consider more specific matching like full-text search
        "salary": "BETWEEN %s AND %s",  # Use two placeholders for min and max salary
        "requirements": "LIKE",  # Consider more specific matching like full-text search
    }

    # Construct the SQL query with parameterized placeholders.
    sql = """
        SELECT *
        FROM company_job_vacancy
        WHERE ("""

    # Dynamically build clauses based on search terms and fields.
    for field, comparison in search_fields.items():
        if employee_search in field:
            sql += f" {field} {comparison} %s OR"

    # Remove the trailing "OR" and add closing parenthesis.
    sql = sql[:-2] + ")"

    # Define placeholders for search terms used in the final query.
    search_terms = tuple(employee_search.split())

    # Execute the query with parameterized values.
    success, results = execute_query(sql, search_terms)

    if success:
        if results:
            # Process and present the retrieved job vacancies.
            print("Found", len(results), "job vacancies matching your search:")
            for vacancy in results:
                # Display relevant information about each vacancy.
                pass
        else:
            print("No job vacancies found matching your search criteria.")
    else:
        print("Error retrieving job vacancies. Please try again later.")





try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='job_hunt_db'
    )

    def main():
        """
        The main function of the program.
        """
            # Establish database connection

        while True:
                # Display menu options
                print("+------------------+")
                print("   Job Hunt System   ")
                print("+------------------+")
                print("1. Log-in\n2. Register\n3. Exit")
                choice = int(input("Enter choice of action: "))

                # Handle user choices
                if choice == 1:
                    # Login for different user types
                    print("1. Admin Login\n2. Employee Login\n3. Company Login")
                    loginaction = int(input("Enter choice: "))
                    if loginaction == 1:
                        admin_login()
                    elif loginaction == 2:
                        employee_login()
                        print("1. View company details \n2. Search")
                        ask = input("Enter action: ")
                        while True:
                            if ask == 1:
                                employee_view()
                            elif ask == 2:
                                employee_search()
                            elif ask == 3:
                                print("Exit")
                                False
                            else:
                                print("Enter a valid choice!")
                    elif loginaction == 3:
                        company_login()
                        print("1. View Employee details \n2. ")
                        ask2 = input('Enter action: ')
                        while True:
                            if ask2 == 1:
                                company_vacancy()
                            elif ask2 == 2:
                                company_view()
                                
                    else:
                        print("Invalid choice.")
                elif choice == 2:
                    # Registration for different user types
                    print("1. Employee Registration\n2. Company Registration")
                    action1 = int(input("Enter choice: "))
                    if action1 == 1:
                        reg_employee()
                    elif action1 == 2:
                        reg_comapany()
                    else:
                        print("Invalid choice.")
                elif choice == 3:
                    # Exit the program
                    print("Good bye!")
                    break
                else:
                    print("Invalid choice.")
    main()
except Error as e:
    print(f"Error connecting to database: {e}")
    exit()
finally:
    # close connection as usual
    if connection:
        connection.close()