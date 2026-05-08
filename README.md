# BYD EV Pro — Home Assistant Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

Custom Home Assistant integration for [BYD EV Pro](https://github.com/ant0nkr/ev-pro-app) — receive real-time vehicle telemetry from your BYD EV via webhook.

## Features

- **25+ sensors**: battery SOC, voltage, current, power, temperatures, range, odometer, speed, charging state, climate status, and more
- **GPS device tracker**: real-time vehicle location on the HA map
- **Voice actions**: configure HA scripts as voice commands in the BYD EV Pro app
- **HMAC webhook security**: optional signature verification for incoming data
- **Zero polling**: the car pushes data — no cloud API, no scraping

## Installation

### HACS (recommended)

1. Open HACS → Integrations → **Custom repositories**
2. Add `https://github.com/ant0nkr/ev-pro-ha-integration` as an **Integration**
3. Search for "BYD EV Pro" and install
4. Restart Home Assistant

### Manual

Copy the `custom_components/byd_ev_pro` folder into your Home Assistant `config/custom_components/` directory and restart.

## Setup

1. Go to **Settings → Devices & Services → Add Integration**
2. Search for **BYD EV Pro**
3. Enter your vehicle name
4. Copy the generated webhook URL into the BYD EV Pro app (Settings → Home Assistant)

## Configuration

In the integration options you can configure:

- **Long-lived access token** — allows the car to call HA services (voice commands, automations)
- **Webhook secret** — HMAC-SHA256 signing key for verifying incoming webhooks
- **Voice actions** — map HA scripts to voice phrases (Ukrainian / English) that can be triggered from the car

## Sensors

| Sensor | Device Class | Unit |
|--------|-------------|------|
| Battery Level | battery | % |
| Battery Health | — | % |
| HV Battery Voltage | voltage | V |
| HV Battery Current | current | A |
| Battery Power | power | kW |
| 12V Battery | voltage | V |
| Cell Max/Min Voltage | voltage | V |
| Cabin Temperature | temperature | °C |
| Outside Temperature | temperature | °C |
| Battery Max/Min Temp | temperature | °C |
| Motor Temperatures | temperature | °C |
| EV Range | distance | km |
| Odometer | distance | km |
| Speed | speed | km/h |
| Vehicle State | — | OFF/ON/REMOTE ON |
| Charging State | — | Not Charging/Charging/Complete |
| Charging Gun | — | Disconnected/AC/DC |
| Climate | — | Off/On |
| Fan Speed | — | — |
| Steering Wheel Heat | — | Off/On |
| Seat Heat | — | Off/Level 1/Level 2 |
| Front Motor Speed | — | RPM |

## License

MIT
