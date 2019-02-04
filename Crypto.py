import hashlib

def get_pub_key(privateKey):

    sha = hashlib.sha256()
    sha.update(privateKey.encode('utf-8'))

    # make all 'addresses' 64 bits
    key = "0x" + sha.hexdigest()[:-32]
    return key

def hash_str(str_to_hash):
    sha = hashlib.sha256()
    sha.update(str_to_hash.encode('utf-8'))
    h_str = "0x" + sha.hexdigest()
    return h_str
