from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(
    __name__,
    static_folder="../static",      # Static files are in the parent directory
    template_folder="templates"     # Templates are inside /backend/templates
)

# Secret key for flashing messages
app.secret_key = "your_secret_key"  

# In-memory list to store students (for testing purposes)
students = []

# Home route
@app.route("/")
def index():
    return render_template("home.html")

# View students route
@app.route("/students")
def view_students():
    return render_template("index.html", students=students)

# Add student route
@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        # Retrieve form data
        student_id = request.form.get("id")
        name = request.form.get("name")
        age = request.form.get("age")

        # Add the student to the in-memory list
        students.append({"id": student_id, "name": name, "age": age})

        # Flash a success message
        flash("Student added successfully!")

        # Redirect to the students page after adding
        return redirect(url_for("view_students"))

    # Render the add_student.html template for GET requests
    return render_template("add_student.html")

# Edit student route
@app.route("/edit_student/<student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    # Find the student to edit
    student = next((student for student in students if student["id"] == student_id), None)

    if not student:
        flash("Student not found!")
        return redirect(url_for("view_students"))

    if request.method == "POST":
        # Update the student's details
        student["name"] = request.form.get("name")
        student["age"] = request.form.get("age")

        # Flash a success message
        flash("Student updated successfully!")

        # Redirect to the students page
        return redirect(url_for("view_students"))

    # Render the edit_student.html template for GET requests
    return render_template("edit_student.html", student=student)

# Delete student route
@app.route("/delete_student/<student_id>", methods=["POST"])
def delete_student(student_id):
    global students
    # Remove the student with the given ID
    students = [student for student in students if student["id"] != student_id]

    # Flash a success message
    flash("Student deleted successfully!")

    # Redirect to the students page
    return redirect(url_for("view_students"))

if __name__ == "__main__":
    app.run(debug=True)