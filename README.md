# Hanabi AI

Runner for an AI competition based on the card game Hanabi

## Status of Master

[![Build Status](https://travis-ci.com/akaps/hanabi_ai.svg?branch=master)](https://travis-ci.com/akaps/hanabi_ai)

## Getting Started

To run the example simulation
```
sample.sh
```
To get help info for running your own simulations
```
python playgame.py -h
python playgame.py single -h
```

### Tournament Mode

Hanabi has a tournament mode, which runs combinations of all listed players.
To run the example tournament
```
sample_tournament.sh
```
to get help info for setting up your own tournament
```
python playgame.py tournament -h
```

### Variants

Hanabi has 3 variants to increase difficulty, included in the rules sheet. They are:

1 - Adds the multicolor suit as a 6th suit to the game. It is not a wildcard suit

2 - Same as Variant 1, but only 1 card from each rank of the multicolor suit is used

3 - Adds the 6th suit to the game and these cards are wild. In this variant, you cannot call out the mutlicolor suit. Instead, the multicolor cards always count as the color in your clue. When playing the card, it counts and builds as the 6th color

### Prerequisites

Python 2.7

### Installing

A step by step series of examples that tell you how to get a development env running

Install nose and enum34

```
pip install nose
pip install enum34
pip install matplotlib
```

## Running the tests

All tests are written as unit tests and can be run with nose

```
nosetests
```

To run an individual test, provide the filepath
```
nosetests path_to_test.py
```
