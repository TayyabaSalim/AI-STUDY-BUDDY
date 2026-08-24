import os

from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

from werkzeug.utils import secure_filename

from rag_engine import (
    process_notes,
    generate_summary,
    generate_flashcards
)


# ============================================================
# FLASK CONFIGURATION
# ============================================================

app = Flask(__name__)

UPLOAD_FOLDER = "./uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ============================================================
# ALLOWED FILES
# ============================================================

ALLOWED_EXTENSIONS = {
    "txt",
    "pdf",
    "pptx"
}


def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(
            ".",
            1
        )[1].lower()
        in ALLOWED_EXTENSIONS
    )


# ============================================================
# HOME
# ============================================================

@app.route("/")
def index():

    return render_template(
        "index.html"
    )


# ============================================================
# UPLOAD
# ============================================================

@app.route(
    "/upload",
    methods=["POST"]
)
def upload_file():

    try:

        if "file" not in request.files:

            return jsonify({
                "error": "No file was uploaded."
            }), 400

        file = request.files["file"]

        if file.filename == "":

            return jsonify({
                "error": "Please select a file."
            }), 400

        if not allowed_file(file.filename):

            return jsonify({
                "error": (
                    "Unsupported file type. "
                    "Use TXT, PDF, or PPTX."
                )
            }), 400

        filename = secure_filename(
            file.filename
        )

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(file_path)

        print(
            f"\nProcessing: {filename}"
        )

        status = process_notes(
            file_path
        )

        return jsonify({
            "message": status
        }), 200

    except Exception as error:

        print("\n===== UPLOAD ERROR =====")
        print(error)
        print("========================\n")

        return jsonify({
            "error": str(error)
        }), 500


# ============================================================
# SUMMARY
# ============================================================

@app.route(
    "/summarize",
    methods=["GET"]
)
def get_summary():

    try:

        summary = generate_summary()

        return jsonify({
            "summary": summary
        }), 200

    except Exception as error:

        print("\n===== SUMMARY ROUTE ERROR =====")
        print(error)
        print("===============================\n")

        return jsonify({
            "error": str(error)
        }), 500


# ============================================================
# FLASHCARDS
# ============================================================

@app.route(
    "/flashcards",
    methods=["GET"]
)
def get_flashcards():

    try:

        flashcards = generate_flashcards()

        return jsonify({
            "flashcards": flashcards
        }), 200

    except Exception as error:

        print("\n===== FLASHCARD ROUTE ERROR =====")
        print(error)
        print("=================================\n")

        return jsonify({
            "error": str(error)
        }), 500


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    print("\n========================================")
    print("          AI STUDY BUDDY")
    print("========================================")
    print("LLM:        llama3.2")
    print("Embeddings: nomic-embed-text")
    print("Database:   ChromaDB")
    print("Files:      TXT / PDF / PPTX")
    print("Server:     http://127.0.0.1:5000")
    print("========================================\n")

    app.run(
        debug=True,
        port=5000
    )