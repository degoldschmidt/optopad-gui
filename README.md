# optopad-gui
[![GitHub release](https://img.shields.io/badge/Release-0.9.3--beta-blue.svg?maxAge=2592000)]()

Python-/TKinter-based GUI for creating optogenetic stimulation protocols for the OptoPad setup 

<div style="text-align:center">
<img src="./screenshots/demo.png" width="400">
</div>

## Changelog

v0.9.3-beta:
* Duty cycle/constant on-cycle option now work
* **New function:** Load protocol button  

v0.9.2-beta:
* **New function:** Dynamic protocols
* Duty cycle added
* Constant on-cycle added

v0.9.1-beta:
* **New function:** Copy button for transferring data from one channel to another

v0.9-beta:
* **First working version**

## Installation

## Quickstart

## Useful information

### Column indices in data matrix
| Index         | Description   |
| ------------: |:-------------:|
| 0             | Color CH1 (int) |
| 1             | Color CH2 (int) |
| 2             | Delay CH1 (float) |
| 3             | Delay CH2 (float) |
| 4             | Sustain CH1 (float) |
| 5             | Sustain CH2 (float) |
| 6             | Probability CH1 (float) |
| 7             | Probability CH2 (float) |
| 8             | Stop condition (int) |
| 9             | Stop condition (int) |
| 10            | Frequency CH1 (int) |
| 11            | Frequency CH2 (int) |
| 12            | Duty cycle CH1 (float) |
| 13            | Duty cycle CH2 (float) |
