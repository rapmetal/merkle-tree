# coding: utf-8

from merkel_tree import MerkelTree

tree = MerkelTree()
for i in range(0, 10):
    tree.addLeaf('value: {}'.format(i))
    n = len(tree)
    for m in range(n):
        leaf = tree.leafHash(m)
        path = tree.auditPath(m)
        root = tree.rootHash()

        isValid = tree.validPath(m, n, leaf, root, path)
        print(isValid)
        # gratuitous display of the audit path
        path_list = ''.join(
            ['\n    - {}'.format(h) for h in path])
        print('m: {}, n: {}, leaf: {}, path: {}, root: {}'.format(
            m, n, leaf, path_list, root))
