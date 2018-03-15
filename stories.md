## Story: greet                     <!-- name of the story - just for debugging -->
* greet
    - utter_greet

## Story: request_price
* price_request{"rfqID": null}
   - action_request_price
   - action_listen
> process_direction

## Story: request_price_again
> process_direction{"rfqID": null}
   - action_listen

## Story: process_direction
> process_direction
* inform_direction{"rfqID": "12345"}
   - action_set_direction
> process_booking

## Story: process_direction_again
> process_booking
* inform_direction{"rfqID": "12345", "direction": null}
   - action_set_direction
> process_booking

## Story: process_booking_affirm
> process_booking
* affirm{"direction": "ClientReceive"}
   - action_book
   - action_restart

## Story: process_booking_deny
> process_booking{"direction": "ClientReceive"}
* deny
   - slot{"direction": null, "rfqID": null}
   - action_restart
