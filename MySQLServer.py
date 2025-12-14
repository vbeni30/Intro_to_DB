import mysql.connector

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword"  # replace with your MySQL root password
    )
    cursor = conn.cursor()

    # Drop and create the database
    cursor.execute("DROP DATABASE IF EXISTS alx_book_store")
    cursor.execute("CREATE DATABASE alx_book_store")
    cursor.execute("USE alx_book_store")

    # Create Authors table
    cursor.execute("""
    CREATE TABLE Authors (
        author_id INT AUTO_INCREMENT PRIMARY KEY,
        author_name VARCHAR(215) NOT NULL
    )
    """)

    # Create Books table
    cursor.execute("""
    CREATE TABLE Books (
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(130) NOT NULL,
        author_id INT NOT NULL,
        price DOUBLE NOT NULL,
        publication_date DATE,
        CONSTRAINT fk_author
            FOREIGN KEY (author_id)
            REFERENCES Authors(author_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    )
    """)

    # Create Customers table
    cursor.execute("""
    CREATE TABLE Customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(215) NOT NULL,
        email VARCHAR(215) UNIQUE NOT NULL,
        address TEXT
    )
    """)

    # Create Orders table
    cursor.execute("""
    CREATE TABLE Orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT NOT NULL,
        order_date DATE NOT NULL,
        CONSTRAINT fk_customer
            FOREIGN KEY (customer_id)
            REFERENCES Customers(customer_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    )
    """)

    # Create Order_Details table
    cursor.execute("""
    CREATE TABLE Order_Details (
        orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
        order_id INT NOT NULL,
        book_id INT NOT NULL,
        quantity DOUBLE NOT NULL,
        CONSTRAINT fk_order
            FOREIGN KEY (order_id)
            REFERENCES Orders(order_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        CONSTRAINT fk_book
            FOREIGN KEY (book_id)
            REFERENCES Books(book_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    )
    """)

    # Commit changes
    conn.commit()
    print("Database and tables created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
