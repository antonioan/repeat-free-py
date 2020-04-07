<h1 align="center">236608 - Coding and Algorithms for Memories - Final Project</h1>

# Repeat-free Codes

The main goal of this tool is to eliminate identical windows in a given sequence. The input is a length-n q-ary vector
and the output is a length-(n+1) q-ary vector which has no identical windows, when windows size is 2 * log_q(n) +2.

## Getting Started

The project was developed in Python.

### Prerequisites

```
Python 3.6 or higher
```
## Running the tests

The tool can be operated using the command line as follows:
```
usage: ./main [-h] [-i] [-r {1,2}] [-q Q] [-c {time,space}] [-v] [-t] action [sequence]
```

### Positional Parameters

action and sequence are must parameters where action is either "encode" or "decode" and sequence is a q-ary word.

```
./main encode 101010
./main decode 0,1,0,1
```

### Optional Flags

There are some optional flags which can affect how the tool works
* **-h** - show help message.
* **-i** - when flag is on input will be supplied via the standard input .

```
Give an example
```



