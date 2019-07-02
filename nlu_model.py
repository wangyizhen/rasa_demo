# -*- coding: utf-8 -*-
# ** Project : hackernoon
# ** Created by: Yizhen
# ** Date: 2019/7/1
# ** Time: 10:10

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_nlu.config import load
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu.training_data import load_data


def train(data, config, model_dir):
    training_data = load_data(data)
    configuration = load(config)
    trainer = Trainer(configuration)
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name='chat')
    print('model_directory:{}'.format(model_directory))


def run():
    interpreter = Interpreter.load('./models/nlu/default/chat')
    print(interpreter.parse('I want to order pizza'))
    # print(interpreter.parse(u'What is the reivew for the movie Die Hard?'))


if __name__ == '__main__':
    train('./data/training_data.json', './config/config.yml', './models/nlu')
    run()
