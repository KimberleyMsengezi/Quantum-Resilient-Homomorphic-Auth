import numpy as np

class HomomorphicAuth:
    """Simple BFV-style lattice homomorphic encryption for auth tokens"""
    
    def __init__(self):
        self.modulus = 2**32  
        self.secret_key = np.random.randint(1, 1000)
    
    def encrypt(self, token: int):
        noise = np.random.randint(-10, 10)
        ciphertext = (token + self.secret_key * noise) % self.modulus
        return ciphertext
    
    def homomorphic_equals(self, ct1: int, ct2: int):
        """Check equality on ciphertexts without decryption"""
        return (ct1 - ct2) % self.modulus == 0
