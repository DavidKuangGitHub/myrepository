"""TrieNodeviapython.py
Author: David Kuang Last updated: Sep 3rd 2020
Description: Non-case-sensitive will be implemented if there is a requirement
"""
from typing import Tuple

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1

def add(root, word: str):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True

def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    node = root
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False, 0
    return True, node.counter

if __name__ == "__main__":
    """root = TrieNode('*')"""
    root = TrieNode('$')
    add(root, "DavidKuang")
    add(root, 'Davi')
    add(root, "Ford Motor Company")

    #print("Root Verification should be ", find_prefix(root,'$'))
    print(find_prefix(root, 'Dav'))
    print(find_prefix(root, 'Davi'))
    print(find_prefix(root, 'DavidKuang'))
    print(find_prefix(root, 'Da'))
    print(find_prefix(root, 'Dave'))
    """print(find_prefix(root, 'ford m'))"""
    print(find_prefix(root, 'Ford Mot'))
