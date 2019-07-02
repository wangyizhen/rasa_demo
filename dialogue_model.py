# -*- coding: utf-8 -*-
# ** Project : rasa_demo
# ** Created by: Yizhen
# ** Date: 2019/7/1
# ** Time: 11:22

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

logging.basicConfig(level='INFO')


def dialogue_model_train():
    dialog_training_data_file = './data/stories.md'
    path_to_model = './models/dialogue'
    agent = Agent('./config/chat_domain.yml', policies=[MemoizationPolicy(), KerasPolicy()])

    agent.train(
        dialog_training_data_file,
        augmentation_factor=50,
        # max_history=2,
        epochs=100,
        batch_size=10,
        validation_split=0.2
    )
    agent.persist(path_to_model)



def dialogue_model_test():
    agent = Agent.load('models/dialogue', interpreter='./models/nlu/default/chat')
    print("Your bot is ready to talk! Type your messages here or send 'stop'")
    while True:
        a = input("User: ")
        if a == 'stop':
            break
        responses = agent.handle_message(a)
        for response in responses:
            print("Robot: ", response["text"])


if __name__ == '__main__':
    pass
    dialogue_model_train()
    dialogue_model_test()
