"""
Description:
    Method of packing numeric expressions into a binary sequence. Your submarine's computer has saved the transmission
    in hexadecimal (your puzzle input).

    The first step of decoding the message is to convert the hexadecimal representation into binary. Each character of
    hexadecimal corresponds to four bits of binary data:

        0 = 0000
        1 = 0001
        2 = 0010
        3 = 0011
        4 = 0100
        5 = 0101
        6 = 0110
        7 = 0111
        8 = 1000
        9 = 1001
        A = 1010
        B = 1011
        C = 1100
        D = 1101
        E = 1110
        F = 1111

    The hexadecimal representation of this packet might encode a few extra 0 bits at the end; these are not part of the
    transmission and should be ignored.

    Every packet begins with a standard header: the first three bits encode the packet version, and the next three bits
    encode the packet type ID. These two values are numbers; all numbers encoded in any packet are represented as
    binary with the most significant bit first. For example, a version encoded as the binary sequence 100 represents
    the number 4.

    Packets with type ID 4 represent a literal value. Literal value packets encode a single binary number. To do this,
    the binary number is padded with leading zeroes until its length is a multiple of four bits, and then it is broken
    into groups of four bits. Each group is prefixed by a 1 bit except the last group, which is prefixed by a 0 bit.
    These groups of five bits immediately follow the packet header. For example, the hexadecimal string D2FE28 becomes:

        110100101111111000101000
        VVVTTTAAAAABBBBBCCCCC

    Every other type of packet (any packet with a type ID other than 4) represent an operator that performs some
    calculation on one or more sub-packets contained within.

Goal:
    Decode the structure of your hexadecimal-encoded BITS transmission; what do you get if you add up the version
    numbers in all packets?

"""

import numpy as np
import pandas as pd


# ========= #
# Functions #
# ========= #


def open_file(path: str):
    
    file = open(path)
    
    return file


def read_file_as_data_frame(path: str):
    
    inputs = pd.read_csv(path, sep="\n", skiprows=-1, dtype=str)
        
    return inputs
  

# =================== #
# Read the input data #
# =================== #

# Open the file conventionally,
file = open_file('./input.txt')
#  read the entire file,
# inputs = file.read()
#  read the next line.
# line = file.readline()

# Read the entire file as a DataFrame
# inputs = read_file_as_data_frame("./input.txt")


# ======= #
# Helpers #
# ======= #

DECODING = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


class Packet:
    def __init__(self, version, type_id, literal_value):
        self.version = version
        self.type_id = type_id
        self.literal_value = literal_value


def _read(n: int) -> str:

    # To change the value of a global variable inside a function, refer to the variable by using the global keyword
    global idx
    global transmission_binary

    # Get the requestes group
    group = transmission_binary[idx:(idx + n)]
    # Update the index to start the reading
    idx = idx + n

    return group


def _get_if_available_next_chunk_and_bits_current_chunk(bits_to_parse: str):

    # Initialize the storage of the bits
    bits = ""

    next_chunk_available = int(bits_to_parse[0])
    bits = bits_to_parse[1:]

    return next_chunk_available, bits


def _parse_packet(chunk_to_parse: str) -> str:

    # Initialize the storage of the bits
    bits_packet = ""

    next_chunk_available, bits = _get_if_available_next_chunk_and_bits_current_chunk(chunk_to_parse)
    bits_packet += bits

    while next_chunk_available:  # Last group if it starts wit zero
        next_chunk = _read(5)
        next_chunk_available, bits = _get_if_available_next_chunk_and_bits_current_chunk(next_chunk)
        bits_packet += bits

    return bits_packet


# ==== #
# Main #
# ==== #

# Initialize the reading index
idx = 0
# Initialize the decoded transmission on binary
transmission_binary = ""
# Initialize a list to store all the version
versions = []


if __name__ == '__main__':

    # ========= #
    # Read data #
    # ========= #

    transmission_hexadecimal = []

    line = file.readline()
    while line != '\n':
        for ch in line.strip():
            transmission_hexadecimal.append(ch)
        line = file.readline()

    # Close the file
    file.close()

    # =========================================== #
    # Decode sequence. From hexadecimal to binary #
    # =========================================== #

    for hexadecimal in transmission_hexadecimal:
        transmission_binary += DECODING[hexadecimal]

    len_binary = len(transmission_binary)

    # ======================================= #
    # Process the binary decoded transmission #
    # ======================================= #

    def parse_packet():
        global versions

        # Read the packet version and packet type id
        packet_version = _read(3)
        packet_type_id = _read(3)

        # # Store the version. Most outer packet
        versions.append(int(packet_version, 2))

        # Literal packet. It encodes a single binary number
        if int(packet_type_id, 2) == 4:
            chunk_to_decode = _read(5)

            # _parse_packet() start from the first chunk, and if necessary, continues the parsing
            packet_bits = _parse_packet(chunk_to_decode)

            literal_value_packet = int(packet_bits, 2)

            return Packet(int(packet_version, 2), int(packet_type_id, 2), literal_value_packet)

        # Operator. It encodes one or mode sub-packets
        else:
            length_type_id = _read(1)

            # 15-bit
            if length_type_id == "0":
                total_length_in_bits = _read(15)

                # Read sub-packets until reached total_length_in_bits
                i = idx + int(total_length_in_bits, 2)

                # Each sub-packet has the structure of a packet:
                #  3 bits -> version; 3 bit -> type ID; 5 bits -> First chunk to decode
                while idx < i:
                    packet = parse_packet()

            # 11-bit
            else:
                num_sub_packets = _read(11)

                # Each sub-packet has the structure of a packet:
                #  3 bits -> version; 3 bit -> type ID; 5 bits -> First chunk to decode
                for i in range(int(num_sub_packets, 2)):
                    packet = parse_packet()

    # ================ #
    # Print the result #
    # ================ #

    aux = parse_packet()
    print("Result: {}".format(np.sum(versions)))




    


