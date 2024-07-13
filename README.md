# Medical Chatbot using Llama2

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-Llama2-green.svg)](https://platform.openai.com/docs/models/llama2)

A user-friendly medical chatbot powered by Llama2, designed to provide preliminary information on health concerns and promote informed decision-making.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This chatbot aims to assist users by answering basic medical queries, providing potential diagnoses, and suggesting when professional medical attention might be needed. It leverages the power of the Llama2 language model, offering natural language understanding and informative responses.

**Disclaimer:** This chatbot is intended for informational purposes only and should not be used as a substitute for professional medical advice or diagnosis. Always consult a qualified healthcare professional for any health concerns.

## Features

- **Natural Language Understanding:**  Understands user questions and concerns in plain language.
- **Medical Information Retrieval:** Accesses relevant medical information from trusted sources.
- **Preliminary Symptom Assessment:**  Helps identify potential causes and next steps.
- **User-Friendly Interface:**  Provides a simple and intuitive chat interface.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone "https://github.com/prabhakarsharma-pythonaire/Medical-chatbot-using-Llama2"
   cd Medical-chatbot-using-Llama2

2. **Install Dependencies:**
   python -m venv venv  # Create a virtual environment
   source venv/bin/activate # or venv/Scripts/activate for windows
   pip install -r requirements.txt 

3. **Set Up Pinecone API Key:**
   Pinecone_API_KEY=your_Pinecone_api_key

4. **Run The App**
   python app.py

5. **Open in Browser**:
   http://localhost:7860/