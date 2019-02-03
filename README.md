# Raspberry Pi Signal and Departure Board for Model Lego Train

Simple single signal and LCD departure board screen using a Raspberry Pi - ideally suited for Lego railways or other similar model railway layouts. Created for my 5-year-old son to use. There is a single set of signal lights, buttons which can be used to change the signals, and an LCD screen acting as a departure board showing random-selected destinations and a countdown timer for each. My son is mad about trains and lego, so he loves it, and we're using the station names on the departure board to help him practice his reading.

There's a lot of potential to improve this, among my thoughts are:
* support multiple signals
* add logic between the signals - for instance ensuring only one can show a green light at any time
* connect the buttons and signals via a GPIO expander (e.g. [PCF8574](https://www.amazon.co.uk/dp/B07CNYF9FX/ref=cm_sw_em_r_mt_dp_U_u1wsCbKMFYN6P)) so multiple sets can be positioned around a train layout daisy-chained with 4 core cable to the I2C bus
* add a speaker (connected to via an ADC and amp such as [MAX98357A]( https://shop.pimoroni.com/products/adafruit-i2s-3w-class-d-amplifier-breakout-max98357a) to the Pi's I2S output) for station announcements and other sounds


## Getting Started

The parts list below can be used to make the components as pictured, you can ofcourse wire up the buttons and lights differently and/or not use a breadboard and cobbler if you prefer:

### Parts required

* [Any Raspberry Pi model with a 40-pin GPIO connector](https://shop.pimoroni.com/collections/raspberry-pi?view=featured)
* [PiStop traffic light](https://shop.pimoroni.com/products/pistop-traffic-light-add-on-for-raspberry-pi)
* [20x4 character LCD screen with a PCF8574 I2C backpack](https://www.amazon.co.uk/dp/B00LSG5EVU/ref=cm_sw_em_r_mt_dp_U_aGxrCbJ8JP23R)
* [2x Small piece of stripboard](https://www.amazon.co.uk/dp/B00KM1EG0M/ref=cm_sw_em_r_mt_dp_U_WLxrCbAPNEH57)
* [3x PCB buttons](https://www.amazon.co.uk/dp/B06XT5X7LH/ref=cm_sw_em_r_mt_dp_U_mNxrCbD0ESZDD)
* [A selection of F->F jumper wires](https://www.amazon.co.uk/dp/B00OL6JZ3C/ref=cm_sw_em_r_mt_dp_U_nTDtCb7MXJ9RH)
* [Dupont Male PCB headers 2x 4pin single row, 1x 9pin single row](https://www.amazon.co.uk/dp/B06XR8CV8P/ref=cm_sw_em_r_mt_dp_U_Q5wsCbPJ7MDAM)

### Wiring diagram

* Connect the LCD screen as follows:
    * SDA to GPIO pin 3
    * SCL to GPIO pin 5
    * GND to any GND GPIO pin (pin 6 is nearby)
    * VDD to a 5V supply on GPIO pin 2 or pin 4
* Connect the buttons as follows
    * Red button to GPIO pin 35 (this is BCM19, and is re-configurable in the code)
    * Amber button to GPIO pin 38 (this is BCM20, and is re-configurable in the code)
    * Green button to GPIO pin 40 (this is BCM21, and is re-configurable in the code)
    * Connect the other side of the buttons to GND, so the button pulls its respective GPIO line low when pressed 
* Connect the signal lights as follows:
    * Red light to GPIO pin 26 (this is BCM7, and is re-configurable in the code)
    * Amber light to GPIO pin 24 (this is BCM8, and is re-configurable in the code)
    * Green light to GPIO pin 22 (this is BCM25, and is re-configurable in the code)
    * GND to GND (GPIO pin 20 is nearby) 

### Installing

Install Raspbian on to a memory stick, boot your Pi and log in as the "pi" user (see here for instructions).

Install git:

```
sudo apt-get install git -y
```

Clone the github repo in to a new directory on your Pi:

```
git clone https://github.com/djdunford/PiLegoTrainStation
```

Install the software on to your Pi - this will copy the code in to /opt, and set up a service called "signals" which you can start / stop. By default the service will start automatically on boot, however you can change this with systemctl.

## Versions

For the versions available, see the [tags on this repository](https://github.com/djdunford/PiLegoTrainStation/tags). 

## Authors

* **Darren Dunford** - *Initial work* - [djdroyston](https://github.com/djdroyston)
