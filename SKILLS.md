# AI Engineer Journey

## Goal

Become an AI Engineer, with a focus on LLM applications, Azure OpenAI, RAG, and agentic AI.

## Current Topic

RAG Implementation

## Background

- Software Engineer with Android SDK development experience
- Familiar with REST APIs, HTTP methods, status codes, headers, authentication, serialization, and deserialization
- Comfortable with client\-server architecture
- Learning Python and AI concepts for an AI Engineer role
- Prefer concept\-focused explanations rather than beginner\-level REST API explanations
- Prefer practical examples connected to Android, APIs, accessibility, Azure DevOps, and enterprise AI systems

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
- GitHub repository created for the AI Engineer learning journey

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
- Understanding when DataFrames are more practical than manually processing large JSON collections
- Basic DataFrame interview questions
- Explaining DataFrames conceptually in an interview

### REST APIs

- Understanding client\-server architecture
- Understanding REST APIs
- HTTP GET requests
- HTTP POST requests conceptually
- Request and response flow
- HTTP status codes
- 200 OK
- 201 Created
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 500 Internal Server Error
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
- Understanding that LLM APIs consume prompts rather than traditional business requests
- Understanding that LLM responses are generated rather than retrieved
- Understanding that the networking layer is familiar while model behavior is the new concept
- Understanding token\-based pricing
- Understanding context\-window limitations

### LLM Fundamentals

- Understanding what a Large Language Model is
- Understanding prompts and generated responses
- Understanding deterministic software versus probabilistic model output
- Understanding that an LLM predicts likely output tokens
- Understanding hallucinations
- Understanding why LLM output must be validated
- Basic understanding of responsible AI
- Understanding that an LLM does not automatically know current private or internal information
- Understanding that LLM API calls are generally stateless

### Prompt Engineering

- Understanding prompts as instructions for LLMs
- Role prompting
- Task definition
- Context prompting
- Constraints
- Output formatting
- Zero\-shot prompting
- One\-shot prompting
- Few\-shot prompting
- Basic understanding of Chain\-of\-Thought prompting
- Understanding that good prompts reduce ambiguity
- Understanding that prompt engineering is similar to programming an LLM using natural language
- Designing prompts with role, task, context, constraints, and output format

### Tokens and Context Windows

- Understanding tokens as units processed by an LLM
- Understanding that a token is not always equal to one word
- Input tokens
- Output tokens
- Token\-based billing
- Understanding that input and output tokens can have different costs
- Understanding context windows
- Understanding that input tokens and output tokens must fit within the context window
- Understanding that system instructions also consume context
- Understanding that conversation history consumes context
- Understanding that retrieved documents consume context
- Understanding why full chat history cannot be sent forever
- Understanding that large histories increase cost and latency
- Truncating older messages conceptually
- Summarizing older messages conceptually
- Retrieving only relevant information instead of sending everything

### Temperature and Top\-P

- Understanding temperature
- Understanding Top\-P
- Understanding deterministic versus creative generation
- Understanding that lower temperature generally produces more consistent output
- Understanding that higher temperature generally produces more varied output
- Understanding why lower randomness is preferred for extraction and structured\-data tasks
- Understanding why higher randomness can help with brainstorming and creative tasks
- Understanding that temperature and Top\-P influence token selection

### System, User, and Assistant Messages

- Understanding the system message as instructions defining model behavior
- Understanding the user role as the human's input
- Understanding the assistant role as model output and conversation history
- Understanding that applications manage conversation history
- Understanding that previous messages may need to be sent again as context
- Understanding that the model itself does not automatically retain all previous API requests
- Understanding messages as the foundation of AI chat applications

### OpenAI SDK Concepts

- Understanding the purpose of an AI SDK
- Understanding the OpenAI client as the main SDK object
- Understanding that the client abstracts authentication and request handling
- Understanding that the SDK reduces HTTP boilerplate
- Understanding that the model parameter selects the LLM used for the request
- Understanding that the prompt or input is sent to the selected model
- Understanding why an SDK is usually easier than manually using requests.post()
- Understanding the conceptual similarity between an AI SDK client and Retrofit or an API client
- Understanding the basic request and response flow

### Structured Outputs

- Understanding the difference between natural\-language output and structured output
- Understanding why applications need predictable output
- Understanding JSON as the most common structured\-output format
- Designing structured JSON responses
- Using consistent snake\_case property names
- Selecting appropriate data types for output fields
- Using numbers without quotation marks
- Using JSON booleans such as true and false
- Understanding that true is different from the string "true"
- Understanding how structured outputs reduce manual parsing
- Understanding how structured outputs integrate LLMs with APIs and downstream systems
- Understanding how individual fields support filtering, validation, analytics, and automation

### JSON Schema Concepts

- Understanding a schema as a data contract
- Understanding that valid JSON does not always match the required shape
- Defining expected field names conceptually
- Defining expected field types conceptually
- Understanding required fields
- Understanding why applications should control the response structure
- Understanding that two valid JSON responses can still be incompatible
- Understanding that schemas make LLM output more predictable

### LLM Output Validation

- JSON syntax validation
- Schema validation
- Business\-rule validation
- Recognizing malformed JSON
- Recognizing missing or incorrectly named fields
- Recognizing incorrect data types
- Recognizing values that violate allowed business rules
- Understanding that syntactically valid JSON can still contain invalid business data
- Understanding why AI\-generated output must be validated before downstream use
- Understanding the need to reject, retry, normalize, or safely handle invalid output

### Function Calling and Tool Calling

- Understanding function calling
- Understanding tool calling
- Understanding that an LLM cannot directly access live external systems by itself
- Understanding how an LLM decides that external data or an action is required
- Understanding that tools retrieve live or private data
- Understanding that tools can perform external actions
- Understanding that the application executes the actual function or tool
- Understanding that tool results are returned to the LLM
- Understanding that the LLM interprets tool results and generates a human\-readable answer
- Understanding that an LLM does not directly execute arbitrary functions by itself
- Understanding the difference between an LLM response and a tool action
- Understanding how Azure DevOps bug data could be retrieved using a tool
- Understanding how structured arguments can be safely passed to external tools
- Understanding how validation should happen before executing an action

### Structured Outputs with Tool Calling

- Extracting required fields from natural\-language input
- Returning predictable JSON
- Validating the extracted information
- Passing validated data to an external tool
- Receiving structured results from the tool
- Converting tool results into a human\-readable answer
- Understanding the flow from user request to LLM, structured data, validation, tool execution, and final response
- Understanding why structured outputs improve tool\-calling reliability
- Understanding how these concepts support agent workflows

### Embeddings

- Basic understanding of embeddings
- Understanding embeddings as numerical representations of meaning
- Understanding that embeddings support semantic similarity
- Understanding that semantic search compares meaning rather than only exact words
- Understanding why "login issue" and "sign\-in problem" may have similar embeddings
- Understanding that embedding models learn semantic patterns from large amounts of training text
- Understanding that text appearing in similar contexts can be represented near each other
- Understanding that the individual vector numbers are not manually interpreted
- Understanding that relative distance and similarity are more important than individual vector values
- Understanding that different embedding models can produce different values for the same text
- Understanding that different models may produce vectors with different numbers of dimensions
- Understanding that embedding values from different models are generally incompatible
- Understanding why document embeddings and query embeddings should be created with the same embedding model
- Understanding that the embedding model creates the vectors
- Understanding that the vector\-search system compares the vectors
- Understanding that the vector database itself does not understand English

### Vector Search and Vector Databases

- Understanding vector search
- Understanding semantic search
- Understanding the difference between keyword search and vector search
- Understanding that keyword search looks for matching words
- Understanding that vector search looks for similar meaning
- Understanding a vector database as a system that stores and searches embeddings
- Understanding similarity search conceptually
- Understanding nearest\-neighbor search conceptually
- Understanding that similar vectors are retrieved as relevant results
- Understanding that the query is converted into an embedding before searching
- Understanding that stored document embeddings are compared with the query embedding
- Understanding that the most similar results can be returned as top results
- Basic awareness of Azure AI Search as a Microsoft search technology used in AI solutions
- Basic awareness of other vector\-search and vector\-database products

### Chunking and Indexing

- Understanding why large documents should be divided into smaller chunks
- Understanding that a single embedding for a very large document can dilute meaning
- Understanding that each chunk can receive its own embedding
- Understanding how focused chunks improve retrieval accuracy
- Understanding that excessively small chunks can lose surrounding context
- Understanding that excessively large chunks can reduce retrieval precision
- Understanding chunk overlap conceptually
- Understanding why overlap preserves information across chunk boundaries
- Understanding indexing as the preparation and storage of searchable document content
- Understanding that indexing can include chunk text, embeddings, and metadata
- Understanding that RAG retrieves relevant chunks rather than always retrieving an entire document

### RAG Fundamentals

- Understanding RAG as Retrieval\-Augmented Generation
- Understanding the Retrieval step
- Understanding the Augmentation step
- Understanding the Generation step
- Understanding that retrieval finds relevant external information
- Understanding that augmentation adds retrieved information to the model's prompt or context
- Understanding that generation uses the question and retrieved context to produce an answer
- Understanding that RAG does not retrain the LLM
- Understanding that RAG provides knowledge at request time
- Understanding how RAG can use current, private, and company\-specific information
- Understanding that RAG can reduce unsupported answers by grounding the model in retrieved information
- Understanding that RAG does not guarantee correctness
- Understanding that retrieval quality affects answer quality
- Understanding that irrelevant retrieved content can lead to poor answers
- Understanding that retrieved context still consumes tokens
- Understanding why only the most relevant chunks should be provided
- Understanding the complete conceptual RAG pipeline

### RAG Pipeline

- User submits a question
- The system creates an embedding for the question
- Vector search compares the query embedding with stored chunk embeddings
- Relevant chunks are retrieved
- Retrieved chunks are added to the prompt as context
- The prompt is sent to the LLM
- The LLM generates an answer based on the supplied context
- The application returns the answer to the user
- The application may include citations or source references
- The application should validate and monitor the generated answer

### RAG vs Fine\-Tuning

- Understanding that RAG and fine\-tuning solve different problems
- Understanding that RAG adds external knowledge at runtime
- Understanding that fine\-tuning changes model behavior or learned response patterns
- Understanding that RAG is useful for frequently changing information
- Understanding that RAG is useful for internal company documents
- Understanding that knowledge sources can be updated without retraining the LLM
- Understanding that fine\-tuning is not usually the first choice for frequently changing documents
- Understanding that RAG and fine\-tuning can be used together
- Mental model: RAG gives the model relevant reference material before answering
- Mental model: Fine\-tuning changes how the model behaves

### AI Agents

- Basic understanding of AI Agents
- Understanding an agent as an LLM\-based system that can reason about a goal and use tools
- Understanding LLM \+ instructions \+ tools \+ memory \+ workflow conceptually
- Understanding that an agent may choose between available tools
- Understanding that agents can retrieve information or perform actions
- Understanding the difference between a standalone LLM and an agent
- Understanding that an LLM generates output from supplied context
- Understanding that an agent combines an LLM with external capabilities
- Understanding that tool results may be fed back to the model
- Understanding that agents require validation, permissions, and safety controls
- Understanding accessibility bug analysis as a potential agent workflow

### Projects

- ATM mini\-project
- Used variables, conditions, functions, loops, error handling, and user input
- Implemented PIN validation
- Implemented balance checking
- Implemented deposits
- Implemented withdrawals
- Implemented insufficient\-balance validation
- Implemented a repeating menu using while
- Implemented program exit using break

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

## Conceptually Completed Lessons

- Tokens and context windows
- Prompt engineering
- System, user, and assistant messages
- OpenAI SDK concepts
- Structured outputs
- JSON Schema concepts
- LLM output validation
- Function and tool calling
- Embeddings
- Vector search
- Vector databases
- Chunking and indexing
- RAG fundamentals
- RAG versus fine\-tuning
- AI Agent fundamentals

## Current File

ai\-basics/26\_rag\_basics.py

## Current Lesson

Build a basic RAG application in Python

## Current Learning Goals

- Move from RAG theory to a small working Python implementation
- Understand the difference between document ingestion and query\-time retrieval
- Create document chunks in Python
- Generate embeddings through an embedding model
- Store or manage embeddings for a small learning example
- Convert a user query into an embedding
- Compare query and document embeddings
- Retrieve the most relevant chunks
- Construct an augmented prompt
- Send the grounded prompt to an LLM
- Generate an answer using retrieved context
- Understand citations and source attribution
- Understand retrieval\-quality evaluation
- Learn Azure OpenAI fundamentals
- Learn Azure AI Search fundamentals
- Implement structured outputs using a schema
- Implement function or tool calling
- Build a basic AI Agent
- Build an end\-to\-end AI project

## Next Topics

1. Build a basic RAG pipeline in Python
2. Document ingestion versus query\-time retrieval
3. Embedding generation using Python
4. Similarity calculation
5. Retrieval of top matching chunks
6. Prompt augmentation
7. Grounded answer generation
8. Source attribution and citations
9. RAG retrieval evaluation
10. Azure OpenAI
11. Azure AI Search
12. Practical Structured Outputs
13. Practical Tool Calling
14. AI Agents in Practice
15. Agent memory and state
16. Semantic Kernel
17. Evaluation and Responsible AI
18. End\-to\-End AI Assistant Project

## Planned Files

- ai\-basics/19\_tokens\_and\_context.py
- ai\-basics/20\_prompt\_engineering.py
- ai\-basics/21\_openai\_sdk.py
- ai\-basics/22\_structured\_outputs.py
- ai\-basics/23\_tool\_calling.py
- ai\-basics/24\_embeddings.py
- ai\-basics/25\_vector\_search.py
- ai\-basics/26\_rag\_basics.py
- ai\-basics/27\_agents\_and\_tools.py
- ai\-basics/28\_azure\_openai.py
- ai\-basics/29\_azure\_ai\_search.py
- ai\-basics/30\_semantic\_kernel.py
- ai\-projects/01\_ai\_assistant.py

## Recommended Practical Learning Sequence

1. Review the conceptual RAG pipeline
2. Create a small in\-memory document collection
3. Split the documents into chunks
4. Generate embeddings
5. Calculate similarity
6. Retrieve the most relevant chunks
7. Add the retrieved chunks to the prompt
8. Generate an answer using the augmented prompt
9. Add structured output
10. Add source references
11. Add validation and error handling
12. Replace local retrieval with Azure AI Search
13. Replace standalone calls with an agent workflow

## Learning Approach

- Use existing Android and software engineering experience when explaining APIs and architecture
- Avoid repeating basic HTTP and REST concepts unless needed
- Focus on concepts that are new for AI Engineering
- Connect Python concepts to real AI applications
- Connect examples to accessibility engineering where useful
- Prefer small practical examples over long theoretical explanations
- Build understanding before introducing frameworks
- Learn one major topic at a time
- Add a short exercise after each explanation
- Review an exercise before moving to the next topic
- Prefer Azure OpenAI and Microsoft AI technologies where appropriate
- Avoid unnecessary tools, tracking systems, and complex project structures
- Separate conceptual completion from practical implementation
- Do not mark an implementation complete until the Python code has been created and tested

## Instructions for Copilot

1. Read this file before continuing my AI Engineer lessons.
2. Use the completed topics and files to understand my existing knowledge.
3. Do not restart completed Python fundamentals unless I request a revision.
4. Remember that I already understand Android networking, REST APIs, HTTP, and serialization.
5. Explain new AI concepts in simple language while respecting my software engineering background.
6. Teach only one major topic at a time.
7. Give me a short practical exercise after each explanation.
8. Connect concepts to realistic AI Engineer use cases.
9. Use accessibility, Azure DevOps, Android, and enterprise AI examples where helpful.
10. Avoid unnecessary tools or overcomplicated project structures.
11. Clearly distinguish conceptual understanding from completed practical implementation.
12. Do not mark a file as completed unless I have created or run it.
13. When I complete a lesson, provide a complete replacement version of this file.
14. Always state the exact filename and topic to continue with next.
15. Keep business communication concise, but provide step\-by\-step detail for technical learning.
16. Correct my answers directly but explain the reason in simple language.
17. When introducing code, explain the purpose of each important line.
18. Do not jump to LangChain or Semantic Kernel before I understand the basic implementation.
19. Prefer direct SDK and Python examples before introducing orchestration frameworks.
20. Keep exercises short, practical, and connected to the current lesson.

