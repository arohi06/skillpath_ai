import os
import requests
import json

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = "models/gemini-2.5-flash"


def generate_roadmap(profile_data):
    if not GOOGLE_API_KEY:
        return {"error": "Google API key not set"}

    url = f"https://generativelanguage.googleapis.com/v1beta/{MODEL}:generateContent?key={GOOGLE_API_KEY}"

    
    prompt = f"""
You are an expert career mentor.

User Profile:
- Degree: {profile_data['degree']}
- Skills: {profile_data['skills']}
- End Goal: {profile_data['end_goal']}
- Time Available: {profile_data['time_available']}

Create ONLY 3 levels (level_1, level_2, level_3).

Return STRICT JSON in this exact format:

{{
  "level_1": {{
    "title": "",
    "goal": "",
    "skills": [],
    "tasks": [],
    "resources": [],
    "project": "",
    "outcome": ""
  }},
  "level_2": {{
    "title": "",
    "goal": "",
    "skills": [],
    "tasks": [],
    "resources": [],
    "project": "",
    "outcome": ""
  }},
  "level_3": {{
    "title": "",
    "goal": "",
    "skills": [],
    "tasks": [],
    "resources": [],
    "project": "",
    "outcome": ""
  }}
}}

DO NOT add explanation or markdown.
ONLY valid JSON.
"""

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()

        data = response.json()
        text = data["candidates"][0]["content"]["parts"][0]["text"]

        
        return json.loads(text)

    except json.JSONDecodeError:
        return {"error": "Gemini returned invalid JSON", "raw": text}

    except Exception as e:
        return {"error": str(e)}
