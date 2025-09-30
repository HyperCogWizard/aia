"""
AI Agent Implementation

This module contains the AIAgent class that provides functionality for
processing inputs, replication, problem solving, and knowledge sharing.
"""

import logging
from typing import List, Dict, Any, Optional


class AIAgent:
    """
    An AI Agent that can process inputs, manage child agents, and share knowledge.
    
    Attributes:
        name (str): The name of the agent
        child_agents (List[AIAgent]): List of child agents created by this agent
        knowledge_base (List[Dict[str, Any]]): Knowledge base containing learned information
        model (List[Any]): Model components (placeholder for actual ML models)
        tokenizer (List[Any]): Tokenizer components (placeholder for actual tokenizers)
    """
    
    def __init__(self, name: str):
        """
        Initialize the AI Agent.
        
        Args:
            name (str): The name of the agent
        """
        self.name = name
        self.child_agents: List['AIAgent'] = []
        self.knowledge_base: List[Dict[str, Any]] = []
        self.model: List[Any] = []
        self.tokenizer: List[Any] = []
        
        # Set up logging for this agent
        self.logger = logging.getLogger(f"AIAgent.{name}")
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                f'%(asctime)s - AIAgent.{name} - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    def process_input(self, user_input: str) -> str:
        """
        Process user input through tokenization, response generation, and decoding.
        
        Args:
            user_input (str): The input from the user to process
            
        Returns:
            str: The processed response
        """
        # Tokenize input
        tokenized_input = self._tokenize_input(user_input)
        self.logger.info(f"Tokenized input: {tokenized_input}")
        
        # Generate response
        response_tokens = self._generate_response(tokenized_input)
        self.logger.info(f"Generated response tokens: {response_tokens}")
        
        # Decode response
        decoded_response = self._decode_response(response_tokens)
        self.logger.info(f"Decoded response: {decoded_response}")
        
        # Log the learning
        self._log_learning(user_input, decoded_response)
        
        return decoded_response

    def _tokenize_input(self, user_input: str) -> List[str]:
        """
        Tokenize the user input into a list of tokens.
        
        Args:
            user_input (str): Raw user input
            
        Returns:
            List[str]: List of tokens
        """
        # Simple tokenization - split by spaces and punctuation
        import re
        tokens = re.findall(r'\w+|[^\w\s]', user_input.lower())
        return tokens

    def _generate_response(self, tokenized_input: List[str]) -> List[str]:
        """
        Generate response tokens based on tokenized input.
        
        Args:
            tokenized_input (List[str]): Tokenized input
            
        Returns:
            List[str]: Response tokens
        """
        # Simple response generation - echo with processing indicator
        response_tokens = ["processing", ":"] + tokenized_input + [".", "response", "generated"]
        return response_tokens

    def _decode_response(self, response_tokens: List[str]) -> str:
        """
        Decode response tokens into a readable string.
        
        Args:
            response_tokens (List[str]): Response tokens
            
        Returns:
            str: Decoded response string
        """
        return " ".join(response_tokens)

    def _log_learning(self, user_input: str, response: str) -> None:
        """
        Log the learning from this interaction.
        
        Args:
            user_input (str): Original user input
            response (str): Generated response
        """
        learning_entry = {
            "timestamp": self._get_timestamp(),
            "input": user_input,
            "response": response,
            "agent": self.name
        }
        self.knowledge_base.append(learning_entry)
        self.logger.info(f"Logged learning entry: {learning_entry}")

    def _get_timestamp(self) -> str:
        """Get current timestamp as string."""
        from datetime import datetime
        return datetime.now().isoformat()

    def replicate(self, problem: str) -> 'AIAgent':
        """
        Create a child agent to handle a specific problem.
        
        Args:
            problem (str): The problem description that the child agent will focus on
            
        Returns:
            AIAgent: A new child agent specialized for the given problem
        """
        child_name = f"{self.name}_child_{len(self.child_agents) + 1}"
        child_agent = AIAgent(child_name)
        
        # Transfer relevant knowledge to child agent
        child_agent.knowledge_base = self.knowledge_base.copy()
        
        # Add problem-specific knowledge
        problem_knowledge = {
            "timestamp": self._get_timestamp(),
            "type": "problem_assignment",
            "problem": problem,
            "parent_agent": self.name,
            "specialization": problem
        }
        child_agent.knowledge_base.append(problem_knowledge)
        
        # Add to child agents list
        self.child_agents.append(child_agent)
        
        self.logger.info(f"Created child agent '{child_name}' for problem: {problem}")
        return child_agent

    def get_child_agent(self, name: str) -> Optional['AIAgent']:
        """
        Retrieve a child agent by name.
        
        Args:
            name (str): The name of the child agent to retrieve
            
        Returns:
            Optional[AIAgent]: The child agent if found, None otherwise
        """
        for child in self.child_agents:
            if child.name == name:
                return child
        
        self.logger.warning(f"Child agent '{name}' not found")
        return None

    def solve_problem(self, problem: str) -> str:
        """
        Solve a problem using the agent's knowledge and capabilities.
        
        Args:
            problem (str): The problem to solve
            
        Returns:
            str: The solution or response to the problem
        """
        self.logger.info(f"Attempting to solve problem: {problem}")
        
        # Check if we have relevant knowledge
        relevant_knowledge = []
        for entry in self.knowledge_base:
            if any(word in entry.get("input", "").lower() or 
                   word in entry.get("problem", "").lower() 
                   for word in problem.lower().split()):
                relevant_knowledge.append(entry)
        
        # If we have child agents, delegate to specialized ones
        if self.child_agents:
            for child in self.child_agents:
                child_solution = child.solve_problem(problem)
                solution = f"Child agent {child.name} attempted: {child_solution}"
                self.logger.info(f"Problem delegated to child agent: {solution}")
                return solution
        
        # Generate solution based on knowledge
        if relevant_knowledge:
            solution = f"Based on {len(relevant_knowledge)} relevant knowledge entries, solution for '{problem}': Processing complete with learned patterns applied."
        else:
            solution = f"No solution found for: {problem}"
        
        # Log this problem-solving attempt
        self._log_learning(f"PROBLEM: {problem}", solution)
        
        return solution

    def share_knowledge(self, other_agent: 'AIAgent') -> None:
        """
        Share knowledge with another agent.
        
        Args:
            other_agent (AIAgent): The agent to share knowledge with
        """
        if not isinstance(other_agent, AIAgent):
            raise TypeError("Can only share knowledge with other AIAgent instances")
        
        # Count knowledge before sharing
        initial_count = len(other_agent.knowledge_base)
        
        # Share unique knowledge entries
        shared_entries = 0
        for entry in self.knowledge_base:
            # Check if other agent already has this knowledge
            if entry not in other_agent.knowledge_base:
                # Add source information
                shared_entry = entry.copy()
                shared_entry["shared_from"] = self.name
                shared_entry["shared_at"] = self._get_timestamp()
                
                other_agent.knowledge_base.append(shared_entry)
                shared_entries += 1
        
        # Log the knowledge sharing
        knowledge_sharing_log = {
            "timestamp": self._get_timestamp(),
            "type": "knowledge_sharing",
            "shared_to": other_agent.name,
            "entries_shared": shared_entries,
            "total_knowledge_before": initial_count,
            "total_knowledge_after": len(other_agent.knowledge_base)
        }
        
        self.knowledge_base.append(knowledge_sharing_log)
        other_agent.knowledge_base.append(knowledge_sharing_log)
        
        self.logger.info(f"Shared {shared_entries} knowledge entries with {other_agent.name}")
        other_agent.logger.info(f"Received {shared_entries} knowledge entries from {self.name}")

    def get_knowledge_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the agent's current state and knowledge.
        
        Returns:
            Dict[str, Any]: Summary information about the agent
        """
        return {
            "name": self.name,
            "knowledge_entries": len(self.knowledge_base),
            "child_agents": len(self.child_agents),
            "child_agent_names": [child.name for child in self.child_agents],
            "model_components": len(self.model),
            "tokenizer_components": len(self.tokenizer)
        }

    def __repr__(self) -> str:
        """String representation of the AIAgent."""
        return f"AIAgent(name='{self.name}', children={len(self.child_agents)}, knowledge={len(self.knowledge_base)})"