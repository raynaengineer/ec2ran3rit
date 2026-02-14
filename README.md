<p align="center">
  <img src="./banner.png" alt="Project Banner" width="100%">
</p>

# Horegallu 🧠

## Basic Details

### Team Name:
Torus

### Team Members
- Member 1: Anukrishna P Anil - RIT,Kottyama
- Member 2: Rayna Nadarsha - RIT,Kottayam

### Hosted Project Link
Currently runs locally using Flask development server  
(Localhost: http://127.0.0.1:5000)

### Project Description
Horegallu is a web-based AI mental health support chatbot.  
It provides calm, therapist-style responses and detects crisis-related language to offer immediate emergency resources.

### The Problem Statement
Many individuals experience emotional distress but hesitate to seek immediate professional help. There is a need for a safe, private, and non-judgmental digital space where users can express thoughts and receive grounded emotional support.

### The Solution
Horegallu integrates a locally hosted LLM (gemma3 via Ollama) with structured therapist prompts and crisis keyword detection. It generates concise, supportive responses and automatically displays Indian mental health helpline numbers when high-risk language is detected.

---

## Technical Details

### Technologies/Components Used

**For Software:**

- Languages used: Python, HTML, CSS, JavaScript
- Frameworks used: Flask
- Libraries used: requests
- Tools used: VS Code, Git, Ollama (Local LLM Runtime)

**For Hardware:**
Not applicable.

---

## Features

- Therapist-style AI responses (1–3 concise sentences)
- Crisis keyword detection (self-harm related phrases)
- India-specific mental health helplines integration
- Short-term conversation memory (last 6 exchanges)
- Clear conversation functionality
- REST API backend endpoints
- Local LLM integration using gemma3 model
- Typing indicator UI for better user experience

---

## Implementation

### For Software:

#### Installation
Install Ollama (if not installed) from:
https://ollama.com

Pull required model:

ollama pull gemma3

Run

Start Ollama model:

ollama run gemma3


In another terminal, run Flask app:

python app.py


Open in browser:

http://127.0.0.1:5000


git clone <https://github.com/raynaengineer/ec2ran3rit>
cd horegallu
## Project Documentation

normal

<img src="./screen1.png" alt="Project screenshot" width="100%">


Someone scolded me.

<img src="./screen2.png" alt="Project screenshot" width="100%">


I am going to commit suicide.

<img src="./screen3.png" alt="Project screenshot" width="100%">


##System Architecture Diagram
<img width="953" height="593" alt="Untitled Diagram drawio" src="https://github.com/user-attachments/assets/916429a0-8396-445f-a2e7-06bbccb207b0" />
## Workflow Diagram
<img src="./workflow.png" alt="Project screenshot" width="100%">
#### Diagrams
System Architecture:
- Frontend communicates with Flask backend.
- Backend processes input via ai.py.
- Crisis detection runs before model call.
- Ollama local API generates response.
- Final response returned to UI.
##API Documentation Section
POST /chat
Body:
{
  "message": "I feel anxious"
}

Response:
{
  "response": "You're feeling anxious right now..."
}
##Project Demo
https://drive.google.com/file/d/1PK4L00XvJL4QHNu5sytNsueBkkXWvRIB/view?usp=sharing




python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

pip install flask requests
