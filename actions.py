# -*- coding: utf-8 -*-
# ** Project : rasa_demo
# ** Created by: Yizhen
# ** Date: 2019/7/1
# ** Time: 12:11
from rasa_core.actions import Action


class ActionOrderPizza(Action):
    # 在 story 裡 action 的名称则是使用此 class 的def name的回传值
    # Action API 的接口会是在此class的def run，chatbot 会传入多组参数
    def name(self):
        return 'action_order_pizza'

    def run(self, dispatcher, tracker, domain):
        """
        1.使用template的回话: dispatcher.utter_template(utter_reply, my_variable='some')
        2.回传message: dispatcher.utter_message(msg)
        3.取得slot资讯: tracker.get_slot(<slot key>)
        :param dispatcher:
        :param tracker:
        :param domain:
        :return:
        """
        msg = 'Ordering Pizza is completed! It should be with you soon :)'
        # print(msg)
        dispatcher.utter_message(msg)