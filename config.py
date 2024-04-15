import os 
from dotenv import load_dotenv 
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

GEMINIPRO_API_KEY = os.getenv("GEMINIPRO_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

DATASET_PATH = Path("data") / "codes.txt"

REPO = [
    "prathimacode-hub/Awesome_Python_Scripts",
    "adnanh/webhook",
    "chaoss/grimoirelab-perceval",
    "Logan1x/Python-Scripts",
    "larymak/Python-project-Scripts",
] 

prompt = """
**User Input:** {user_prompt} 

**Task:**  Extract the necessary steps involved in the task that the user describes. 
Break down user input into actionable python tasks suitable for automation. 
List these steps in a sequential manner. Maintain the output format and dont output anything except the steps.

**Output Format:**

* STEP1: Use python to - [Action in present tense verb form] 
* STEP2: Use python to - [Action in present tense verb form]
* ... 

Response :
"""

rag_prompt = """
Role: You are a proficient Retrieval Augmented Generation Artificial Intelligence Engineer, specializing in Generating Automation codes.
Task: Generate syntactically correct codes for the automation task below.
Instructions: 
1. Use the context to understand the task and how to perform it in python.
2. Make sure to write complete python scripts and not just outlines.

Task:
{question}

Context:
{context}

Code Response:
"""

prompt_llm = """
    Role: You are a proficient python developer, specializing in Automation Tasks.
    Task: Respond with the syntactically correct code for to the automation task below. Make sure you follow rules below:
    Rules:
    1. Understand the task and how to perform it in python.
    2. Do not add license information to the output code.
    3. Ensure all the requirements in the question are met.
    4. Make sure to write complete scripts not just outlines.

    Task:
    {user_prompt}

    Helpful Response :
    """