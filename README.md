<h1 align="center">Repeat-free Codes - Final Project</h1>

# Project Goals

The main goal of this tool is to eliminate identical windows in a given sequence. The input is a length-n q-ary vector
and the output is a length-(n+1) q-ary vector which has no identical windows, when windows size is <img src="https://render.githubusercontent.com/render/math?math={2\log_qn%2B1}">.


The algorithm is based on Algorithm 1 from the article "[Repeat-Free Codes](/article.pdf)" by E. Yaakobi, O. Elishco, R. Gabrys and M. Medard.

## Getting Started

The project was developed in Python.

### Prerequisites

```
Python 3.6 or higher
```
## Usage

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

### Examples

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

### Running Tests
Random test generation is supplied at [test.py](test.py) and requires the Python `numpy` package.

## Encoder
*File: encoder.py*

### Parameters
The encoder accepts four parameters.

1. **alg_type** (either *"time"* or *"space"*): Whether to save time or space.

2. **redundancy** (either *1* or *2*): Whether to use one or two redundancy bits.

3. **verbose_mode** (bool): If set, the resulting word of every step is printed to the standard output.

4. **q** (int): Alphabet size. Alphabet is assumed to be *{0, 1, ..., q - 1}*. Default is 2.

### Algorithm
The algorithm includes two degrees of freedom determined by the *redundancy* and the *alg_type*.

The following description of the algorithm assumes **redundancy = 1**. The other case is described afterward. 

**Input:** *w* of length *n - redundancy*.

**Output:** *E(w)* of length *n*, *k*-repeat-free and *(0, zero_rll)*-run-length-limited, where *zero_rll = log_q(n) + 2*. Note that the latter property is not part of the requirements for the encoder, but is needed to allow decoding.

1. Append *1 &bull; 0^zero_rll* to the end of *w*. Call this appended series of characters the **marker**.

2. **Elimination:** Iteratively handle identical windows and long runs of zeros, until the condition of the output is achieved. The behavior of the algorithm is described in the [article](article.pdf), and so we will not go into further details.

3. **Expansion:** As long as the word length is less than *n*, append to *w* new chunks, each of length log_q(n), such that the output condition remains satisfied.

The first *n* characters of the resulting word are then returned as the codeword *c = E(w)*.

**Notes:**

* While working on the algorithm, another approach emerged which uses two redundancy bits. The only change is this: Prepend a zero to the beginning of *w* and set *zero_rll = log_q(n) + 1*, then run the algorithm identically on the resulting word. Upon decoding, the redundant zero at the beginning is dropped once the main decoder algorithm is done, and *w* is retrieved.

* See the [article](article.pdf) for the algorithm correctness proof and analysis.

### Complexity

Upon each identical window detection, a *k*-long window is deleted from the word and *(k - 1)* new characters are prepended. Therefore, there are *O(k) = O(log_q(n))* newly added windows. Since after each iteration the word length decreases by *1*, there are *O(n)* possible iterations with *O(log_q(n))* possible new windows each time. All in all, there are *O(n &bull; log_q(n))* possibly distinct handled windows throughout the algorithm.

Upon the addition of the new windows, we have to either compare only them to all other windows by hashing the already visited windows in the current iteration (taking *O(log_q(n))* time and *O(n &bull; log_q(n))* space) when *(alg_type == "space")*, or compare again all pairs of windows (taking *O(n)* time and *O(log_q(n))* space) when *(alg_type == "space")*.
**Empirically, the former implementation way outperforms the latter, both in time and space consumption.**

Since each window is possibly compared with all others, there are O(n) comparisons, each taking O(log_q(n)) time and space complexity.

Time complexity can be summarized in the following: 

* *(n &bull; log_q(n))* **iterations**
* *n* OR *log_q(n)* **new windows** need to be compared per iteration
* *n* **comparisons** for each window
* *log_q(n)* **operations** for each comparison

**Total:** *n^3 &bull; log^2_q(n)* (saving space) OR *n^2 &bull; log^3_q(n)* (saving time).


## Decoder
*File: decoder.py*

### Parameters
The decoder accepts three parameters.

1. **redundancy** (either *1* or *2*): Whether the encoder used one or two redundancy bits.

2. **verbose_mode** (bool): If set, the resulting word of every step is printed to the standard output.

3. **q** (int): Alphabet size. Alphabet is assumed to be *{0, 1, ..., q - 1}*. Default is 2.


### Algorithm

**Input:** *w* of length *n*, output of the supplied encoder.

**Output:** *D(w)* of length *(n - 1)*.

* (1) Search for a *zero_rll*-long run of zeros - the aforementioned **marker**.
    * (1.1) If found: *w = w' &bull; 1 &bull; 0^(log_n + 1) &bull; w''*.
    * (1.2) Otherwise: *w = w' &bull; 1 &bull; 0^t, where (0 <= t <= log_n)*.
    * (**Note**: Recall that *(1 &bull; 0^zero_rll* was appended. These zeros are never victims of phase 2.)
* (2) Update: *w <- w' * 1 * 0^(log_n + 1)*
* (3) Do until *len(w) == (n + log_n + 1)*:
    * (3.1) If *w[0] == 0*, **undo case 1** on *w*.
    * (3.2) Otherwise, **undo case 2** on *w*.
* (4) Return *w[:(n - 1)]*.

#### Data Structures and Complexity
* (1) One way would be to convert the input into a dictionary, so that random-access is *O(log_q(n))*.
    * **Time complexity:** O(ITERATIONS * UPDATE TIME/ITERATION) = O((n * log_q(n)) * (log_q(n) * log_q(n))) = O(n * log^3_q(n))
    * **Space complexity:** O(n)
* (2) Another way, maintaining *O(log_q(n)) space complexity, is to insert with *O(n)* time complexity.
    * **Time complexity:** O(ITERATIONS * UPDATE TIME/ITERATION) = O((n * log_q(n)) * (n * log_q(n))) = O(n^2 * log^2_q(n))
    * **Space complexity:** O(log_n)

Our decoder implements option 2.

## Better time complexity?
The lower-bound for time complexity is *O(n &bull; log^2_q(n))*: We must go over *O(n &bulls; log_q(n))* distinct windows and compare each one at least once in *O(loq_q(n))*.

Is it achievable? We think so. However, considering the amount of data structures we tried to put together and the substantial time we put into stubbornly trying to achieve it, we are led to believe that such a complicated structure would have little practical advantages. Our endeavors still exist in the [rip](rip/) directory, waiting for those bold enough to wander there.

## Profiler

See README.md under profiler.

## Authors

* [**Antonio Abu Nassar**](https://github.com/antonioan)
* [**Rotem Samuel**](https://github.com/rotemsamuel)

## Mentor

* [Professor **Eitan Yaakobi**](http://www.cs.technion.ac.il/people/yaakobi/)

## Contributing
Pull requests are welcome. For major changes, please open an *issue* for discussion first.

Make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

