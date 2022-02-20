"""
Description:
    Now that you have the structure of your transmission decoded, you can calculate the value of the expression it
    represents.

Literal values (type ID 4) represent a single number as described above. The remaining type IDs are more interesting:

    Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets.
        If they only have a single sub-packet, their value is the value of the sub-packet.
    Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their
        sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
    Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
    Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
    Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater
        than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two
        sub-packets.
    Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than
        the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
    Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the
        value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.


Goal:
    What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?

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
    def __init__(self, version, type_id, sub_packets, literal_value):
        self.version = version
        self.type_id = type_id
        self.sub_packets = sub_packets
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

    # Recursive function to precess the packets (both main and sub-packets)
    def parse_packet():

        # Initialize a list to keep track of the sub-packets found in each packet
        sub_packets = []

        # Read the packet version and packet type id
        packet_version = _read(3)
        packet_type_id = _read(3)

        # Literal packet. It encodes a single binary number
        if int(packet_type_id, 2) == 4:
            chunk_to_decode = _read(5)

            # _parse_packet() start from the first chunk, and if necessary, continues the parsing
            packet_bits = _parse_packet(chunk_to_decode)

            # Get the literal value of the literal packet
            literal_value_packet = int(packet_bits, 2)

            # Return literal packet. No sub-packets possible
            return Packet(int(packet_version, 2), int(packet_type_id, 2), [], literal_value_packet)

        # Operator. It encodes one or mode sub-packets
        else:
            # Read the type of operator packet
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
                    sub_packets.append(packet)

                # Ones extracted and processed all sub-packet, store them.
                #  The literal value is zero because sub-packets found. Only literal packets has literal values
                return Packet(int(packet_version, 2), int(packet_type_id, 2), sub_packets, 0)

            # 11-bit
            else:
                num_sub_packets = _read(11)

                # Each sub-packet has the structure of a packet:
                #  3 bits -> version; 3 bit -> type ID; 5 bits -> First chunk to decode
                for i in range(int(num_sub_packets, 2)):
                    packet = parse_packet()
                    sub_packets.append(packet)

                # Ones extracted and processed all sub-packet, store them.
                #  The literal value is zero because sub-packets found. Only literal packets has literal values
                return Packet(int(packet_version, 2), int(packet_type_id, 2), sub_packets, 0)

    # Recursive function to get the value of the processed packets
    def get_value(p):

        if p.type_id == 4:
            return p.literal_value
        elif p.type_id == 0:
            return sum(get_value(sub_packet) for sub_packet in p.sub_packets)
        elif p.type_id == 1:
            result = 1
            for sub_packet in p.sub_packets:
                result *= get_value(sub_packet)
            return result
        elif p.type_id == 2:
            return min(get_value(sub_packet) for sub_packet in p.sub_packets)
        elif p.type_id == 3:
            return max(get_value(sub_packet) for sub_packet in p.sub_packets)
        elif p.type_id == 5:
            # These packets always have exactly two sub-packets
            return int(get_value(p.sub_packets[0]) > get_value(p.sub_packets[1]))
        elif p.type_id == 6:
            # These packets always have exactly two sub-packets
            return int(get_value(p.sub_packets[0]) < get_value(p.sub_packets[1]))
        elif p.type_id == 7:
            # These packets always have exactly two sub-packets
            return int(get_value(p.sub_packets[0]) == get_value(p.sub_packets[1]))

    # ================ #
    # Print the result #
    # ================ #

    packets = parse_packet()

    result = get_value(packets)
    print("Final result: {}".format(result))
