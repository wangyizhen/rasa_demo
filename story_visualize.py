# -*- coding: utf-8 -*-
# ** Project : rasa_demo
# ** Created by: Yizhen
# ** Date: 2019/7/2
# ** Time: 16:24

"""
method 1:
直接执行
python -m rasa_core.visualize -d config/chat_domain.yml -s data/stories.md -o graph.jpg

"""



import logging

from rasa_core.agent import Agent
from rasa_core.policies import MemoizationPolicy, KerasPolicy

logger = logging.getLogger(__name__)

agent = Agent('config/chat_domain.yml', policies=[MemoizationPolicy(), KerasPolicy()])

nlu_data = None

logger.info("Starting to visualize stories...")
agent.visualize('data/stories.md', 'graph.jpg', 10, nlu_training_data=nlu_data)
