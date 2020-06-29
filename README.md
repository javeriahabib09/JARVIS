# *JARVIS* movie recommender system
This is v0.1.

*JARVIS* is an open-source, conversational movie recommender system which models users
' preferences dynamically and supports user initiatives and multi-turn recommendations. 
*JARVIS* equips with a scaleable structure for future amendments. 
It facilities the standardized components. 
In specific, intent recognition in NLU identifies users' intent based on preferences and
 recognizes entities (movies and attributes) for users' utterances, NLG generates natural language responses based on templates, and dialogue policy in the dialogue manager adapts to the users' requirements in the conversation.

The main architecture is shown in the figure below. A multi-turn conversation is initiated and terminated by the users. The users' response is processed by the NLU. The DM receives the users' dialogue acts from the NLU and generates the agent's dialogue acts. Based on the act from DM, the NLG generates a natural response to the users. This loop happens for each turn in the conversation.


![A sample dialogue in JARVIS](jarvis/_resources/Blueprint_JARVIS.png)

## Main Components in *JARVIS*:
- [Controller](jarvis/jmrs/controller/controller.py)
  - [Controller Telegram Bot](jarvis/jmrs/controller/controller_bot.py)
  - [Controller Terminal](jarvis/jmrs/controller/controller_terminal.py)
- [Conversational Agent](jarvis/jmrs/agent/agent.py)
  - [Natural Language Understanding](jarvis/jmrs/nlu/nlu.py)
    - [Intents Detection](jarvis/jmrs/nlu/user_intents_checker.py)
    - [Slot Filling](jarvis/jmrs/nlu/slot_annotator.py)
    - [Data Loader](jarvis/jmrs/nlu/data_loader.py)
  - [Natural Language Generation](jarvis/jmrs/nlg/nlg.py)
  - [Dialogue Manager](jarvis/jmrs/dialogue_manager/dialogue_manager.py)
    - [Dialogue State Tracker](jarvis/jmrs/dialogue_manager/dialogue_state_tracker.py)
      - [Dialogue State](jarvis/jmrs/dialogue_manager/dialogue_state.py)
      - [Dialogue Context](jarvis/jmrs/dialogue_manager/dialogue_context.py)
    - [Dialogue Policy](jarvis/jmrs/dialogue_manager/dialogue_policy.py)
    - [Dialogue Act](jarvis/jmrs/dialogue_manager/dialogue_act.py)
      - [Item Constraints](jarvis/jmrs/dialogue_manager/item_constraint.py)
      - [Slots](jarvis/jmrs/dialogue_manager/slots.py)
      - [Operator](jarvis/jmrs/dialogue_manager/operator.py)
      - [Values](jarvis/jmrs/dialogue_manager/values.py)
- Intents
   - [User Intents](jarvis/jmrs/intents/user_intents.py)
   - [Agent Intents](jarvis/jmrs/intents/agent_intents.py)
 - Database/Ontology
   - [Database](jarvis/jmrs/database/database.py)
   - [Ontology](jarvis/jmrs/ontology/ontology.py)
   
## External Files in *JARVIS*:
- [Configuration](jarvis/external_files/config/jarvis_config.yaml): This file defines the basic
 configuration of *JARVIS* including the paths to database, ontology and the token of Telegram Bot.
- [Telegram Bot Token](jarvis/external_files/config/bot_token.yaml): This file should contain the
 Telegram Bot Token in the following format:
 
        BOT_TOKEN: <<token>>
        
- [Tag words for NLU](jarvis/external_files/config/tag_words_slots.json): The designed patters for
 detection of slots in NLU are defined in this file. 
- [MySQL Database](jarvis/external_files/data/movies_dbase.db)
- [Ontology](jarvis/external_files/data/movies_ontology.json)
- [Slot-Values](jarvis/external_files/data/slot_values.json): This file must be created by the NLU

## Telegram Bot Token
- To use Telegram, one must install the Telegram application available [here](https://telegram.org/).
- Click [here](https://core.telegram.org/bots#6-botfather) for instructions about how to create a Telegram Bot.
- Add the token of the new bot to the [Telegram Bot Token](jarvis/external_files/config/bot_token.yaml
) file as ``BOT_TOKEN: <<token>>``.

## Running *JARVIS*
Once the Telegram Bot token is added, execute the following commands to execute *JARVIS*

       pip install pyyaml
       pip install python-telegram-bot --upgrade
       pip install wikipedia
       python jarvis.py -c <path_to_config.yaml>
