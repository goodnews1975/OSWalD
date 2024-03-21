# OSWaLD

**O**FF-**S**witch **W**ith **L**ED and **D**isplay

## Definition
The purpose of this device shall be an **OFF-Switch**, which is located at the exit of an automated building.

When I leave the building, I push the **OFF-Button**.

**OSWaLD** sends this request to the Automation Unit of the building. The Automation Unit checks if there is any window open.

If this check is ok, an **green LED** near the Off-Switch indicates all is ok.

If this check fails, an **red LED** blinks, also there is a **display** which shows a message like "Please close the window in the main entrance"

The Logic will be implemented in the **Home Automation Unit**. OSWaLD will connect over built-in WIFI
Communication over MQTT. 

## Contents of OSWaLD
- Microcontroller
  - Raspberry Pi Pico WH
    - with WLAN
- Push-Button
- green LED
- red LED
- Display for Messages 


