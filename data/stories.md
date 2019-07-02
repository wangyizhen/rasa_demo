## Generated Story -1361956661909885507
* greet
    - utter_greet
* order_pizza
    - utter_get_pizza_size
* order_pizza
    - utter_get_pizza_toppings
* order_pizza
    - action_order_pizza

## Generated Story -3547075773026053592
* greet
    - utter_greet
* order_pizza
    - utter_get_pizza_size
* order_pizza{"size": "large"}
    - slot{"size": "large"}
    - utter_get_pizza_toppings
* order_pizza{"toppings": "olives"}
    - slot{"toppings": "olives"}
    - action_order_pizza

## Generated Story -5528848379176214771
* greet
    - utter_greet
* order_pizza
    - utter_get_pizza_toppings
* order_pizza{"toppings": "olives"}
    - slot{"toppings": "olives"}
    - utter_get_pizza_size
* order_pizza{"size": "small"}
    - slot{"size": "small"}
    - action_order_pizza