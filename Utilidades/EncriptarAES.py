import hashlib
import binascii, os
from Crypto.Cipher import AES

class EncriptarAES:
    secretKey = os.urandom(32);
        
    def Encriptar(self, valor: str) -> str :
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM);
        ciphertext, authTag = aesCipher.encrypt_and_digest(str.encode(valor));
        response = (ciphertext, aesCipher.nonce, authTag);
        return binascii.hexlify(response[0]).decode() + '|' + binascii.hexlify(response[1]).decode() + '|' + binascii.hexlify(response[2]).decode();

    def Descifrar(self, valor: str) -> str :
        split = valor.split('|');
        ciphertext = binascii.unhexlify(split[0]);
        nonce = binascii.unhexlify(split[1]);
        authTag = binascii.unhexlify(split[2]);
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce);
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag);
        return plaintext.decode();