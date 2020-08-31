# *JARVIS* movie recommender system
This is v0.1.

*JARVIS* is an open-source, conversational movie recommender system which models users
' preferences dynamically and supports user initiatives and multi-turn recommendations.
*JARVIS* equips with a scaleable structure for future amendments.
It facilities the standardized components.
In specific, intent recognition in NLU identifies users' intent based on preferences and
 recognizes entities (movies and attributes) for users' utterances, NLG generates natural language responses based on templates, and dialogue policy in the dialogue manager adapts to the users' requirements in the conversation.

The main architecture is shown in the figure below. A multi-turn conversation is initiated and terminated by the users. The users' response is processed by the NLU. The DM receives the users' dialogue acts from the NLU and generates the agent's dialogue acts. Based on the act from DM, the NLG generates a natural response to the users. This loop happens for each turn in the conversation.


![A sample dialogue in JARVIS](doc/Blueprint_JARVIS.png)

## Main Components in *JARVIS*:
- [Controller](jmrs/controller/controller.py)
  - [Controller Telegram Bot](jmrs/controller/controller_bot.py)
  - [Controller Terminal](jmrs/controller/controller_terminal.py)
- [Conversational Agent](jmrs/agent/agent.py)
  - [Natural Language Understanding](jmrs/nlu/nlu.py)
    - [Intents Detection](jmrs/nlu/user_intents_checker.py)
    - [Slot Filling](jmrs/nlu/slot_annotator.py)
    - [Data Loader](jmrs/nlu/data_loader.py)
  - [Natural Language Generation](jmrs/nlg/nlg.py)
  - [Dialogue Manager](jmrs/dialogue_manager/dialogue_manager.py)
    - [Dialogue State Tracker](jmrs/dialogue_manager/dialogue_state_tracker.py)
      - [Dialogue State](jmrs/dialogue_manager/dialogue_state.py)
      - [Dialogue Context](jmrs/dialogue_manager/dialogue_context.py)
    - [Dialogue Policy](jmrs/dialogue_manager/dialogue_policy.py)
    - [Dialogue Act](jmrs/dialogue_manager/dialogue_act.py)
      - [Item Constraints](jmrs/dialogue_manager/item_constraint.py)
      - [Slots](jmrs/dialogue_manager/slots.py)
      - [Operator](jmrs/dialogue_manager/operator.py)
      - [Values](jmrs/dialogue_manager/values.py)
- Intents
   - [User Intents](jmrs/intents/user_intents.py)
   - [Agent Intents](jmrs/intents/agent_intents.py)
 - Database/Ontology
   - [Database](jmrs/database/database.py)
   - [Ontology](jmrs/ontology/ontology.py)

## Data and Configuration files in *JARVIS*:
- [Configuration](data_and_config/config/jarvis_config.yaml): This file defines the basic
 configuration of *JARVIS* including the paths to database, ontology and the token of Telegram Bot.
- [Telegram Bot Token](data_and_config/config/bot_token.yaml): This file should contain the
 Telegram Bot Token in the following format:

        BOT_TOKEN: <<token>>

- [Tag words for NLU](data_and_config/config/tag_words_slots.json): The designed patters for
 detection of slots in NLU are defined in this file.
- [MySQL Database](data_and_config/data/movies_dbase.db)
- [Ontology](data_and_config/data/movies_ontology.json)
- [Slot-Values](data_and_config/data/slot_values.json): This file must be created by the NLU

## *JARVIS* Installation

### Telegram Bot Token
- To use Telegram, one must install the Telegram application available [here](https://telegram.org/).
- Click [here](https://core.telegram.org/bots#6-botfather) for instructions about how to create a Telegram Bot.
- Add the token of the new bot to the [Telegram Bot Token](data_and_config/config/bot_token.yaml
) file as ``BOT_TOKEN: <<token>>``.

### Conversation History folder
Create a folder named `conversation_history`. The conversational logs will be saved in this folder if allowed in the config file. These logs will be created when the *JARVIS* is being executed on Telegram.

### Python Libraries
- Execute the following commands to install necessary libraries for *JARVIS*

       pip install pyyaml
       pip install python-telegram-bot --upgrade
       pip install wikipedia
       pip install nltk
       
### nltk Resources
       nltk.download('punkt')
       nltk.download('wordnet')
       nltk.download('stopwords')
	   
## Running *JARVIS*

       python jarvis.py -c <path_to_config.yaml>
       
Note: To create Slot-Values, execute the code once by setting `BOT: False` n the configuration file.