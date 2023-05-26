# Beautiful-Machine-Code

Beautiful-Machine-Code converts a binary file (`binary_to_btf.txt`) into a formatted BTF (Binary Test Format) string. The binary file should contain a series of binary numbers separated by newlines.

## Usage

1. Place the binary file (`binary_to_btf.txt`) in the same directory as the script.
2. Run the script.
3. The formatted BTF string will be printed to the console.

## Input

The input binary file (`binary_to_btf.txt`) should contain a set of binary numbers, each represented as a 32-bit string, separated by newlines. For example:
```
00000000001100000000010110010011
00000000001100000000011000010011
00000001000000000000000011101111
00000010101101100000100100110011
00000010101101100000100110110011
00000010101101100000101000110011
00000000101101100000010010110011
00000000001100000000010110010011
00000000001100000000011000010011
00000001000000000000000011101111
00000010101101100000100100110011
00000010101101100000100110110011
00000010101101100000101000110011
00000000101101100000010010110011
```
## Output

The code processes the binary file and converts it into a formatted BTF string. Each binary number in the file is assigned an index, starting from 0, and the BTF string is generated as follows:

```
(
  0 =>     "00000000001100000000010110010011",
  1 =>     "00000000001100000000011000010011",
  2 =>     "00000001000000000000000011101111",
  3 =>     "00000010101101100000100100110011",
  4 =>     "00000010101101100000100110110011",
  5 =>     "00000010101101100000101000110011",
  6 =>     "00000000101101100000010010110011",
  7 =>     "00000000001100000000010110010011",
  8 =>     "00000000001100000000011000010011",
  9 =>     "00000001000000000000000011101111",
  10 =>     "00000010101101100000100100110011",
  11 =>     "00000010101101100000100110110011",
  12 =>     "00000010101101100000101000110011",
  13 =>     "00000000101101100000010010110011",
  others =>     X"00000000");
```
  
Each row represents an index-value pair, where the index corresponds, e.g., to the position of the instruction in VHDL instruction memory. In turn, the value stored in instruction memory is the binary code corresponding to the instructions to be executed.
