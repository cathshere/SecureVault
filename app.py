from flask import Flask, render_template, request, send_file
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ENCRYPTED_FOLDER = "encrypted_files"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load Key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Create folders if not present
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        file = request.files["file"]

        if file.filename == "":
            return "No file selected"

        filepath = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        file.save(filepath)

        # Read file
        with open(filepath, "rb") as f:
            data = f.read()

        # Encrypt
        encrypted = fernet.encrypt(data)

        encrypted_path = os.path.join(
            ENCRYPTED_FOLDER,
            file.filename + ".enc"
        )

        # Save encrypted file
        with open(encrypted_path, "wb") as f:
            f.write(encrypted)

    # ALWAYS load files here
    files = os.listdir(ENCRYPTED_FOLDER)

    return render_template(
        "upload.html",
        files=files
    )


@app.route("/download/<filename>")
def download(filename):

    encrypted_path = os.path.join(
        ENCRYPTED_FOLDER,
        filename
    )

    with open(encrypted_path, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    original_name = filename.replace(".enc", "")

    temp_file = os.path.join(
        UPLOAD_FOLDER,
        "temp_" + original_name
    )

    with open(temp_file, "wb") as f:
        f.write(decrypted_data)

    return send_file(
        temp_file,
        as_attachment=True,
        download_name=original_name
    )


if __name__ == "__main__":
    app.run(debug=True)