from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet


class ActionRequestPrice(Action):
    def name(self):
        return 'action_request_price'

    def run(self, dispatcher, tracker, domain):
        missing_params = ["quantity", "tenor", "currency", "product", "client"]
        params = {x: "" for x in missing_params}

        for x in list(missing_params):
            if tracker.current_slot_values().get(x):
                params[x] = tracker.current_slot_values().get(x)
                missing_params.remove(x)

        if missing_params:
            dispatcher.utter_message("Please provide the following parameters: {}".format(",".join(missing_params)))
            return []

        rfqID = "abc123"
        dispatcher.utter_message("Got it, pricing now... {} {} {} {} for {} - RFQ ID: {}".format(
            params['quantity'], params['tenor'], params['currency'], params['product'], params['client'], rfqID
        ))

        dispatcher.utter_message("Trader quoted: {}/{} for RFQ ID: {}".format(6.05, 6.03, rfqID))
        dispatcher.utter_message("Would you like to buy/sell (ClientPay/ClientReceive) on RFQ ID: {}".format(6.05, 6.03, rfqID))

        return [
            SlotSet("quantity"),
            SlotSet("tenor"),
            SlotSet("currency"),
            SlotSet("product"),
            SlotSet("client"),
            SlotSet("rfqID", rfqID)
        ]


class ActionSetDirection(Action):
    def name(self):
        return 'action_set_direction'

    def run(self, dispatcher, tracker, domain):
        rfqID = tracker.get_slot("rfqID")
        direction = tracker.get_slot("direction")
        if direction:
            dispatcher.utter_message("Alright, {} on RFQ ID: {}".format(direction, rfqID))
            dispatcher.utter_message("Would you like me to book RFQ ID: {}".format(rfqID))
            return []
        else:
            dispatcher.utter_message("Sorry, I am unable to understand. Can you please try again?")
            return []


class ActionBook(Action):
    def name(self):
        return 'action_book'

    def run(self, dispatcher, tracker, domain):
        direction = tracker.get_slot("direction")
        rfqID = tracker.get_slot("rfqID")
        if direction and rfqID:
            dispatcher.utter_message("Booked RFQ {} on {}".format(direction, rfqID))
            return [SlotSet("direction"), SlotSet("rfqID")]
        else:
            dispatcher.utter_message("Sorry, something went wrong. I am not sure which Direction ({}) and RFQ ({})".format(direction, rfqID))
            return [SlotSet("direction"), SlotSet("rfqID")]


class ActionTest1(Action):
    def name(self):
        return 'action_test1'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Test1")
        dispatcher.utter_message("{}".format(tracker.current_slot_values()))
        return []


class ActionTest2(Action):
    def name(self):
        return 'action_test2'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Test2")
        dispatcher.utter_message("{}".format(tracker.current_slot_values()))
        return []
