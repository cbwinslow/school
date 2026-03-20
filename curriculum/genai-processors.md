# 🔧 GenAI Processors Library Module

## Module Overview

**Module ID**: genai-processors  
**Difficulty**: Intermediate to Advanced  
**Duration**: 4-6 hours  
**Prerequisites**: Python async/await, basic LLM concepts

## Learning Objectives

By completing this module, you will:
- Understand the GenAI Processors architecture
- Build modular, composable AI pipelines
- Implement asynchronous content processing
- Create custom processors for your applications
- Work with streaming data in AI applications

## About GenAI Processors

GenAI Processors is a lightweight Python library by Google that enables efficient, parallel content processing. It addresses fragmentation of LLM APIs through three core pillars:

1. **Unified Content Model**: A single, consistent representation for inputs and outputs across models
2. **Processors**: Simple, composable Python classes that transform content streams using native asyncio
3. **Streaming**: Asynchronous streaming capabilities built-in by default

### Repository
- **GitHub**: https://github.com/google-gemini/genai-processors
- **PyPI**: `pip install genai-processors`
- **Documentation**: https://google-gemini.github.io/genai-processors/
- **License**: Apache 2.0

---

## Lesson 1: Understanding the Architecture (45 min)

### Core Concepts

#### The Processor Pattern

A `Processor` encapsulates a unit of work. It has two interfaces:

1. **Producer Interface** (for processor author): Takes input, yields output
2. **Consumer Interface** (for caller): Provides input, gets output stream

```python
from typing import AsyncIterable
from genai_processors import content_api
from genai_processors import processor

class EchoProcessor(processor.Processor):
    # PRODUCER interface
    async def call(
        self, 
        content: content_api.ProcessorStream
    ) -> AsyncIterable[content_api.ProcessorPartTypes]:
        async for part in content:
            yield part
```

#### Using a Processor

```python
# CONSUMER interface - multiple ways to consume output

# 1. Gather all outputs
result = await simple_text_processor(input_content).gather()

# 2. Get text directly (for text-only)
text = await simple_text_processor(input_content).text()

# 3. Stream parts as they arrive
async for part in simple_text_processor(input_content):
    print(part.text, end="")
```

### Key Components

#### ProcessorPart
A wrapper around `genai.types.Part` with metadata:
- MIME type
- Role (user/model)
- Custom attributes

#### ProcessorContent
Collection of ProcessorParts representing complete content.

#### ProcessorStream
Async stream of ProcessorParts for real-time processing.

### Exercises

1. Create a simple EchoProcessor that returns input unchanged
2. Create a processor that uppercases all text content
3. Test both gather() and streaming consumption

---

## Lesson 2: Building Custom Processors (60 min)

### Processor Types

#### Basic Processor
```python
from genai_processors import processor

class MyProcessor(processor.Processor):
    async def call(self, content):
        async for part in content:
            # Process each part
            yield processed_part
```

#### PartProcessor (for transforming individual parts)
```python
from genai_processors import processor

class UppercaseProcessor(processor.PartProcessor):
    async def process_part(self, part):
        if part.text:
            return part.with_text(part.text.upper())
        return part
```

### Chaining Processors

Use `+` to chain processors sequentially:
```python
pipeline = processor1 + processor2 + processor3
result = await pipeline(input).gather()
```

Use `//` to parallelize:
```python
parallel = processor1 // processor2  # Run concurrently
result = await parallel(input).gather()
```

### Built-in Processors

#### GenaiModel
For turn-based Gemini API calls:
```python
from genai_processors.core import genai_model

model = genai_model.GenaiModel(
    model_name="gemini-2.0-flash",
    api_key="your-key"
)

response = await model("Hello, how are you?").text()
```

#### LiveProcessor
For real-time streaming with Gemini Live API:
```python
from genai_processors.core import live_processor

live = live_processor.LiveProcessor(
    model_name="gemini-2.0-flash-live",
    api_key="your-key"
)
```

### Exercises

1. Create a processor that counts words in text
2. Create a processor that extracts JSON from text
3. Chain two processors together
4. Build a simple text summarization pipeline

---

## Lesson 3: Advanced Patterns (60 min)

### Error Handling

```python
class SafeProcessor(processor.Processor):
    async def call(self, content):
        try:
            async for part in content:
                yield await self.process(part)
        except Exception as e:
            yield content_api.ProcessorPart(
                text=f"Error: {e}",
                role="error"
            )
```

### Stateful Processors

```python
class ConversationProcessor(processor.Processor):
    def __init__(self):
        self.history = []
    
    async def call(self, content):
        async for part in content:
            self.history.append(part)
            # Process with context
            yield await self.process_with_history(part)
```

### Stream Manipulation

```python
# Split stream
async def split_by_paragraph(stream):
    buffer = []
    async for part in stream:
        if part.text and "\n\n" in part.text:
            # Yield accumulated
            yield content_api.ProcessorContent(buffer)
            buffer = []
        buffer.append(part)
    if buffer:
        yield content_api.ProcessorContent(buffer)
```

### Custom Content Types

```python
class JsonPart(content_api.ProcessorPart):
    def __init__(self, data: dict):
        super().__init__(
            text=json.dumps(data),
            mime_type="application/json"
        )
    
    @property
    def data(self) -> dict:
        return json.loads(self.text)
```

### Exercises

1. Build a conversation-aware chatbot processor
2. Create a processor that batches requests
3. Implement retry logic with exponential backoff
4. Build a custom content type for structured data

---

## Lesson 4: Real-World Applications (60 min)

### Use Case 1: Research Agent

```python
from genai_processors import processor
from genai_processors.core import genai_model

class ResearchAgent(processor.Processor):
    def __init__(self):
        self.model = genai_model.GenaiModel("gemini-2.0-flash")
        self.search_tool = SearchProcessor()
    
    async def call(self, query):
        # Step 1: Analyze query
        search_terms = await self.extract_terms(query)
        
        # Step 2: Search (parallel)
        results = await (self.search_tool // self.search_tool)(search_terms).gather()
        
        # Step 3: Synthesize
        synthesis = await self.model(results).text()
        
        yield content_api.ProcessorPart(synthesis)
```

### Use Case 2: Real-Time Audio Agent

```python
from genai_processors.core import live_processor

class AudioAgent(processor.Processor):
    def __init__(self):
        self.live = live_processor.LiveProcessor(
            model_name="gemini-2.0-flash-live",
            modalities=["audio", "text"]
        )
    
    async def call(self, audio_stream):
        async for response in self.live(audio_stream):
            yield response
```

### Use Case 3: Content Moderation Pipeline

```python
class ModerationPipeline(processor.Processor):
    def __init__(self):
        self.safety_check = SafetyProcessor()
        self.quality_check = QualityProcessor()
        self.transform = ContentTransformProcessor()
    
    async def call(self, content):
        # Parallel safety and quality checks
        checks = await (self.safety_check // self.quality_check)(content).gather()
        
        if checks.safe and checks.quality_ok:
            async for part in self.transform(content):
                yield part
        else:
            yield content_api.ProcessorPart("Content rejected", role="system")
```

### Project: Build a Multi-Modal Assistant

Combine everything you've learned to build an assistant that:
1. Accepts text, image, and audio input
2. Routes to appropriate processors
3. Maintains conversation context
4. Streams responses in real-time
5. Handles errors gracefully

---

## Assessment Criteria

| Category | Weight | Criteria |
|----------|--------|----------|
| Functionality | 40% | Processors work as specified |
| Code Quality | 25% | Clean, async best practices |
| Architecture | 20% | Proper use of Processor pattern |
| Documentation | 15% | Clear docstrings and README |

---

## Resources

- [GenAI Processors Documentation](https://google-gemini.github.io/genai-processors/)
- [Content API Colab](https://colab.research.google.com/github/google-gemini/genai-processors/blob/main/notebooks/content_api_intro.ipynb)
- [Processor Intro Colab](https://colab.research.google.com/github/google-gemini/genai-processors/blob/main/notebooks/processor_intro.ipynb)
- [Create Your Own Processor Colab](https://colab.research.google.com/github/google-gemini/genai-processors/blob/main/notebooks/create_your_own_processor.ipynb)
- [Live API Colab](https://colab.research.google.com/github/google-gemini/genai-processors/blob/main/notebooks/live_processor_intro.ipynb)

---

**Module Version**: 1.0  
**Last Updated**: March 2026  
**Source**: Google Gemini GenAI Processors Library