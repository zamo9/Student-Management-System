import sqlite3
DB_FILE = 'students.db'


#initialize the database
def initialize_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    

    #Add a new student to the database
def add_student_to_db(student_id, name, age):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if student_id is None:  # If no ID is provided, let SQLite auto-generate it
        cursor.execute('''
            INSERT INTO students (name, age) VALUES (?, ?)
        ''', (name, age))
    else:
        cursor.execute('''
            INSERT INTO students (id, name, age) VALUES (?, ?, ?)
        ''', (student_id, name, age))
    conn.commit()
    conn.close()

    #retrieve all students from the database
def get_all_students():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return students


# Update a student's information in the database
def update_student_in_db(student_id, name, age):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students SET name = ?, age = ? WHERE id = ?
    ''', (name, age, student_id))
    conn.commit()
    conn.close()


# Delete a student from the database
def delete_student_from_db(student_id):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    connection.commit()
    connection.close()
