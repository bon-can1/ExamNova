from flask import Flask, render_template, request, jsonify
import json
import os
import google.generativeai as genai

app = Flask(__name__)

# API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "AIzaSyAPjNtcRqDCH4OtwbYZA_YgDb-kJCB19kw"))

#  Use supported model
model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json() or {}
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({"error": "Please enter a topic."}), 400

    prompt = f"""
You are an exam content generator.
Generate study content for this topic: "{topic}".

Return ONLY valid JSON with this exact shape:
{{
  "topic": "string",
  "explanation": "2-3 paragraph explanation",
  "mcqs": [
    {{
      "question": "string",
      "options": ["A option", "B option", "C option", "D option"],
      "correct_index": 0,
      "answer_explanation": "why this option is correct"
    }}
  ],
  "theory": [
    {{
      "question": "string",
      "answer": "detailed answer in 5-8 lines"
    }}
  ]
}}

Rules:
- Create exactly 7 MCQs and exactly 4 theory questions.
- MCQ options must be distinct.
- correct_index must be 0, 1, 2, or 3.
- Keep quality suitable for university exam prep.
    """

    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip()
        start = raw_text.find("{")
        end = raw_text.rfind("}")

        if start == -1 or end == -1:
            return jsonify({"error": "Model returned an invalid response format."}), 500

        payload = json.loads(raw_text[start : end + 1])
        return jsonify(payload)

    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)