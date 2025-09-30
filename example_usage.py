#!/usr/bin/env python3
"""
Example usage of the AIAgent class

This script demonstrates how to use the AIAgent class with various features
including input processing, agent replication, problem solving, and knowledge sharing.
"""

from ai_agent import AIAgent


def main():
    """Demonstrate AIAgent functionality."""
    print("=== AI Agent Demo ===\n")
    
    # Create a main AI agent
    print("1. Creating main AI agent...")
    main_agent = AIAgent("MainAI")
    print(f"Created: {main_agent}")
    print()
    
    # Process some inputs
    print("2. Processing user inputs...")
    inputs = [
        "Hello, how are you?",
        "I need help with machine learning",
        "Can you solve mathematical problems?"
    ]
    
    for user_input in inputs:
        print(f"Input: {user_input}")
        response = main_agent.process_input(user_input)
        print(f"Response: {response}")
        print()
    
    # Show knowledge accumulated
    print("3. Current knowledge summary:")
    summary = main_agent.get_knowledge_summary()
    print(f"Knowledge entries: {summary['knowledge_entries']}")
    print()
    
    # Create specialized child agents
    print("4. Creating specialized child agents...")
    ml_specialist = main_agent.replicate("Machine Learning Specialist")
    math_specialist = main_agent.replicate("Mathematics Specialist")
    
    print(f"Created ML specialist: {ml_specialist}")
    print(f"Created Math specialist: {math_specialist}")
    print()
    
    # Test child agent retrieval
    print("5. Retrieving child agents...")
    retrieved_ml = main_agent.get_child_agent(ml_specialist.name)
    print(f"Retrieved ML agent: {retrieved_ml}")
    
    # Attempt to retrieve non-existent child
    non_existent = main_agent.get_child_agent("NonExistentAgent")
    print(f"Non-existent agent: {non_existent}")
    print()
    
    # Solve problems using the main agent (delegates to children)
    print("6. Solving problems...")
    problems = [
        "Train a neural network for image classification",
        "Calculate the derivative of x^2 + 3x + 1",
        "Optimize database query performance"
    ]
    
    for problem in problems:
        print(f"Problem: {problem}")
        solution = main_agent.solve_problem(problem)
        print(f"Solution: {solution}")
        print()
    
    # Create another agent and share knowledge
    print("7. Knowledge sharing...")
    secondary_agent = AIAgent("SecondaryAI")
    print(f"Secondary agent before sharing: {secondary_agent.get_knowledge_summary()}")
    
    main_agent.share_knowledge(secondary_agent)
    print(f"Secondary agent after sharing: {secondary_agent.get_knowledge_summary()}")
    print()
    
    # Final summary
    print("8. Final agent summaries:")
    print(f"Main agent: {main_agent.get_knowledge_summary()}")
    print(f"ML specialist: {ml_specialist.get_knowledge_summary()}")
    print(f"Math specialist: {math_specialist.get_knowledge_summary()}")
    print(f"Secondary agent: {secondary_agent.get_knowledge_summary()}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()