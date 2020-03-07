# merkle-tree

In cryptography and computer science, a hash tree or Merkle tree is a tree in which every leaf node is labelled with the cryptographic hash of a data block, and every non-leaf node is labelled with the hash of the labels of its child nodes. Hash trees allow efficient and secure verification of the contents of large data structures. Hash trees are a generalization of hash lists and hash chains.

Demonstrating that a leaf node is a part of a given binary hash tree requires computing a number of hashes proportional to the logarithm of the number of leaf nodes of the tree; this contrasts with hash lists, where the number is proportional to the number of leaf nodes itself.

The concept of hash trees is named after Ralph Merkle who patented it in 1979.

## References
Becker, Georg (2008-07-18). [Merkle Signature Schemes, Merkle Trees and Their Cryptanalysis](https://www.emsec.ruhr-uni-bochum.de/media/crypto/attachments/files/2011/04/becker_1.pdf). Ruhr-Universität Bochum. p. 16. Retrieved 2013-11-20.

Merkle, R. C. (1988). A Digital Signature Based on a Conventional Encryption Function. Advances in Cryptology — CRYPTO '87. Lecture Notes in Computer Science. 293. pp. 369–378. doi:10.1007/3-540-48184-2_32. ISBN 978-3-540-18796-7.

## Further reading
[Merkle tree patent](https://patents.google.com/patent/US4309569) – explains both the hash tree structure and the use of it to handle many one-time signatures
[Tree Hash EXchange format](https://web.archive.org/web/20080316033726/http://www.open-content.net/specs/draft-jchapweske-thex-02.html) – a detailed description of Tiger trees

[A C implementation of a dynamically re-sizeable binary SHA-256 hash tree](https://github.com/IAIK/merkle-tree)

[Merkle tree implementation in Java](https://github.com/richpl/merkletree)