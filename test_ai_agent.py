"""
Test suite for AIAgent class

Basic tests to validate the functionality of the AIAgent implementation.
"""

import unittest
import sys
import os

# Add the current directory to the path so we can import ai_agent
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ai_agent import AIAgent


class TestAIAgent(unittest.TestCase):
    """Test cases for AIAgent class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.agent = AIAgent("TestAgent")
    
    def test_initialization(self):
        """Test that AIAgent initializes correctly."""
        self.assertEqual(self.agent.name, "TestAgent")
        self.assertEqual(len(self.agent.child_agents), 0)
        self.assertEqual(len(self.agent.knowledge_base), 0)
        self.assertEqual(len(self.agent.model), 0)
        self.assertEqual(len(self.agent.tokenizer), 0)
    
    def test_process_input(self):
        """Test the process_input method."""
        result = self.agent.process_input("Hello world!")
        self.assertIsInstance(result, str)
        self.assertIn("hello", result.lower())
        self.assertIn("world", result.lower())
        
        # Check that knowledge was logged
        self.assertEqual(len(self.agent.knowledge_base), 1)
        self.assertEqual(self.agent.knowledge_base[0]["input"], "Hello world!")
    
    def test_replicate(self):
        """Test the replicate method."""
        problem = "Solve math equations"
        child_agent = self.agent.replicate(problem)
        
        self.assertIsInstance(child_agent, AIAgent)
        self.assertEqual(len(self.agent.child_agents), 1)
        self.assertIn("TestAgent_child_1", child_agent.name)
        
        # Check that child has inherited knowledge
        self.assertEqual(len(child_agent.knowledge_base), 1)  # Problem assignment entry
    
    def test_get_child_agent(self):
        """Test the get_child_agent method."""
        # Test with no children
        result = self.agent.get_child_agent("nonexistent")
        self.assertIsNone(result)
        
        # Create a child and test retrieval
        child = self.agent.replicate("Test problem")
        retrieved_child = self.agent.get_child_agent(child.name)
        self.assertEqual(retrieved_child, child)
    
    def test_solve_problem(self):
        """Test the solve_problem method."""
        problem = "Test problem to solve"
        solution = self.agent.solve_problem(problem)
        
        self.assertIsInstance(solution, str)
        self.assertIn("problem", solution.lower())
        
        # Check that the problem-solving was logged
        self.assertEqual(len(self.agent.knowledge_base), 1)
    
    def test_solve_problem_with_child_agents(self):
        """Test problem solving with child agents."""
        # Create a child agent
        child = self.agent.replicate("Math problems")
        
        # Solve a problem
        problem = "Calculate 2 + 2"
        solution = self.agent.solve_problem(problem)
        
        self.assertIsInstance(solution, str)
        self.assertIn("child agent", solution.lower())
    
    def test_share_knowledge(self):
        """Test the share_knowledge method."""
        # Create another agent
        other_agent = AIAgent("OtherAgent")
        
        # Add some knowledge to the first agent
        self.agent.process_input("Learning something new")
        
        # Share knowledge
        self.agent.share_knowledge(other_agent)
        
        # Check that knowledge was shared
        self.assertGreater(len(other_agent.knowledge_base), 0)
        
        # Check that sharing was logged
        sharing_logs = [entry for entry in self.agent.knowledge_base 
                       if entry.get("type") == "knowledge_sharing"]
        self.assertEqual(len(sharing_logs), 1)
    
    def test_share_knowledge_type_error(self):
        """Test that share_knowledge raises TypeError for invalid input."""
        with self.assertRaises(TypeError):
            self.agent.share_knowledge("not an agent")
    
    def test_get_knowledge_summary(self):
        """Test the get_knowledge_summary method."""
        summary = self.agent.get_knowledge_summary()
        
        self.assertIsInstance(summary, dict)
        self.assertEqual(summary["name"], "TestAgent")
        self.assertEqual(summary["knowledge_entries"], 0)
        self.assertEqual(summary["child_agents"], 0)
        self.assertEqual(summary["child_agent_names"], [])
    
    def test_repr(self):
        """Test the string representation of AIAgent."""
        repr_str = repr(self.agent)
        self.assertIn("AIAgent", repr_str)
        self.assertIn("TestAgent", repr_str)
    
    def test_integration_workflow(self):
        """Test a complete workflow integration."""
        # Create main agent
        main_agent = AIAgent("MainAgent")
        
        # Process some input
        main_agent.process_input("I need help with data analysis")
        
        # Create specialized child agent
        data_child = main_agent.replicate("Data analysis specialist")
        
        # Let child solve a problem
        solution = data_child.solve_problem("Analyze dataset trends")
        self.assertIsInstance(solution, str)
        
        # Create another agent and share knowledge
        secondary_agent = AIAgent("SecondaryAgent")
        main_agent.share_knowledge(secondary_agent)
        
        # Verify knowledge was shared
        self.assertGreater(len(secondary_agent.knowledge_base), 0)
        
        # Get summary
        summary = main_agent.get_knowledge_summary()
        self.assertEqual(summary["child_agents"], 1)
        self.assertGreater(summary["knowledge_entries"], 0)


if __name__ == "__main__":
    unittest.main()