# Algorithm: Greedy — Min-Heap (Priority Queue)
# Time Complexity:  O(n log n) — each heappush/heappop is O(log n)
# Space Complexity: O(n)       — heap and code table

import heapq
from collections import Counter


class HuffmanNode:
    """Node in the Huffman tree."""
    def __init__(self, char, freq):
        self.char  = char
        self.freq  = freq
        self.left  = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text: str) -> HuffmanNode:
    """
    Build a Huffman tree from the frequency of characters in text.
    Characters with lower frequency get longer codes.
    """
    freq = Counter(text)
    heap = [HuffmanNode(char, f) for char, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left  = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left  = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0] if heap else None


def generate_codes(node: HuffmanNode, prefix: str = "", codes: dict = None) -> dict:
    """
    Walk the Huffman tree and assign binary codes.
    Left edge = '0', Right edge = '1'.
    """
    if codes is None:
        codes = {}
    if node:
        if node.char is not None:
            codes[node.char] = prefix or '0'
        generate_codes(node.left,  prefix + '0', codes)
        generate_codes(node.right, prefix + '1', codes)
    return codes


def huffman_encode(text: str) -> tuple[str, dict]:
    """
    Encode text using Huffman coding.
    Returns (encoded_bits, code_table).
    """
    if not text:
        return "", {}
    root   = build_huffman_tree(text)
    codes  = generate_codes(root)
    encoded = ''.join(codes[ch] for ch in text)
    return encoded, codes


def huffman_decode(encoded: str, root: HuffmanNode) -> str:
    """
    Decode a Huffman-encoded bit string using the original tree.
    """
    if not encoded or not root:
        return ""
    result  = []
    current = root
    for bit in encoded:
        current = current.left if bit == '0' else current.right
        if current.char is not None:
            result.append(current.char)
            current = root
    return ''.join(result)


if __name__ == "__main__":
    text    = "huffman coding is a greedy algorithm"
    encoded, codes = huffman_encode(text)

    print("Original bits:", len(text) * 8)
    print("Encoded bits: ", len(encoded))
    print("Compression:  ", f"{(1 - len(encoded)/(len(text)*8))*100:.1f}%")
    print("\nCode table:")
    for ch, code in sorted(codes.items(), key=lambda x: len(x[1])):
        print(f"  '{ch}': {code}")

    root    = build_huffman_tree(text)
    decoded = huffman_decode(encoded, root)
    print("\nDecoded matches original:", decoded == text)
