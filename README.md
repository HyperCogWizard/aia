# aia - AI Agent Implementation

A Python implementation of an AI Agent class that provides functionality for processing inputs, creating specialized child agents, solving problems, and sharing knowledge between agents.

## Features

- **Input Processing**: Tokenizes user input, generates responses, and logs learning
- **Agent Replication**: Creates specialized child agents for specific problem domains
- **Problem Solving**: Delegates problems to appropriate child agents or solves using accumulated knowledge
- **Knowledge Sharing**: Shares learned information between different agents
- **Comprehensive Logging**: Tracks all agent activities and learning

## Usage

```python
from ai_agent import AIAgent

# Create a main agent
agent = AIAgent("MainAgent")

# Process user input
response = agent.process_input("Hello, how can you help me?")
print(response)

# Create specialized child agents
ml_specialist = agent.replicate("Machine Learning Expert")
math_specialist = agent.replicate("Mathematics Expert")

# Solve problems (delegates to child agents)
solution = agent.solve_problem("Train a neural network")
print(solution)

# Share knowledge with other agents
other_agent = AIAgent("OtherAgent")
agent.share_knowledge(other_agent)
```

## Files

- `ai_agent.py` - Main AIAgent class implementation
- `test_ai_agent.py` - Comprehensive test suite
- `example_usage.py` - Demonstration script showing all features

## Running Tests

```bash
python test_ai_agent.py
```

## Running Example

```bash
python example_usage.py
```