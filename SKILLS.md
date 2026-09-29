# AI Engineer Journey

## Goal

Become an AI Engineer, with a focus on LLM applications, Azure OpenAI, RAG, and agentic AI.

## Current Topic

OpenAI Python SDK

## Background

- Software Engineer with Android SDK development experience
- Familiar with REST APIs, HTTP methods, status codes, headers, authentication, serialization, and deserialization
- Comfortable with client\-server architecture
- Learning Python and AI concepts for an AI Engineer role
- Prefer concept\-focused explanations rather than beginner\-level REST API explanations

## Completed

### Setup

- Python 3.14.2 installed
- VS Code installed
- AI\-Lab workspace created
- Virtual environment created and activated
- Pandas installed
- Requests installed and upgraded
- Understood package installation using pip
- Understood virtual environments

### Python Basics

- Variables
- Strings
- Integers
- Floats
- print()
- f\-strings
- String methods such as upper() and lower()
- len()
- User input using input()
- Type conversion using int() and float()
- Lists
- List indexing
- append()
- remove()
- sort()
- reverse()
- for loops
- range(start, stop, step)
- Forward and reverse ranges
- Nested loops
- while loops
- Infinite loops
- break
- Functions using def
- Function parameters
- Function calls
- Return values
- Indentation and code blocks
- Basic recursion
- RecursionError

### Dictionaries

- Creating dictionaries
- Dictionary keys and values
- Accessing values using keys
- Adding dictionary values
- Updating dictionary values
- Removing dictionary values
- Looping through dictionaries
- Using items()
- Understanding nested dictionaries

### Conditions

- if
- elif
- else
- Comparison operators
- Logical operators using and and or
- Combining conditions with dictionaries and user input
- Understanding that Python uses elif rather than elseif

### Error Handling

- try
- except
- ValueError
- Preventing programs from crashing on invalid input
- Combining error handling with conditions
- Handling invalid numeric input

### Files

- Opening files
- Reading files
- Writing files
- Appending to files
- File modes: r, w, and a
- Using with open()
- Automatic file closing
- Current working directory
- Relative paths
- Absolute paths
- Custom file locations
- Understanding local file storage

### Modules

- Importing modules
- Using import
- Using the math module
- math.sqrt()
- math.pi
- math.e
- Mathematical utility functions
- Creating custom modules
- Calling functions from custom modules
- Understanding module namespaces

### Object\-Oriented Programming

- Classes
- Objects
- Instances
- Class as a blueprint
- Creating multiple objects from one class
- **init**()
- Understanding that **init** is a special method, not a Python keyword
- Understanding that **init** runs automatically during object initialization
- self
- Understanding self as the current object
- Instance variables
- Methods
- Calling methods on objects
- Storing different data in different objects
- Combining methods with conditions
- Difference between special methods and custom methods
- Basic understanding of dunder methods

### JSON

- Understanding JSON as a text\-based data format
- Difference between JSON and Python dictionaries
- Difference between JSON and Python lists
- Difference between JSON text and Python objects
- Recognizing a Python list of dictionaries
- Understanding that JSON text must be represented as a string in Python
- Importing the json module
- json.dumps()
- Converting Python objects into JSON strings
- json.loads()
- Converting JSON text into Python objects
- JSON object to Python dictionary conversion
- JSON array to Python list conversion
- JSON true and false to Python True and False
- JSON null to Python None
- Accessing values after JSON conversion
- Basic nested dictionary and list navigation

### Pandas and DataFrames

- Understanding Pandas
- Importing Pandas using import pandas as pd
- Understanding a DataFrame as a two\-dimensional table
- Understanding rows
- Understanding columns
- Understanding indexes
- Understanding cells
- Difference between a Series and a DataFrame
- Creating a DataFrame from a dictionary
- Creating a DataFrame from a list of dictionaries
- Selecting a column
- Accessing an individual value
- Filtering rows
- head()
- shape
- mean()
- min()
- max()
- count()
- Reading CSV files using read\_csv()
- Saving CSV files using to\_csv()
- Understanding index=False
- Converting API\-style Python data into a DataFrame
- Understanding why DataFrames simplify filtering and analysis
- Understanding why DataFrames can reduce manual looping
- Basic DataFrame interview questions
- Explaining DataFrames conceptually in an interview

### REST APIs

- Understanding client\-server architecture
- Understanding REST APIs
- HTTP GET requests
- HTTP POST requests conceptually
- Request and response flow
- HTTP status codes
- Headers
- Query parameters
- JSON request bodies
- Authentication headers conceptually
- Serialization and deserialization
- Difference between REST APIs and LLM APIs

### Python Requests

- Installing the requests library
- Importing requests
- Sending GET requests using requests.get()
- Understanding the Response object
- Accessing response.status\_code
- Accessing response.text
- Using response.json()
- Understanding that response.text returns a string
- Understanding that response.json() converts JSON into Python objects
- Accessing API response values using dictionary keys
- Calling the GitHub API
- Receiving HTTP 200 responses
- Reading GitHub API endpoint information
- Understanding requests.get() from an Android networking perspective
- Understanding requests as conceptually similar to Retrofit and OkHttp

### REST API vs LLM API

- REST APIs usually return stored or calculated application data
- LLM APIs generate content using a language model
- Both use standard HTTP request and response concepts
- Both commonly exchange JSON data
- LLM responses may vary between calls
- LLM APIs accept prompts or messages as input
- LLM APIs return generated text or structured output
- Understanding token\-based pricing
- Understanding context\-window limitations

### LLM Fundamentals

- What is a Large Language Model (LLM)
- Prompts and generated responses
- Prompt Engineering
- Role prompting
- Context prompting
- Constraints and output formatting
- Zero\-shot prompting
- One\-shot prompting
- Few\-shot prompting
- Chain\-of\-Thought prompting
- Tokens
- Input tokens
- Output tokens
- Token\-based billing
- Context windows
- Understanding that input \+ output tokens must fit in the context window
- Temperature
- Top\-P
- Deterministic vs probabilistic outputs
- Understanding why low temperature is used for structured outputs
- Understanding why high temperature increases creativity
- Hallucinations
- Structured outputs
- System messages
- User messages
- Assistant messages
- Basic understanding of embeddings
- Understanding semantic similarity
- Basic understanding of vector search
- Basic understanding of RAG (Retrieval\-Augmented Generation)
- Understanding Retrieval → Augmentation → Generation flow
- Understanding how embeddings enable semantic search
- Understanding that RAG reduces hallucinations
- Basic understanding of AI Agents
- Understanding LLM \+ Tools \+ Reasoning workflow

## Completed Files

- python\-basics/01\_variables.py
- python\-basics/02\_strings.py
- python\-basics/03\_input.py
- python\-basics/04\_lists.py
- python\-basics/05\_loops.py
- python\-basics/06\_functions.py
- python\-basics/07\_dictionaries.py
- python\-basics/08\_conditions.py
- python\-basics/09\_while\_loops.py
- python\-basics/10\_error\_handling.py
- python\-basics/11\_files.py
- python\-basics/12\_modules.py
- python\-basics/13\_atm\_project.py
- python\-basics/14\_classes\_and\_objects.py
- python\-basics/15\_json.py
- python\-basics/16\_pandas.py
- python\-basics/17\_apis.py
- ai\-basics/18\_llm\_fundamentals.py

## Current File

ai\-basics/21\_openai\_sdk.py

## Current Lesson

OpenAI Python SDK

## Current Learning Goals

- Learn OpenAI Python SDK
- Understand chat completion APIs
- Understand messages and conversations
- Understand structured outputs
- Deepen understanding of embeddings
- Understand vector databases
- Understand vector search
- Implement RAG in Python
- Understand tool calling
- Understand AI agents in practice
- Learn Azure OpenAI fundamentals
- Build an end\-to\-end AI application

## Next Topics

1. OpenAI Python SDK
2. Azure OpenAI
3. Structured Outputs
4. Embeddings Deep Dive
5. Vector Search
6. Vector Databases
7. RAG Fundamentals
8. RAG Implementation
9. AI Agents in Practice
10. Tool Calling
11. Semantic Kernel
12. Evaluation and Responsible AI
13. End\-to\-End AI Project

## Planned Files

- ai\-basics/21\_openai\_sdk.py
- ai\-basics/22\_azure\_openai.py
- ai\-basics/23\_structured\_outputs.py
- ai\-basics/24\_embeddings.py
- ai\-basics/25\_vector\_search.py
- ai\-basics/26\_rag\_basics.py
- ai\-basics/27\_agents\_and\_tools.py
- ai\-basics/28\_semantic\_kernel.py
- ai\-projects/01\_ai\_assistant.py

## Learning Approach

- Use existing Android and software engineering experience when explaining APIs and architecture
- Avoid repeating basic HTTP and REST concepts unless needed
- Focus on concepts that are new for AI Engineering
- Connect Python concepts to real AI applications
- Prefer small practical examples over long theoretical explanations
- Build understanding before introducing frameworks
- Learn one major topic at a time
- Add a short exercise after each explanation
- Review an exercise before moving to the next topic
- Prefer Azure OpenAI and Microsoft AI technologies where appropriate
- Avoid unnecessary tools, tracking systems, and complex project structures

## Instructions for Copilot

1. Read this file before continuing my AI Engineer lessons.
2. Use the completed topics and files to understand my existing knowledge.
3. Do not restart completed Python fundamentals unless I request a revision.
4. Remember that I already understand Android networking, REST APIs, HTTP, and serialization.
5. Explain new AI concepts in simple language while respecting my software engineering background.
6. Teach only one major topic at a time.
7. Give me a short practical exercise after each explanation.
8. Connect concepts to realistic AI Engineer use cases.
9. Avoid unnecessary tools or overcomplicated project structures.
10. When I complete a lesson, provide a complete replacement version of this file.
11. Always state the exact filename and topic to continue with next.
12. Keep business communication concise, but provide step\-by\-step detail for technical learning.

