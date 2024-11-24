from flask import Flask, render_template, request

app = Flask(__name__)

# Define the route for the home page with support for GET and POST
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Extract form data using request.form
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        availability_date = request.form.get("availability-date")
        status = request.form.get("status")

        # Print the data to the console for debugging (or use it as needed)
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Availability Date: {availability_date}")
        print(f"Status: {status}")

        return f"Form submitted! Hello {first_name} {last_name}!"

    # Render the form for GET requests
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
