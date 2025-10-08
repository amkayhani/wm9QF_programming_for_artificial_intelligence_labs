<!--
module_id: sqlite
author: David Croft
email: david.croft@warwick.ac.uk
version: 0.0.1
current_version_description: a
module_type: standard
language: en
narrator: UK English Female
mode: Textbook
title: SQLite

comment:  a

long_description: a

estimated_time_in_minutes: ?

@pre_reqs
Familiarity with basic SQL concepts (such as tables, rows, and columns) and experience answering SQL-related questions is recommended. You should also have some experience with Python programming, including writing simple scripts and using libraries. No advanced SQL or Python knowledge is required.
@end

@learning_objectives  
- Understand how to connect to and interact with SQLite databases using Python
- Explain the benefits of using the Python Database API Specification (PEP 249)
- Demonstrate how to create tables, insert, update, and query data in SQLite from Python
- Use context managers and transactions (`commit`, `rollback`) for safe database operations
- Apply best practices for executing parameterized queries to prevent SQL injection
- Compare different methods for retrieving query results (`fetchall`, `fetchmany`, `fetchone`)
- Recognize common pitfalls when writing SQL queries in Python and how to avoid them
@end

good_first_module: false
data_domain: ehr
data_task: data_wrangling
collection: learn_to_code
coding_required: true
coding_level: basic
coding_language: sql
sequence_name: sql

@version_history
Previous versions: 
@end

import: ../module_templates/macros.md
import: https://dscroft.github.io/Pyodide/README.md
mport: https://github.com/LiaScript/CodeRunner/blob/master/README.md


@create_sqlite_db
```python @Pyodide.exec
import sqlite3, os

filename = "sqlite.db"

with sqlite3.connect(filename) as con:
    con.execute("DROP TABLE IF EXISTS users;")
    con.execute("CREATE TABLE users (id integer PRIMARY KEY AUTOINCREMENT, username text, password text, firstname text, lastname text, address text, city text, county text, postal text, phone text, email text);")
    con.execute("INSERT INTO users VALUES (1000,'Trout393','steal3','Aleshia','Tomkiewicz','14 Taylor St','St. Stephens Ward','Kent','CT2 7PP','01835-703597','atomkiewicz@hotmail.com');")
    con.execute("INSERT INTO users VALUES (1017,'Pigeon729','nose8','Evan','Zigomalas','5 Binney St','Abbey Ward','Buckinghamshire','HP11 2AX','01937-864715','evan.zigomalas@gmail.com');")
    con.execute("INSERT INTO users VALUES (1034,'Aardwolf536','party9','France','Andrade','8 Moor Place','East Southbourne and Tuckton W','Bournemouth','BH6 3BE','01347-368222','france.andrade@hotmail.com');")
    con.execute("INSERT INTO users VALUES (1051,'Stoat334','brown0','Ulysses','Mcwalters','505 Exeter Rd','Hawerby cum Beesby','Lincolnshire','DN36 5RP','01912-771311','ulysses@hotmail.com');")
    con.execute("INSERT INTO users VALUES (1068,'Toucan875','ought3','Tyisha','Veness','5396 Forth Street','Greets Green and Lyng Ward','West Midlands','B70 9DT','01547-429341','tyisha.veness@hotmail.com');")

f"Creating {filename} {"successful" if os.path.exists(filename) else "unsuccessful"}."
```
@end

@style
.flex-container {
    display: flex;
    flex-wrap: wrap; /* Allows the items to wrap as needed */
    align-items: stretch;
    gap: 20px; /* Adds both horizontal and vertical spacing between items */
}

.flex-child { 
    flex: 1;
    margin-right: 20px; /* Adds space between the columns */
}

@media (max-width: 600px) {
    .flex-child {
        flex: 100%; /* Makes the child divs take up the full width on slim devices */
        margin-right: 0; /* Removes the right margin */
    }
}
@end

@create_demo_db
``` python @Pyodide.exec
from contextlib import closing, suppress
import os
import sqlite3

filename = "@0"
data = (("row1_col1", "row1_col2"),
        ("row2_col1", "row2_col2"),
        ("row3_col1", "row3_col2"))

with suppress(FileNotFoundError):
    os.remove(filename)

with closing(sqlite3.connect(filename)) as con:
    con.execute("CREATE TABLE table_name (col1 text, col2 text);")
    con.executemany("INSERT INTO table_name VALUES (?, ?);", data)

    con.execute("CREATE TABLE other_table (col1 text, col2 text);")
    con.executemany("INSERT INTO other_table VALUES (?, ?);", data)

f"Creating {filename} {"successful" if os.path.exists(filename) else "unsuccessful"}."
```
@end

@create_product_db
``` python @Pyodide.exec
import os, sqlite3
from contextlib import closing

filename = "@0"

product_data = [("Product A", 10.0, 100),
                ("Product B", 15.0, 200),
                ("Product C", 20.0, 300)]

user_data = [("Alice",1000),
             ("Bob",2000),
             ("Charlie",3000)]

with closing(sqlite3.connect(filename)) as con:
    with con:        
        q1 = """
        CREATE TABLE IF NOT EXISTS "orders" (
            "id"	INTEGER NOT NULL,
            "user_id"	INTEGER NOT NULL,
            "product_id"	INTEGER NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT),
            FOREIGN KEY("product_id") REFERENCES "products"("id"),
            FOREIGN KEY("user_id") REFERENCES "users"("id")
        );"""

        q2 = """
        CREATE TABLE IF NOT EXISTS "products" (
            "id"	INTEGER NOT NULL UNIQUE,
            "name"	TEXT NOT NULL,
            "price"	NUMERIC NOT NULL,
            "quantity"	INTEGER NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
        );"""

        q3 = """
        CREATE TABLE IF NOT EXISTS "users" (
            "id"	INTEGER NOT NULL UNIQUE,
            "name"	TEXT NOT NULL,
            "credit" NUMERIC NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
        );"""

        con.execute(q1)
        con.execute(q2)
        con.execute(q3)

        con.executemany("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?);", product_data)
        con.executemany("INSERT INTO users (name, credit) VALUES (?, ?);", user_data)

f"Creating {filename} {"successfull" if os.path.exists(filename) else "unsuccessful"}."
```
@end


@create_users_db
```python @Pyodide.exec 
from contextlib import closing, suppress
import os
import sqlite3

filename = "users.db"

data = [('Trout393','steal3'),
    ('Pigeon729','nose8'),
    ('Aardwolf536','party9'),
    ('Stoat334','brown0'),
    ('Toucan875','ought3')]

with closing(sqlite3.connect(filename)) as con:
    con.execute("""CREATE TABLE users 
            (id integer PRIMARY KEY AUTOINCREMENT, 
             username text, 
             password text);""")
    con.executemany("INSERT INTO users (username, password) VALUES (?, ?);", data)
    con.commit()

f"Creating {filename} {"successful" if os.path.exists(filename) else "unsuccessful"}."
```
@end


@basic_import
<div style="display: none;">
```python @Pyodide.exec
import sqlite3
from contextlib import closing
```
</div>
@end

link:  ../assets/styles.css
import: ../module_templates/macros.md
import: ../module_templates/macros_sql.md

-->

# Demo

```python
import sqlite3

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE demo (value TEXT UNIQUE);")

try:
  with con:
    con.execute("INSERT INTO demo VALUES ('example1');")
    con.execute("INSERT INTO demo VALUES ('example2');")
    con.execute("INSERT INTO demo VALUES ('example1');")
except sqlite3.IntegrityError as e:
    print(f"Error while inserting: {e}")

with con:
    print("Table contents: ")
    print(con.execute("SELECT * FROM demo;").fetchall())

con.close()
```
@Pyodide.eval


```python
import sqlite3

con = sqlite3.connect(":memory:")

cur1 = con.cursor()
cur2 = con.cursor()

cur1.execute("CREATE TABLE demo (value TEXT);")
cur1.execute("INSERT INTO demo VALUES ('example1');")
cur1.execute("INSERT INTO demo VALUES ('example2');")
cur1.execute("INSRT INTO demo VALUES ('example3');")

print( cur2.execute("SELECT * FROM demo;").fetchall() )

con.close()
```
@Pyodide.eval


# SQL and Python

Accessing SQL databases from a programming language is essential skill for many dynamic, data-driven applications. Here are some key reasons why this is relevant and important:

- **Data Storage and Retrieval:** Most applications need to store, retrieve, and manipulate data efficiently. Databases provide a structured way to manage large volumes of data, while programming languages allow you to interact with this data programmatically.

- **Automation:** By accessing databases through code, you can automate repetitive tasks such as data entry, updates, reporting, and analytics, reducing manual effort and minimizing errors.

- **Integration:** Applications often need to combine data from multiple sources or systems. Programming languages enable you to connect to different databases, integrate data, and build unified solutions.

- **Scalability and Flexibility:** Code-based access allows you to scale your application, handle complex business logic, and adapt to changing requirements more easily than manual database management.

- **Security and Validation:** Programming languages provide mechanisms to validate user input, enforce business rules, and implement security controls before interacting with the database, helping to protect sensitive data.

- **User Interaction:** Most modern applications have user interfaces that require real-time interaction with data. Accessing databases from code enables features like search, filtering, and personalized content.

In summary, accessing databases from a programming language bridges the gap between raw data storage and practical, interactive applications, making it a fundamental skill for developers.


## Python

Python has significant benefits for database access over older languages such a Java, C or C++.
In those languages you would typically need to use an external library to access the database and the functionality of said library would vary from database to database.

In Python, Guido van Rossum (Python's benevolent dictator for life), has made it a priority to ensure that Python has a standard interface for database access. 
This means that you can use the same code to access different databases, such as SQLite, MySQL, PostgreSQL, and others.
This is done through the [Python Database API Specification](https://www.python.org/dev/peps/pep-0249/), which defines a standard interface for database access in Python. 
PEP 249 means that you can use the same code to access different databases, and you can easily switch between databases without having to change your code.

There may be additional functionality that is specific to a particular database, but the core functionality of connecting to a database, executing queries, and retrieving results is the same across all databases.
This means that that the concepts you learn hear are directly applicable to any other database engine you may use in the future.


## SQLite

SQLite is a lightweight, serverless SQL database engine that is widely used for local data storage in applications. It is particularly useful for mobile and desktop applications, as well as for small to medium-sized web applications. 

SQLite databases are stored in a single file, making them easy to manage and deploy.
This distinguishes SQLite from client-server databases like MySQL or PostgreSQL, which require a server to run and manage the database and support the full range of functionality that is typically expected from a database, i.e. multi-user access, transactions, and so on.

However, if you are looking to store a moderate amount of data to be accessed by a single application, SQLite is a great choice. It is easy to set up, requires no configuration, and has a small footprint.

We are using SQLite for these activities for exactly these reasons. 
We do not need a full client-server database to demonstrate the concepts of SQL and database access in Python, and SQLite allows us to do this without the overhead of setting up a server or managing a complex database system.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

There have been multiple versions of SQLite since its initial release in 2000. 
At time of writing the latest version is 3.50.3, released in July 2025.
As long as you are not working across major versions, i.e. SQLite 2.x with SQLite 3.x, you should not have issues with compatibility.

</div>

### SQLite in Python

To use SQLite in Python, you use the `sqlite3` module. 
This module provides a simple and easy-to-use interface for working with SQLite databases.

The main difference between accessing a SQLite database and a client-server database such as MySQL or PostgreSQL is that you do not need to set up a server to run the database. Instead, you can create a SQLite database file and access it directly from your Python code.

<section class="flex-container">

<div class="flex-child" style="min-width: 300px;">

**Accessing a MySQL database in Python**

```python
import mysql.connector

details = {'user':     'username', 
           'password': 'password', 
           'host':     'url_or_ip_address', 
           'database': 'database_name'}

# create a connection to the database
con = mysql.connector.connect(**details)
cur = con.cursor()

# execute a query
cur.execute("SELECT * FROM table_name")

# fetch the results
for row in cur:
    print(row)

# close the connection
con.close()
```

</div>

<div class="flex-child" style="min-width: 300px;">

**Accessing a SQLite database in Python**

```python
import sqlite3






# open the database files
con = sqlite3.connect('demo.db')
cur = con.cursor()

# execute a query
cur.execute("SELECT * FROM table_name")

# fetch the results
for row in cur:
    print(row)

# close the file
con.close()
```

</div>
</section>


<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

In sqlite if you specify a file that does not exist it will be created for you.
The newly created database will be empty, i.e. it will not contain any tables or data.

Therefore if you want to ensure that you are working with an existing database, you should check that the file exists before trying to open it. E.g. using the `os.path.exists()` function.

</div>


### :memory: databases

One piece of functionality possessed by SQLite that is not typical of other databases is the ability to create an in-memory database.
This means that the database is created in RAM and does not persist to disk.

Scenarios where this might be useful include:

- Testing code that interacts with a database, without having to create a file on disk.
- Prototyping a database schema or queries without having to create a file on disk.
- Storing temporary data that is only needed for the duration of a program's execution, such as caching results or storing intermediate data.
- Running a database in a web application that does not require persistent storage, such as a simple web app that only needs to store data for the duration of a user's session.

To create an in-memory database, you can use the special database name `:memory:` when connecting to the database instead of a filename.

```python
con = sqlite3.connect(":memory:")
```

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Remember, nothing is saved to disk when using an in-memory database. 
When the connection is closed, the database and all of its contents are lost.

</div>


# Python Database API

As discussed previously, the standard interface for database access in Python means that although the examples given may use SQLite, identical code can be used to access other databases such as MySQL or PostgreSQL, with only minor changes to the connection details.

In this section we will look at the main components of the Python Database API with examples.

## Connections

A connection is an object that represents a connection to a database.
In Python, you can create a connection object using the `connect()` method of the `sqlite3` module.

If you need to connect to multiple databases, you can create multiple connection objects, one for each database.

It is important to close the connection when you are done with it, as this will free up resources and ensure that any changes made to the database are saved.
This is done using the `close()` method of the connection object when you are done.

----------------------------

@basic_import

**Explicit connection management**

```python
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("SELECT sqlite_version();")
print(cur.fetchall())
con.close()
```
@Pyodide.eval



## Commit and rollback

When working with databases, it is important to ensure that changes made to the database are saved correctly.

This is done using transactions, which are a way to group multiple changes together and ensure that they are either all saved or all discarded.

This is useful when you are making multiple changes to the database and want to ensure that they are all saved correctly, or if you want to discard all changes if there is an error.

For example, if a user is purchasing an item from an online store using store credit.
Multiple changes need to be made to the data:

- The user's store credit balance needs to be reduced by the amount of the purchase.
- The item quantity needs to be decreased.
- A new order record needs to be created.

It is important that either all of the changes are successful or none of them are successful. 
If any of the actions fail then the database should be rolled back to the state it was in before the transaction started.

- `commit()` is used to save all changes made during the transaction.
  - Will generally be used if all changes were successful.
- `rollback()` is used to discard all changes made during the transaction.
  - Will generally be used if there was an error and you want to discard all changes.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

`commit()` and `rollback()` execute the `COMMIT` and `ROLLBACK` SQL commands respectively.
There is nothing stopping you from running these using the `execute()` method of the connection or cursor object, but it is not very Pythonic.

</div>

---------------------

Let's look at an example.
In this example we are creating a table with a unique constraint on the `value` column and then trying to add three rows, two of which are identical and will therefore violate the unique constraint causing an error.

@basic_import

```python
con = sqlite3.connect(":memory:")

con.execute("CREATE TABLE demo (value TEXT UNIQUE);")

try:
    con.execute("INSERT INTO demo VALUES ('example1');")
    con.execute("INSERT INTO demo VALUES ('example2');")
    con.execute("INSERT INTO demo VALUES ('example1');")
except sqlite3.IntegrityError as e:
    print(f"Error while inserting: {e}")
else:
    print("Everything is fine")

print(f"Rows in table:", con.execute("SELECT * FROM demo;").fetchall())

con.close()
```
@Pyodide.eval

As you can see, the error occurs when we try to insert the second 'example1' row, but the first two rows are still in the table leaving our data partially inserted.

Try and modify the code to ensure that either all the rows are inserted or none of them are.

<details>
<summary>**Still stuck?  Click to see our solution!**</summary>

<br/>

<div class = "answer">

Here's the code we used:

```python
con = sqlite3.connect(":memory:")

con.execute("CREATE TABLE demo (value TEXT UNIQUE);")

try:
    con.execute("INSERT INTO demo VALUES ('example1');")
    con.execute("INSERT INTO demo VALUES ('example2');")
    con.execute("INSERT INTO demo VALUES ('example1');")
except sqlite3.IntegrityError as e:
    print(f"Error while inserting: {e}")
    con.rollback()
else:
    print("Everything is fine")
    con.commit()

print(f"Rows in table:", con.execute("SELECT * FROM demo;").fetchall())

con.close()
```
@Pyodide.eval

</div>

</details>


### Context manager approach

All of this does add a fair amount of boilerplate code that has to be included repeatedly, but we can simplify this.

Instead of calling `commit()` and `rollback()` explicitly, we can use a `with` statement to handle this for us.

@basic_import

```python
con = sqlite3.connect(":memory:")

con.execute("CREATE TABLE demo (value TEXT UNIQUE);")
try:
    with con:
        con.execute("INSERT INTO demo VALUES ('example1');")
        con.execute("INSERT INTO demo VALUES ('example2');")
        con.execute("INSERT INTO demo VALUES ('example1');")
except sqlite3.Error as e:
    print(f"Error while inserting: {e}")

print(f"Rows in table:", con.execute("SELECT * FROM demo;").fetchall())
```
@Pyodide.eval

-------------------------------------

We can also use a context manager to handle the connection itself but this is slightly more complex.

We need to explicitly tell python to call the `.close()` method of the connection object instead of just tidying up the transaction with `commit()` or `rollback()` as we have seen previously.


```python
from contextlib import closing

with closing(sqlite3.connect(":memory:")) as con:
    con.execute("SELECT sqlite_version();")

try:
    con.execute("SELECT sqlite_version();")
except sqlite3.Error as e:
    print(f"Error: {e}")
```
@Pyodide.eval




## Cursors

Using the connection object directly to execute queries is fine for simple queries, but for more complex queries it is better to use a cursor.
In Python, you can create a cursor object using the `cursor()` method of the connection object.

@basic_import

```python
con = sqlite3.connect("sqlite.db")
cur = con.cursor()

cur.execute("SELECT * FROM table_name;")
rows = cur.fetchall()
```

Cursors allow us to have more finely grained control over the interaction with the database and execution of queries. 
In particular, creating multiple cursors also allows you to execute multiple queries and read multiple sets of results in parallel, as each cursor maintains its own state and results.

@create_product_db(cursor_example.db)

```python
with closing(sqlite3.connect("cursor_example.db")) as con:
    cur1 = con.cursor()
    cur2 = con.cursor()

    cur1.execute("SELECT * FROM users;")
    cur2.execute("SELECT * FROM products;")

    for i in range(3):
        print(f"Cursor 1, Row {i}: {cur1.fetchone()}")
        print(f"Cursor 2, Row {i}: {cur2.fetchone()}")
```
@Pyodide.eval




## Query gotchas

When writing SQL queries in Python, there are a few common gotchas that you should be aware of.
These predominantly relate to how strings are handled in Python and SQL, and can lead to errors or unexpected behavior if not handled correctly or if you are not aware of them.



### " and '

When writing SQL queries in Python, you will need to be careful about how you use quotes.
In SQL, you can use either single quotes (`'`) or double quotes (`"`) to define string literals.
In Python, you also can also use single and double quotes to define string literals.

The problem occurs when you are defining a string literal in Python containing a SQL query, and that query also contains string literals.
You can end up with a situation where the quotes in the SQL query conflict with the quotes in the Python string.

For example:

```python 
query = "SELECT * FROM products WHERE product_type = "FRUIT";"

query = 'SELECT * FROM products WHERE product_type = 'FRUIT';'
```

There are a few solutions to this problem:

**Different quotes**

Use single quotes for the SQL query and double quotes for the string literal in Python, or vice versa.

```python
query = "SELECT * FROM products WHERE product_type = 'FRUIT';"

query = 'SELECT * FROM products WHERE product_type = "FRUIT";'
```

----------------------

**Escape quotes**

You can escape the quotes in the SQL query using a backslash (`\`).
This works for both single and double quotes.
This can affect readability of the query, but it is worth mentioning that if you are writing a SQL query that contains \ (backslashes) you will need to escape those.

```python
# escaping quotes in a Python string
query = "SELECT * FROM products WHERE product_type = \"FRUIT\";"

# escaping backslashes in a Python string, searching for C:\Users\
query = "SELECT * FROM files WHERE file_path LIKE \"C:\\Users\\%\";"
```

-----------------------

**Triple quotes**

You can use triple quotes to define a multi-line string in Python, which allows you to use both single and double quotes without escaping them.

Triple quotes can be either `'''` or `"""`.

```python
query = """SELECT * FROM products WHERE product_type = "FRUIT";"""

query = '''SELECT * FROM products WHERE product_type = 'FRUIT';'''
```


### Multiline queries

When working with SQL queries, it is often useful to be able to write multiline queries for readability and maintainability.

For example it is better to write:

<section class="flex-container">
<div class="flex-child" style="min-width: 300px;">
This:

```sql
SELECT
  price,
  best_by_date,
  sale_pct,
  quantity
FROM products
WHERE product_type = "FRUIT";
```
</div>
<div class="flex-child" style="min-width: 300px;">
Not this:

```sql
select price, best_by_date, sale_pct, quantity from products where product_type = "FRUIT";
```
</div>
</section>

To write multiline queries in Python, you will need to define a multi-line string. 
In Python this is done using triple quotes.

```python
query = """
SELECT
  price,
  best_by_date,
  sale_pct,
  quantity
FROM products
WHERE product_type = "FRUIT";"""

cur.execute(query)
```

### String concatenation

When writing SQL queries in Python, especially if you are writing queries that rely on user input, you may be tempted to assemble your SQL queries using string concatenation.

![](media/Season_18_Episode_13_GIF_by_The_Simpsons.gif)

Using string concatenation to build SQL queries is a terrible idea, as it leaves your code open to SQL injection attacks.
This concept will be explored in more detail in the [SQL Injection](https://liascript.github.io/course/?https://dscroft.github.io/liascript_sqli/lia.md) activity.

This is not a Python-specific or SQL-specific issues, it is a general issue with any programming language that allows you to create code to run on the host machine using string concatenation.

There are a *very* small number of cases where string concatenation could be acceptable, such as when you are writing a query that does not rely directly on user input. 
But for the most part string concatenation for SQL query creation or *any* code that will be executed on the host machine should be viewed as an actively dangerous anti-pattern and is to be avoided.

----------------------

You should use instead use parameterized queries, these allow you to safely pass user input to your SQL queries without the risk of SQL injection attacks.

`?` is used as a placeholder for the parameter in the query and will be replaced with the provided value when the query is executed.

**This:**

```python
query = "SELECT * FROM products WHERE product_type = ?;"
cur.execute(query, ("FRUIT",))
```

**Not this:**

```python
search_term = "FRUIT"

query = "SELECT * FROM products WHERE product_type = '" + search_term + "';"
cur.execute(query)

# or

query = f"SELECT * FROM products WHERE product_type = '{search_term}';"
cur.execute(query)
```

**Never, *ever*, under *any* circumstances, this:**

```python
# getting user input
search_term = input("Enter a search term: ")

# using user input directly in a query
query = "SELECT * FROM products WHERE product_type = '" + search_term + "';"
cur.execute(query)
```

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>
parameterized queries is one place where code may need to differ between databases.

The specific placeholder syntax is database-specific and not part of the Python Database API Specification.
You will need to check the documentation for the specific database you are using to see what placeholder syntax is supported.

For example, MySQL uses `%s` as a placeholder, while SQLite uses `?`.

However all databases should support the use of parameterized queries, so you should always use this approach when writing SQL queries in Python.
</div>


## Executing queries

We have already seen in the previous examples how to execute queries using the `execute()` method of the cursor object.

This method takes a SQL query as a string and executes it once against the database.
This should suffice for the majority of SELECT queries but there are some additional considerations to be aware of when executing multiple queries.
This is particularly relevant when running queries that modify the database, such as INSERT, UPDATE, or DELETE queries.

### Multiple queries

Although `execute()` should suffice for the majority of SELECT queries but there are some additional considerations to be aware of when executing multiple queries.
This is particularly relevant when running queries that modify the database, such as INSERT, UPDATE, or DELETE queries.

@create_users_db

**Inserting data using a loop**

```python
data = [('Badger999', 'hon3y'),
        ('Fox123', 'jump5')]

with closing(sqlite3.connect("users.db")) as con:
    cur = con.cursor()
    for record in data:
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?);", record)
        print( f"{cur.rowcount} rows inserted." )
```
@Pyodide.eval

-----------------------------

```python
data = [('Zebra111', 'stripe1'),
        ('Lion222', 'roar2')]

with closing(sqlite3.connect("users.db")) as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO users (username, password) VALUES (?, ?);", data)
    print( f"{cur.rowcount} rows inserted." )
```
@Pyodide.eval


## Performance

Regardless of the database that you are using, the performance of your code will depend on how you write your queries and how you choose to access the results.

In python there are three main ways to retrieve the results of a query:

<section class="flex-container">
<div class="flex-child" style="min-width: 300px;">

**fetchall**

Acquires the full set of results from the query in one go.
This is the most fastest way to retrieve the results from a query, but means that you are storing all of the data in memory at once.

It is entirely possible to run out of memory if working with a large dataset and so this approach should be used with caution.

</div>
<div class="flex-child" style="min-width: 300px;">
```python
cur.execute("SELECT * FROM table_name;")
rows = cur.fetchall()
for row in rows:
    print(row)
```
</div>
</section>

----------------------------

<section class="flex-container">
<div class="flex-child" style="min-width: 300px;">

**fetchmany**

Acquires a specified number of results from the query in one go.
This is a good compromise between performance and memory usage, as it allows you to retrieve multiple rows at once without using too much memory.

</div>
<div class="flex-child" style="min-width: 300px;">
```python
cur.execute("SELECT * FROM table_name;")
while rows:=cur.fetchmany(10):
    print( f"{len(rows)} rows fetched:")
    for row in rows:
        print(row)
```
</div>
</section>

----------------------------

<section class="flex-container">
<div class="flex-child" style="min-width: 300px;">

**fetchone**

Acquires a single row from the query at a time.
This is the slowest way to retrieve the results from a query, as it requires a round trip to the database for each row.
However, it is the most memory-efficient way to retrieve the results, as it only retrieves one row at a time.
It is also faster than the other methods in the sense that the time to acquire the first row is usually much less, even while the time to acquire all rows is longer.

This is also the method that is used by default when iterating over a cursor, i.e. `for row in cursor:`.

</div>
<div class="flex-child" style="min-width: 300px;">
```python
cur.execute("SELECT * FROM table_name;")
while row:=cur.fetchone():
    print(row)
```

```python
cur.execute("SELECT * FROM table_name;")
for row in cur:
    print(row)
```
</div>
</section>

The appropriate method to use will depend on the specific use case and the size of the dataset being queried.



# Demonstration

If we put all of this together, we can see the significant difference that it makes to our code.


**Not recommended**

```python
con = sqlite3.connect("store.db")

orders = [(1, 1), (2, 2), (3, 3)]

for user, product in orders:
    con.execute("UPDATE products SET quantity = quantity -1 WHERE id = "+str(product)+";")
    con.execute("INSERT INTO orders (user_id, product_id) VALUES ("+str(user)+", "+str(product)+");")
    con.execute("UPDATE users SET credit = credit - (SELECT price FROM products WHERE id = "+str(product)+") WHERE id = "+str(user)+";")

con.commit()
con.close()
```
----------------

**Better**

```python
orders = [(1, 2), (2, 3), (3, 1)]

try:
    with closing(sqlite3.connect("store.db")) as con, con:
        con.executemany("""UPDATE products 
                        SET quantity = quantity -1 
                        WHERE id = ?;""", 
                        ((product,) for _, product in orders))
        
        con.executemany("""INSERT INTO orders (user_id, product_id) 
                        VALUES (?, ?);""", 
                        orders)
        
        con.executemany("""UPDATE users 
                        SET credit = credit - (SELECT price 
                                                FROM products 
                                                WHERE id = ?) 
                        WHERE id = ?;""", 
                        ((product, user) for user, product in orders))
except sqlite3.Error as e:
    print(f"Error processing orders: {e}")

```


Why is the second example better? 

<details>
<summary>**If you are still stuck, click to see our answer!**</summary>

<br/>

<div class = "answer">
These are the improvements that we have made, are there any additional improvements that you would make?

1. No string concatenation

   - In the initial example we are using string concatenation to build the SQL queries, this is very poor practise. 
   - It also negatively impacts the readability of the SQL statement, although since it's all on one line it's not particularly readable to begin with.

2. Context management
   
   - We are also not using a context manager to handle the connection, we have remembered to call `commit()` and `close()` this time but they might be forgotten if every the code is changed or refactored.

3. Performance

   - Using a for loop to process each order is less clear cut, using `executemany()` in the second example is more efficient but in this case it has made it more difficult to pass the appropriate values to the SQL queries.
   - The for loop from the first example is probably more readable than the multiple generator expressions used in the second example but this could be a situation where the performance benefits outweigh the readability concerns, it would depend on the number of orders being processed.

</div>

</details>


## Quiz: Best Practices

Question 1
==========

Which of the following statements about `executemany()` in Python's `sqlite3` module is correct?

[( )] `executemany()` can only be used for SELECT queries.
[(X)] `executemany()` efficiently executes the same SQL statement multiple times with different parameters.
[( )] `executemany()` automatically commits changes after each execution.
[( )] `executemany()` is less efficient than running a loop with `execute()`.

****

<div class = "answer">

`executemany()` is used to efficiently execute the same SQL statement multiple times with different sets of parameters. This is especially useful for bulk inserts or updates, as it reduces the overhead compared to running a loop with individual `execute()` calls.

</div>
****



Question 2
==========

Which of the following is the best practice for managing SQLite database connections in Python?

[( )] Always use `connect()` and manually call `close()` at the end of your script.
[(X)] Use a context manager with `with` statement to automatically handle connection cleanup.
[( )] Keep the connection open for the entire duration of your program.
[( )] Use `connect()` and rely on Python's garbage collector to close the connection.
****

<div class = "answer">

Using a context manager with the `with` statement is the best practice for managing SQLite database connections. This ensures that the connection is properly closed even if an exception occurs, preventing resource leaks and potential database corruption. The context manager automatically handles both committing transactions and closing the connection when exiting the `with` block.

</div>
****



Question 3
==========

Consider the following code snippet that inserts user data into a SQLite database:

```python
user_id = 123
username = "alice"
email = "alice@example.com"

# Which approach is correct?
```

Which of the following is the correct and secure way to insert this data?

[( )] `cursor.execute(f"INSERT INTO users VALUES ({user_id}, '{username}', '{email}')")`
[( )] `cursor.execute("INSERT INTO users VALUES (" + str(user_id) + ", '" + username + "', '" + email + "')")`
[(X)] `cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (user_id, username, email))`
[( )] `cursor.execute("INSERT INTO users VALUES (%s, %s, %s)", (user_id, username, email))`
****

<div class = "answer">

The correct approach is using parameterized queries with `?` placeholders: `cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (user_id, username, email))`. This method prevents SQL injection attacks by properly escaping the parameters and is the standard way to use placeholders in SQLite with Python's `sqlite3` module. The other options use string formatting or concatenation which are vulnerable to SQL injection, or use `%s` placeholders which are used in other database libraries like `psycopg2` but not in SQLite's `sqlite3` module.

</div>
****

## Recap

@recap
