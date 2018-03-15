## Story: greet                     <!-- name of the story - just for debugging -->
* greet
    - utter_greet

## Story: request_price_no_params
* price_request
    - action_request_price
    - action_listen

## Story: request_price_one_param
* price_request{"quantity": "1mio"}
    - slot{"quantity": "1mio"}
    - action_request_price
    - action_listen
* price_request{"tenor": "2y"}
    - slot{"tenor": "2y"}
    - action_request_price
    - action_listen
* price_request{"currency": "USD"}
    - slot{"currency": "USD"}
    - action_request_price
    - action_listen
* price_request{"product": "SB/3"}
    - slot{"product": "SB/3"}
    - action_request_price
    - action_listen
* price_request{"client": "BlackRock"}
    - slot{"client": "BlackRock"}
    - action_request_price
    - slot{"quantity": null, "tenor": null, "currency": null, "product": null, "client": null}
    - slot{"rfqID": "12345"}
> process_direction

## Story: request_price_two_params
* price_request{"tenor": "2y", "product": "SB/3"}
    - slot{"tenor": "2y", "product": "SB/3"}
    - action_request_price
    - action_listen
* price_request{"quantity": "5mio", "currency": "USD"}
    - slot{"quantity": "5mio", "currency": "USD"}
    - action_request_price
    - action_listen
* price_request{"client": "BlackRock"}
    - slot{"client": "BlackRock"}
    - action_request_price
    - slot{"quantity": null, "tenor": null, "currency": null, "product": null, "client": null}
    - slot{"rfqID": "12345"}
> process_direction

## Story: request_price_three_params
* price_request{"quantity": "5mio", "tenor": "2y", "product": "SB/3"}
    - slot{"quantity": "5mio", "tenor": "2y", "product": "SB/3"}
    - action_request_price
    - action_listen
* price_request{"currency": "USD", "client": "BlackRock"}
    - slot{"currency": "USD", "client": "BlackRock"}
    - action_request_price
    - slot{"quantity": null, "tenor": null, "currency": null, "product": null, "client": null}
    - slot{"rfqID": "12345"}
> process_direction

## Story: request_price_full_params
* price_request{"quantity": "5mio", "tenor": "2y", "currency": "USD", "product": "SB/3", "client": "BlackRock"}
    - slot{"quantity": "5mio", "tenor": "2y", "currency": "USD", "product": "SB/3", "client": "BlackRock"}
    - action_request_price
    - slot{"quantity": null, "tenor": null, "currency": null, "product": null, "client": null}
    - slot{"rfqID": "12345"}
> process_direction

## Story: request_price_again
> process_direction{"rfqID": null} <!-- Something went wrong here and we should restart -->
    - action_listen

## Story: process_direction
> process_direction{"rfqID": "12345"}
* inform_direction{"direction": "ClientReceive"}
    - slot{"direction": "ClientReceive"}
    - action_set_direction
    - slot{"direction": "ClientReceive"}
> process_booking

## Story: process_direction_if_unable_to_understand
> process_direction{"rfqID": "12345"}
* inform_direction{"direction": null}
   - action_set_direction
   - action_listen
* inform_direction{"direction": "ClientPay"}
   - slot{"direction": "ClientPay"}
   - action_set_direction
> process_booking

## Story: process_direction_again
> process_booking{"direction": null} <!-- something is wrong here and we should restart -->
    - action_listen

## Story: process_booking_affirm
> process_booking{"direction": "ClientReceive"}
* affirm
   - action_book
   - slot{"direction": null, "rfqID": null}
   - action_restart

## Story: process_booking_deny
> process_booking{"direction": "ClientReceive"}
* deny
   - slot{"direction": null, "rfqID": null}
   - action_restart
