from utils import *
import math
from node import Node
from merkle_tree import *



'''
def merkle_proof(tx, merkle_tree):
    """Given a tx and a Merkle tree object, retrieve its list of tx's and
    parse through it to arrive at the minimum amount of information required
    to arrive at the correct block header. This does not include the tx
    itself.

    Return this data as a list; remember that order matters!
    """
    #### YOUR CODE HERE
'''
def gethash(tx_list):
    if len(tx_list) == 1:
        return tx_list[0]
    merk =  MerkleTree(tx_list)
    return merk.block_header

def merkle_proof(tx, merkle_tree):
    """Given a tx and a Merkle tree object, retrieve its list of tx's and
    parse through it to arrive at the minimum amount of information required
    to arrive at the correct block header. This does not include the tx
    itself.

    Return this data as a list; remember that order matters!
    """
    "*** YOUR CODE HERE ***"
    tx_list = merkle_tree.leaves

    if len(tx_list) == 1:
        return []

    if not is_power_of_two(len(tx_list)) or len(tx_list) < 2:
        last_tx = tx_list[-1]
        while not is_power_of_two(len(tx_list)) or len(tx_list) < 2:
            tx_list.append(last_tx)

    lst = []
    target = tx_list.index(tx)

    if target in range(0, int(len(tx_list)/2)):
        lst.append(gethash(tx_list[int(len(tx_list)/2):]))
        lst.extend(merkle_proof(tx, MerkleTree(tx_list[:int(len(tx_list)/2)])))
    if target in range(int(len(tx_list)/2), len(tx_list)):
        lst.append(gethash(tx_list[:int(len(tx_list)/2)]))
        lst.extend(merkle_proof(tx, MerkleTree(tx_list[int(len(tx_list)/2):])))

    return lst




def get_max_depth_node(nodes):
    """Helper function to retrieve the node with the maximum depth.
    Helpful for pairing nodes for hashing in verify_proof"""
    curr = nodes[0]
    for i in range(0, len(nodes)):
        if nodes[i].depth > curr.depth:
            curr = nodes[i]
    return curr


def verify_proof(tx, merkle_proof):
    """Given a Merkle proof - constructed via `merkle_proof(...)` - verify
    that the correct block header can be retrieved by properly hashing the tx
    along with every other piece of data in the proof in the correct order
    """
    #### YOUR CODE HERE
    curr = tx
    for i in range(len(merkle_proof)):
        curr = hash_data(curr+merkle_proof[len(merkle_proof)-1 - i], 'sha256')
    return curr

    
