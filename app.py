import os
import json
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")
MODEL_NAME = "gemini-2.5-flash"

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing. Please set it in your .env file.")

client = genai.Client(api_key=GEMINI_API_KEY)


def read_transcript(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def build_prompt(transcript: str) -> str:
    return f"""
You are an AI meeting assistant.

Your task:
1. Read the meeting transcript.
2. Generate a concise meeting summary in 2-4 sentences.
3. Extract action items with:
   - owner
   - task
   - deadline (if mentioned, otherwise null)
   - priority (High, Medium, Low)
4. Suggest next steps.
5. Return the result in valid JSON only.
6. Do not include markdown formatting.
7. Do not invent information that is not explicitly supported by the transcript.

Expected JSON format:
{{
  "summary": "short summary here",
  "action_items": [
    {{
      "owner": "person name",
      "task": "task description",
      "deadline": "deadline if available, otherwise null",
      "priority": "High"
    }}
  ],
  "next_steps": [
    "step 1",
    "step 2"
  ]
}}

Transcript:
{transcript}
""".strip()


def clean_json_response(text: str) -> str:
    text = text.strip()
    text = text.replace("```json", "").replace("```", "").strip()
    return text


def extract_meeting_data(transcript: str) -> dict:
    prompt = build_prompt(transcript)
    print(f"[INFO] Using model: {MODEL_NAME}")

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    content = response.text.strip() if response.text else ""
    if not content:
        raise ValueError("Model returned an empty response.")

    cleaned = clean_json_response(content)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as error:
        print("Raw model response:")
        print(content)
        raise ValueError(f"Failed to parse JSON response: {error}") from error


def save_output(data: dict, output_path: str = "output_tasks.json") -> None:
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def send_to_n8n(data: dict) -> None:
    if not N8N_WEBHOOK_URL:
        print("[INFO] No N8N_WEBHOOK_URL found. Skipping webhook step.")
        return

    try:
        response = requests.post(N8N_WEBHOOK_URL, json=data, timeout=20)
        print(f"[INFO] n8n webhook status: {response.status_code}")
        print("[INFO] n8n response:", response.text)
    except requests.RequestException as error:
        print(f"[WARNING] Failed to send data to n8n webhook: {error}")


def main():
    transcript = read_transcript("sample_transcript.txt")
    result = extract_meeting_data(transcript)
    save_output(result)
    send_to_n8n(result)

    print("\n[INFO] Done. Output saved to output_tasks.json\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()