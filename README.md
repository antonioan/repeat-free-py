<h1 align="center">Repeat-free Codes - Final Project</h1>

# Project Goals

The main goal of this tool is to eliminate identical windows in a given sequence. The input is a length-n q-ary vector
and the output is a length-(n+1) q-ary vector which has no identical windows, when windows size is <img src="https://render.githubusercontent.com/render/math?math=2\cdot{\log_qn%2B2}"> .

$ \2\cdot{\log_qn}{+{2}} $

The algorithm is based on Algorithm 1 from the article "[Repeat-Free Codes](/article.pdf)" by E. Yaakobi, O. Elishco, R. Gabrys and M. Medard.

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

## Encoder
*File: encoder.py*

### Parameters
The encoder accepts four parameters.

1. **alg_type** (either *"time"* or *"space"*): Whether to save time or space.

2. **redundancy** (either *1* or *2*): Whether to use one or two redundancy bits.

3. **verbose_mode** (bool): If set, the resulting word of every step is printed to the standard output.

4. **q** (int): Alphabet size. Alphabet is assumed to be *{0, 1, ..., q - 1}*. Default is 2.

### Algorithm
The algorithm includes two degrees of freedom, which are determined by the *redundancy* and the *alg_type*.

Algorithm structure and complexity analysis will soon be added to this document.

<!--
n * log_n       iterations\
n   OR?  log_n  new windows need to be compared per iteration\
n               comparisons for each window\
log_n           operations for each comparison
-->

## Decoder
*File: decoder.py*

### Parameters

TBA

### Algorithm

Sketch for the algorithm. Will be tweaked soon.

Input: *w* of length *n*.\
Output: *D(w)* of length *(n - 1)*.

(1) Search for a *(log_n + 1)*-long run of zeros.\
&nbsp;&nbsp;&nbsp;&nbsp;(1.1) If found: w = w' * 1 * 0^(log_n + 1) * w''.\
&nbsp;&nbsp;&nbsp;&nbsp;(1.2) Otherwise: w = w' * 1 * 0^t, where (0 <= t <= log_n).\
&nbsp;&nbsp;&nbsp;&nbsp;(Proof for both: Recall that (1 * 0^(log_n + 1)) was appended. These zeros are never victims of phase 2.)\
(2) Update: w <- w' * 1 * 0^(log_n + 1)\
(3) Do until len(w) == (n + log_n + 1):\
&nbsp;&nbsp;&nbsp;&nbsp;(3.1) If w[0] == 0, undo phase 1 on w.\
&nbsp;&nbsp;&nbsp;&nbsp;(3.2) Otherwise, undo phase 2 on w.\
(4) Return w[:(n - 1)]

#### Data Structures and Complexity
(1) One way is to convert the input into a dictionary, so that random-access is O(log_n).\
&nbsp;&nbsp;&nbsp;&nbsp;**Time complexity:** O(ITERATIONS * UPDATE TIME PER ITERATION) = O((n * log_n) * (log_n * log_n)) = O(n * log^3_n)\
&nbsp;&nbsp;&nbsp;&nbsp;**Space complexity:** O(n)\
(2) Another way, maintaining O(log_n) space complexity, is to insert with O(n) time complexity.\
&nbsp;&nbsp;&nbsp;&nbsp;**Time complexity:** O(ITERATIONS * UPDATE TIME PER ITERATION) = O((n * log_n) * (n * log_n)) = O(n^2 * log^2_n)\
&nbsp;&nbsp;&nbsp;&nbsp;**Space complexity:** O(log_n)

Our decoder implements option 2.

## Profiler

See README.md under profiler.

<!--Maybe add an "Anecdotes"-like section, then move the commented-out anecdote from `main.py` to here.-->

## Authors

* [**Antonio Abu Nassar**](https://github.com/antonioan)
* [**Rotem Samuel**](https://github.com/rotemsamuel)

## Mentor

* [Professor **Eitan Yaakobi**](http://www.cs.technion.ac.il/people/yaakobi/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


