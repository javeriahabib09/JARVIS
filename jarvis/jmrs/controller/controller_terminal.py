"""This file contains the Controller class which controls the flow of the conversation while the
user interacts with the agent using python console"""

__author__ = "Javeria Habib"

from jmrs.agent.agent import Agent
from jmrs.controller.controller import Controller


class ControllerTerminal(Controller):
    """This is the main class that controls the other components of the JARVIS Movie Recommendation
    System.
    The controller executes the conversational agent.
    """

    def __init__(self):
        """Initializes some basic structs for the Controller.
        """

    def execute_agent(self, configuration):
        """Runs the conversational agent and executes the dialogue by calling the basic components
        of Jarvis

        :param configuration: the settings for the agent
        """
        agent = Agent(configuration)
        agent.initialize()
        user_options = {}
        agent_response, user_options = agent.start_dialogue()
        print(f'AGENT: {agent_response}')
        while not agent.terminated_dialogue():
            user_utterance = input("User: ")
            agent_response, user_options = agent.continue_dialogue(user_utterance, user_options)
            print(f'AGENT: {agent_response}')
            if user_options:
                print(list(user_options.values()))
        agent.end_dialogue()
