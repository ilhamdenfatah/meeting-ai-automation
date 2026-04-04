# 🤖 AI Meeting Agent

**Automating meeting summarization and action-item extraction using Gemini AI and n8n workflow automation.**

This project demonstrates a simple automation pipeline that converts raw meeting transcripts into structured insights.

The system extracts:
- a concise meeting summary
- action items with owners
- next steps

The extracted data is then sent to an n8n webhook, allowing it to trigger automation workflows.

The goal of this project is to showcase how AI reasoning can be integrated with workflow automation to turn unstructured conversation into actionable information.

---
## 🚀 Demo

### AI Extraction Pipeline

The Python script reads a meeting transcript and sends it to Gemini AI.

Gemini analyzes the conversation and returns structured data containing:

a summary of the meeting

action items with responsible owners

suggested next steps

The extracted data is also sent to an n8n webhook, demonstrating how AI output can trigger downstream automation.

### Structured Output

Example structured output produced by the system:

```
{
  "summary": "The team discussed finalizing the landing page update by Friday...",
  "action_items": [
    {
      "owner": "Anna",
      "task": "Prepare the revised copy",
      "deadline": "tomorrow afternoon",
      "priority": "High"
    }
  ],
  "next_steps": [
    "Align again next Monday to ensure updates are ready before launch."
  ]
}
```

Instead of generating plain text notes, the system produces structured JSON, making the data easier to use in automation pipelines or other systems.

### Automation Workflow

The extracted data is sent to an n8n workflow through a webhook.

The workflow:
1. Receives the structured meeting data
2. Processes the payload
3. Returns a confirmation response

This demonstrates how AI-generated insights can be connected to automation tools and integrations.

---

## 🧠 System Architecture

```
Meeting Transcript
        ↓
Python Script (app.py)
        ↓
Gemini AI
        ↓
Structured JSON Output
        ↓
n8n Webhook
        ↓
Automation Workflow
        ↓
Response returned to Python

This pipeline shows a simple pattern for integrating LLM-generated insights with automation systems.
```

---

## 💡 🛠 Tech Stack

Language:
- Python

AI
- Google Gemini API

Automation
- n8n

Integration
- Webhooks
- JSON processing

Environment
- python-dotenv

---

## 📂 Project Structure

```
ai-meeting-agent
│
├── app.py
├── sample_transcript.txt
├── example_output.json
├── requirements.txt
│
├── images
│   ├── ai_pipeline_terminal.png
│   ├── json_output.png
│   └── n8n_workflow.png
│
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Setup

### 1. Clone Repository

> git clone https://github.com/yourusername/ai-meeting-agent.git
> cd ai-meeting-agent

### 2. Install dependencies

> pip install -r requirements.txt

### 3. Configure environment variables

Create a .env file based on .env.example.

Example:

> GEMINI_API_KEY=put_api_key_here
> N8N_WEBHOOK_URL=http://localhost:5678/webhook/meeting-agent

### 4. Run the script

> python app.py

The script will:
1. Read the meeting transcript
2. Send the transcript to Gemini AI
3. Extract structured insights
4. Send the result to the n8n webhook
5. Save the structured output as JSON

---

## 📄 Example Input

sample_transcript.txt

```
James: We need to finalize the landing page update by Friday.
Anna: I can prepare the revised copy by tomorrow afternoon.
Andrew: I will review the analytics and identify which section has the highest drop-off.
James: Great. Let's align again next Monday and make sure the updates are ready before launch.
Derek: I will coordinate with design once Anna finishes the copy.
```

---

## 📌 Potential Use Cases

This project illustrates how AI can assist with tasks such as:
- meeting summarization
- automatic task extraction
- workflow automation triggers
- AI-assisted productivity tools

Possible integrations include:
- Slack notifications
- project management tools
- task tracking systems
- automated reporting workflows

---

## 👤 Author

Ilham Den Fatah

AI Automation Builder & Decision Systems Engineer

---

## 💡 Project Motivation

Meetings often produce valuable decisions and tasks, but the information usually remains buried in unstructured conversation.

This project explores a simple approach to converting that conversation into structured, actionable data that can feed automation workflows.

---

## 🧩 What This Project Demonstrates

This project was designed not only as a technical exercise, but also as a demonstration of how AI capabilities can be integrated into practical workflows.

Specifically, it highlights several important engineering concepts.

### 1. LLM Integration in Application Logic

The system integrates a Large Language Model (Gemini) into a Python application to transform unstructured conversation into structured data.

Rather than producing plain text summaries, the model is prompted to generate structured JSON that can be used programmatically.

### 2. Turning AI Output into Automation Triggers

Instead of stopping at AI-generated results, the system forwards structured insights to an automation workflow using webhooks.

This demonstrates how AI outputs can become **inputs for operational workflows**, bridging AI reasoning with automation systems.

### 3. Designing AI Systems Around Structured Data

The project emphasizes structured outputs:

- summaries
- action items
- next steps

By enforcing structure, the results become easier to integrate with downstream systems such as task managers, dashboards, or notification services.

### 4. Lightweight AI + Automation Architecture

The architecture intentionally keeps the system simple:

- Python handles AI inference
- Gemini performs reasoning
- n8n handles workflow automation

This pattern shows how AI functionality can be added to existing automation ecosystems without complex infrastructure.

### 5. Practical AI for Productivity Use Cases

Rather than focusing on model training, this project demonstrates **applied AI engineering** — building tools that help convert everyday business conversations into actionable information.

This approach reflects how many real-world AI systems are built: by combining existing models with automation workflows and structured data pipelines.

---

## 🔮 Future Improvements

There are several directions in which this project could be extended to move closer to a real-world meeting assistant system.

### 1. Speech-to-Text Integration

Currently the system processes text transcripts.
A natural extension would be integrating a speech recognition layer (for example using Whisper or similar models) to process recorded meetings directly.

Pipeline example:

```
Meeting Recording
        ↓
Speech-to-Text
        ↓
Transcript Processing (Gemini)
        ↓
Structured Tasks & Summary
```

### 2. Calendar Integration

The agent could be connected to calendar platforms such as:
- Google Calendar
- Outlook Calendar

This would allow the system to automatically:
- fetch meeting recordings or transcripts
- process them after the meeting ends
- generate structured summaries automatically.

### 3. Task Management Integration

Instead of returning action items only as JSON, the system could automatically create tasks in tools such as:
- Notion
- Jira
- Trello
- Asana

Example workflow:

```
AI extracts action items
        ↓
n8n workflow triggers
        ↓
Tasks automatically created in project management system
```

### 4. Slack/Email Notifications

Another extension would be pushing meeting summaries directly to team communication channels.

Examples:
- send meeting summary to Slack
- email action items to meeting participants
- notify owners when tasks are assigned.

### 5. Multi-Meeting Insights

Over time, multiple meetings could be aggregated to generate insights such as:
- recurring topics
- repeated blockers
- delayed tasks
- team workload distribution.

This would turn the system from a meeting summarizer into a meeting intelligence tool.

### 6. Web Interface or Dashboard

Currently the system runs from the terminal.
A simple interface could be added using tools like:
- Streamlit
- FastAPI + frontend
- internal dashboard

This would allow users to:
- upload transcripts
- review summaries
- track action items across meetings.

---

## 💡 Design Goal

The long-term direction of this project is to explore how AI-generated insights can be integrated into automation pipelines, allowing unstructured conversations to be transformed into structured operational data.
