import heapq
import os
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, frequency):
        # Initializes a Huffman Node with character and frequency attributes.
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        # Compares two Huffman Nodes based on their frequencies.
        return self.frequency < other.frequency

def build_frequency_table(text):
    # Builds a frequency table for characters in the input text.

    frequency_table = defaultdict(int)
    for char in text:
        frequency_table[char] += 1
    return frequency_table

def build_huffman_tree(frequency_table):
    # Builds a Huffman tree based on the frequency table.
    priority_queue = []
    for char, frequency in frequency_table.items():
        heapq.heappush(priority_queue, HuffmanNode(char, frequency))

    while len(priority_queue) > 1:
        # Combine two nodes with the lowest frequencies to create a new parent node.
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_huffman_codes(node, prefix="", codes={}):
    # Builds Huffman codes recursively based on the Huffman tree.
    if node:
        if node.char is not None:
            codes[node.char] = prefix
        # Traverse left with '0' prefix and right with '1' prefix.
        build_huffman_codes(node.left, prefix + "0", codes)
        build_huffman_codes(node.right, prefix + "1", codes)
    return codes

def encode_text(text, codes):
    # Encodes text using Huffman codes.

    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text

def pad_encoded_text(encoded_text):
   # Pads encoded text to ensure it is a multiple of 8 bits.
    extra_padding = 8 - len(encoded_text) % 8
    for i in range(extra_padding):
        encoded_text += "0"
    padded_info = "{0:08b}".format(extra_padding)
    return padded_info + encoded_text

def get_byte_array(padded_encoded_text):
    # Converts padded encoded text into a byte array.
    if len(padded_encoded_text) % 8 != 0:
        print("Encoded text not padded properly")
        exit(0)
    b = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
        byte = padded_encoded_text[i:i+8]
        b.append(int(byte, 2))
    return b

def compress(input_file, output_file):
    # Compresses input text file using Huffman coding and writes the compressed data to an output file.
    with open(input_file, 'r') as file:
        text = file.read().rstrip()

    # Build frequency table, Huffman tree, and Huffman codes.
    frequency_table = build_frequency_table(text)
    huffman_tree = build_huffman_tree(frequency_table)
    huffman_codes = build_huffman_codes(huffman_tree)

    # Encode text using Huffman codes and pad the encoded text.
    encoded_text = encode_text(text, huffman_codes)
    padded_encoded_text = pad_encoded_text(encoded_text)

    # Convert padded encoded text into a byte array and write it to the output file.
    byte_array = get_byte_array(padded_encoded_text)
    with open(output_file, 'wb') as file:
        file.write(bytes(byte_array))

    print("Compression successful")

def decompress(input_file, output_file, huffman_codes):
    # Decompresses a file that was compressed using Huffman coding.
    with open(input_file, 'rb') as file:
        bit_string = ""
        byte = file.read(1)
        while len(byte) > 0:
            byte = ord(byte)
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits
            byte = file.read(1)

    padding_info = bit_string[:8]
    extra_padding = int(padding_info, 2)

    bit_string = bit_string[8:]
    encoded_text = bit_string[:-1*extra_padding]

    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in huffman_codes.values():
            # Reverse lookup Huffman codes to find characters.
            for char, code in huffman_codes.items():
                if code == current_code:
                    decoded_text += char
                    current_code = ""
                    break

    with open(output_file, 'w') as file:
        file.write(decoded_text)

    print("Decompression successful")

# Example usage:
input_file = "pg11.txt"
compressed_file = "alice_compressed.bin"
decompressed_file = "alice_decompressed.txt"

frequency_table = build_frequency_table(open(input_file, 'r').read().rstrip())
huffman_tree = build_huffman_tree(frequency_table)
huffman_codes = build_huffman_codes(huffman_tree)

compress(input_file, compressed_file)
decompress(compressed_file, decompressed_file, huffman_codes)



# Print the first few layers of the tree (printing the whole tree is unreadable)
"""
from binarytree import Node

def build_binary_tree(node, depth):
    if depth == 0 or node is None:
        return None
    if node.char is not None:
        return Node("({}: {})".format(node.char, node.frequency), build_binary_tree(node.left, depth - 1), build_binary_tree(node.right, depth - 1))
    else:
        return Node("{}".format(node.frequency), build_binary_tree(node.left, depth - 1), build_binary_tree(node.right, depth - 1))

depth_limit = 5
binary_tree = build_binary_tree(huffman_tree, depth_limit)
print("Simplified Huffman Tree (depth limit={}):".format(depth_limit))
print(binary_tree)
"""