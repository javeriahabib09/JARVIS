"""This file contains the Controller which controls the conversation between the agent and the
user."""

__author__ = "Javeria Habib"

from abc import ABC, abstractmethod


class Controller(ABC):
    """This is the main class that controls the other components of the JARVIS Movie Recommendation
    System.
    The controller executes the conversational agent.
    """

    def __init__(self):
        """Initializes some basic structs for the Controller.
        """

    @abstractmethod
    def execute_agent(configuration):
        """Runs the conversational agent and executes the dialogue by calling the basic components
        of Jarvis

        :param configuration: the settings for the agent
        """
        pass
