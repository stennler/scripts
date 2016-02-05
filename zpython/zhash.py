import hashlib


def hash(hash_string):
    """Hashes a string and returns the hexdigest (SHA-1)"""
    hasher = hashlib.sha1()
    hasher.update(hash_string)
    return hasher.hexdigest()


def hash_file(path):
    """Hashes the given file and returns the hexdigest (SHA-1)"""
    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    with open(path, 'rb') as file_to_hash:
        buf = file_to_hash.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = file_to_hash.read(BLOCKSIZE)
        return hasher.hexdigest()
    return None


def hash_object(hash_string):
    """Hashes a string and returns the corresponding hash object. (SHA-1)"""
    hasher = hashlib.sha1()
    hasher.update(hash_string)
    return hasher
