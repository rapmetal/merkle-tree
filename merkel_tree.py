# coding: utf-8

import hashlib


class MerkelTree(object):
    '''
        In cryptography and computer science, a Hash tree or Merkle tree is a tree in which
        every leaf node is labelled with the cryptographic hash of a data block, 
        and every non-leaf node is labelled with the hash of the labels of its child nodes.
    '''
    def __init__(self, hash_func = 'sha256'):
        self._hashfunc = getattr(hashlib, hash_func)
        self._size = 0 # number of leaf nodes in tree
        self._tree = {}
    
    def hash(self, input):
        return self._hashfunc(input.encode("utf-8")).digest()

    def addLeaf(self, string):
        hashValue = self.hash(chr(0) + string)
        self._size += 1
        self._storeNode(self._size - 1, self._size, hashValue)

    def merkel_hash_tree(self, k1, k2):
        try:
            mNode = self._retrieveNode(k1, k2)
        except Exception:   # no stored node, so make one
            k = k1 + largestPower2(k2 - k1)
            mNode = self.hash(chr(1) + str(self.merkel_hash_tree(k1, k)) + str(self.merkel_hash_tree(k,k2)))
            self._storeNode(k1, k2, mNode)
        return mNode

    def auditPath(self, m, n=None):
        if not n: n = self._size
        def _auditPath(m, k1, k2):
            if (k2 - k1) == 1:
                return [ ] # terminate with null list when range is a single node
            k = k1 + largestPower2(k2-k1)
            if m < k:
                path = _auditPath(m, k1, k) + [self.merkel_hash_tree(k,k2),]
            else:
                path = _auditPath(m, k, k2) + [self.merkel_hash_tree(k1,k),]
            return path
        
        return _auditPath(m, 0, n)

    def validPath(self, m, n, leaf_hash, root_hash, audit_path):
        def _hashAuditPath(m, k1, k2, i):
            if len(audit_path) == i:
                return leaf_hash
            k = k1 + largestPower2(k2-k1)
            ithAuditNode = audit_path[len(audit_path) - 1 - i]
            if m < k:
                hv = self.hash(chr(1) + str(_hashAuditPath(m, k1, k, i+1)) + str(ithAuditNode))
            else:
                hv = self.hash(chr(1) + str(ithAuditNode) + str(_hashAuditPath(m, k, k2, i+1)))
            return hv
           
        hv = _hashAuditPath(m, 0, n, 0)        
        return hv == root_hash
    
    def rootHash(self, n=None):
        if not n: n = self._size
        if n > 0:
            return self.merkel_hash_tree(0, n)
        else:
            return self.hash('')  # empty tree is hash of null string
            
    def leafHash(self, m):
        """ Leaf hash value for mth entry """
        return self.merkel_hash_tree(m, m+1)
        
    def __len__(self):
        return self._size

    def _retrieveNode(self, k1, k2):
        return self._tree[(k1,k2)]
    
    def _storeNode(self, k1, k2, mNode):
        # leaf and non-leaf nodes in the same dictionary indexed by range tuple
        assert k1 < k2 <= self._size
        self._tree[(k1,k2)] = mNode
        
def largestPower2(n):
    """ Return the largest power of 2 less than n """
    lp2 = 1
    while lp2 < n :
        lp2 = lp2 << 1
    return lp2 >> 1
        