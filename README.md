<h1 align="center">Final Project - Repeat-free Codes</h1>

# Project Goals

The main goal of this tool is to eliminate identical windows in a given sequence. The input is a length-n q-ary vector
and the output is a length-(n+1) q-ary vector which has no identical windows, when windows size is <img src="https://render.githubusercontent.com/render/math?math=2\cdot{i \pi} = -1">.

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
* **-i** - when flag is on input will be supplied via the standard input.
* **-r** - choose the number of redundancy bits (can be 1 or 2). default is 1 redundancy bit.
* **-c** - toggle between 2 implementations options. "time" is for better time complexity (but consumes more space) and "space" is for a better space complexity (but less efficient in time).
* **-v** - when flag is on output verbosity increased and a detailed log is printed.
* **-t** - test mode, make sure that encoded word has no identical windows\ decoded word encoding is equeal to the input word.
* **-q** - determine the size of the alphabet. default is 2 (binary). notice that when q > 2 sequence charecters should be delimited by ','.

```
./main.py encode 000000000000000001111111111000000000
output:          1011000100000110010001111111111010000
```
```
./main.py decode 1011000100000110010001111111111010000
output:          000000000000000001111111111000000000
```
```
./main.py decode 1011000100000110010001111111111010000 -v
n      = 37
q      = 2
log_n  = 6
k      = 14
w      = [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
w-0    = [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
w-2    = [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
w-2    = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
w-2    = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
w-1    = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
dec*   = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
output = 000000000000000001111111111000000000
```
```
./main.py decode 1010 -v
n      = 4
q      = 2
log_n  = 2
k      = 6
w      = [1, 0, 1, 0]
w-0    = [1, 0, 1, 0, 0, 0, 0]
w-2    = [0, 0, 0, 0, 0, 0, 0, 0]
dec*   = [0, 0, 0]
output = 000
```
```
./main.py encode 000 -t
0001
TEST SUCCESS
```
```
./main.py encode 0,1,2,3 -q5
0,1,2,3,1
```

```
./main.py encode 0,1,2,3 -q5 -c time -r2
0,0,1,2,3,1
```

## Authors

* **Antonio** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)


