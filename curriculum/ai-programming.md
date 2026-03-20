# 🤖 AI Programming Module

## Module Overview

**Module ID**: ai-programming  
**Difficulty**: Intermediate to Advanced  
**Duration**: 8-12 hours  
**Prerequisites**: Python basics, API concepts, JSON handling

## Learning Objectives

By completing this module, you will:
- Understand how LLMs work and their capabilities
- Build applications that integrate with AI APIs
- Create AI agents with tool-use capabilities
- Develop MCP (Model Context Protocol) servers
- Implement RAG (Retrieval-Augmented Generation) systems
- Apply prompt engineering best practices
- Build multi-agent orchestration systems

---

## Lesson 1: LLM Fundamentals & API Integration (90 min)

### Overview
Learn how Large Language Models work and how to integrate them into applications.

### Concepts
- What are LLMs and how they work
- Token limits and context windows
- Temperature and other parameters
- API authentication and rate limiting
- Streaming vs. synchronous responses

### Code Examples

#### Basic OpenAI Integration (Python)
```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat(message: str, system_prompt: str = "You are a helpful assistant.") -> str:
    """Send a message to the LLM and get a response."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].message.content

# Usage
result = chat("Explain decorators in Python")
print(result)
```

#### Streaming Responses (Python)
```python
def chat_stream(message: str):
    """Stream a response from the LLM."""
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message}],
        stream=True
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")

chat_stream("Write a haiku about coding")
```

#### TypeScript Integration
```typescript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

async function chat(message: string): Promise<string> {
  const response = await client.chat.completions.create({
    model: "gpt-4",
    messages: [{ role: "user", content: message }],
    temperature: 0.7,
  });

  return response.choices[0].message.content ?? "";
}

// Usage
const result = await chat("Explain TypeScript generics");
console.log(result);
```

### Exercises
1. Create a simple chatbot that remembers conversation history
2. Build a function that summarizes long text using LLM
3. Implement streaming with a progress indicator

---

## Lesson 2: Prompt Engineering (60 min)

### Overview
Learn techniques for crafting effective prompts that produce desired outputs.

### Concepts
- Zero-shot vs. few-shot prompting
- Chain-of-thought reasoning
- System prompts and persona setting
- Output formatting (JSON, markdown, etc.)
- Prompt injection and safety

### Code Examples

#### Structured Output
```python
def extract_info(text: str) -> dict:
    """Extract structured information from text."""
    prompt = f"""Extract the following information from the text below and return as JSON:
- name: person's name
- email: email address
- phone: phone number
- sentiment: positive, negative, or neutral

Text: {text}

Return ONLY valid JSON, no other text."""

    response = chat(prompt)
    return json.loads(response)

# Usage
info = extract_info("Hi, I'm John Doe. My email is john@example.com and I'm very happy with the service!")
# {"name": "John Doe", "email": "john@example.com", "phone": null, "sentiment": "positive"}
```

#### Chain-of-Thought Prompting
```python
def solve_problem(problem: str) -> str:
    """Solve a problem using chain-of-thought reasoning."""
    prompt = f"""Solve this problem step by step. Show your reasoning before giving the final answer.

Problem: {problem}

Think through this step by step:"""

    return chat(prompt)
```

#### Few-Shot Learning
```python
def classify_review(review: str) -> str:
    """Classify a review as positive, negative, or neutral."""
    prompt = f"""Classify the following reviews as positive, negative, or neutral.

Review: "This product is amazing! Best purchase ever."
Category: positive

Review: "Terrible quality, broke after one day."
Category: negative

Review: "It's okay, nothing special."
Category: neutral

Review: "{review}"
Category:"""

    return chat(prompt).strip()
```

### Exercises
1. Create a prompt that extracts action items from meeting notes
2. Build a code review prompt that follows specific guidelines
3. Design a prompt chain for multi-step data processing

---

## Lesson 3: Building AI Agents (120 min)

### Overview
Create AI agents that can use tools and take actions.

### Concepts
- Agent architecture (ReAct, Plan-and-Execute)
- Tool definition and registration
- Function calling with LLMs
- Agent memory and state management
- Error handling and retries

### Code Examples

#### Simple Agent with Tools
```python
from openai import OpenAI
import json

client = OpenAI()

# Define available tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name"
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Perform a mathematical calculation",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to evaluate"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

# Tool implementations
def get_weather(location: str) -> str:
    # Simulated weather API
    return f"Weather in {location}: 72°F, sunny"

def calculate(expression: str) -> str:
    try:
        result = eval(expression)  # Note: In production, use safe evaluation
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"

# Agent loop
def run_agent(user_message: str) -> str:
    messages = [{"role": "user", "content": user_message}]
    
    while True:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        
        message = response.choices[0].message
        
        # If no tool calls, return the response
        if not message.tool_calls:
            return message.content
        
        # Process tool calls
        messages.append(message)
        
        for tool_call in message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            
            if function_name == "get_weather":
                result = get_weather(arguments["location"])
            elif function_name == "calculate":
                result = calculate(arguments["expression"])
            else:
                result = "Unknown function"
            
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })

# Usage
response = run_agent("What's the weather in New York and what is 25 * 4?")
print(response)
```

### Exercises
1. Add more tools (web search, file operations, database queries)
2. Implement conversation memory
3. Build an agent that can plan and execute multi-step tasks

---

## Lesson 4: RAG Systems (120 min)

### Overview
Build Retrieval-Augmented Generation systems that ground LLM responses in your data.

### Concepts
- Embeddings and vector representations
- Vector databases (ChromaDB, Pinecone, etc.)
- Chunking strategies
- Retrieval methods (semantic search, hybrid)
- Context window management

### Code Examples

#### Basic RAG with ChromaDB
```python
import chromadb
from openai import OpenAI
from chromadb.utils import embedding_functions

# Setup
client = chromadb.Client()
openai_client = OpenAI()

# Create embedding function
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="text-embedding-ada-002"
)

# Create collection
collection = client.create_collection(
    name="documents",
    embedding_function=openai_ef
)

# Add documents
documents = [
    "Python decorators are functions that modify other functions.",
    "TypeScript generics allow you to create reusable components.",
    "The async/await pattern simplifies asynchronous programming."
]

collection.add(
    documents=documents,
    ids=["doc1", "doc2", "doc3"]
)

# Query and generate response
def rag_query(question: str) -> str:
    # Retrieve relevant documents
    results = collection.query(
        query_texts=[question],
        n_results=2
    )
    
    context = "\n".join(results["documents"][0])
    
    # Generate response with context
    prompt = f"""Answer the question based on the following context:

Context:
{context}

Question: {question}

Answer:"""
    
    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

# Usage
answer = rag_query("How do decorators work in Python?")
print(answer)
```

### Exercises
1. Build a document Q&A system with PDF ingestion
2. Implement chunking strategies for long documents
3. Add metadata filtering to retrievals

---

## Lesson 5: MCP Server Development (120 min)

### Overview
Create Model Context Protocol servers that provide tools and resources to AI assistants.

### Concepts
- MCP architecture and protocol
- Tool providers and resource providers
- Server implementation patterns
- Integration with AI assistants

### Code Example

#### Simple MCP Server (TypeScript)
```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  { name: "my-mcp-server", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// Define a tool
server.setRequestHandler("tools/list", async () => ({
  tools: [
    {
      name: "greet",
      description: "Generate a greeting message",
      inputSchema: {
        type: "object",
        properties: {
          name: { type: "string", description: "Name to greet" }
        },
        required: ["name"]
      }
    }
  ]
}));

// Handle tool execution
server.setRequestHandler("tools/call", async (request) => {
  if (request.params.name === "greet") {
    const name = request.params.arguments?.name ?? "World";
    return {
      content: [{ type: "text", text: `Hello, ${name}!` }]
    };
  }
  throw new Error("Unknown tool");
});

// Start server
const transport = new StdioServerTransport();
await server.connect(transport);
```

### Exercises
1. Create an MCP server with multiple tools
2. Add resource providers for file access
3. Implement error handling and validation

---

## Projects

### Project 1: AI Chatbot with Memory
Build a chatbot that remembers conversation history and can search past conversations.

**Requirements**:
- Conversation history storage
- Semantic search across conversations
- Context-aware responses
- Export/import functionality

**Estimated Time**: 6-8 hours

### Project 2: RAG Document Assistant
Create a system that answers questions based on uploaded documents.

**Requirements**:
- Document upload (PDF, TXT, MD)
- Automatic chunking and embedding
- Semantic search
- Source citation in responses

**Estimated Time**: 8-12 hours

### Project 3: AI Agent Framework
Build a framework for creating AI agents with tool-use capabilities.

**Requirements**:
- Tool registration system
- Agent execution loop
- Memory management
- Error handling and retries
- Logging and debugging

**Estimated Time**: 12-16 hours

### Project 4: MCP Server
Create an MCP server that provides custom tools to AI assistants.

**Requirements**:
- Multiple tool implementations
- Resource providers
- Proper error handling
- Documentation

**Estimated Time**: 8-12 hours

---

## Assessment Criteria

| Category | Weight | Criteria |
|----------|--------|----------|
| Functionality | 40% | Features work as specified |
| Code Quality | 25% | Clean, well-structured code |
| AI Integration | 20% | Proper API usage, error handling |
| Documentation | 15% | Clear README, code comments |

---

## Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [LangChain Documentation](https://docs.langchain.com/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [MCP Specification](https://modelcontextprotocol.io/)

---

**Module Version**: 2.0  
**Last Updated**: March 2026  
**Focus**: Practical AI Integration