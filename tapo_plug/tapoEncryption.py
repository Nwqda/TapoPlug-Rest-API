#tapoEncryption.py   
#@package   tapo_plug
#@author    Samy (Naqwada) <naqwada@pm.me>
#@license   MIT License (http://www.opensource.org/licenses/mit-license.php)
#@docs      https://gitlab.com/Naqwada/TapoPlug-Rest-API

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_v1_5
from pkcs7 import PKCS7Encoder
import hashlib
import base64


def generateKeyPair():
  key = RSA.generate(1024)
  privateKey = key.export_key(pkcs=8)
  publicKey = key.publickey().export_key(pkcs=8)

  tapoKeyPair = {
    "publicKey": publicKey.decode('utf-8'),
    "privateKey": privateKey.decode('utf-8'),
  }

  return tapoKeyPair


def decodeTapoKey(tapoKey, tapoKeyPair):
  try:
    encrypt_data = base64.b64decode(tapoKey)
    rsa_key = RSA.importKey(tapoKeyPair["privateKey"])

    cipher = PKCS1_v1_5.new(rsa_key)
    decryptedBytes = cipher.decrypt(encrypt_data, None)

    decodedTapoKey = {
      "secretKeySpec": decryptedBytes[:16],
      "ivParameterSpec": decryptedBytes[16:32],
    }
    return decodedTapoKey
  except Exception as e:
    raise e


def shaDigestEmail(email):
  email = str.encode(email)
  emailHash = hashlib.sha1(email).hexdigest()
  return emailHash


def encryptJsonData(decodedTapoKey, jsonData):
  try:
    PKCS7 = PKCS7Encoder()
    aes = AES.new(decodedTapoKey["secretKeySpec"], AES.MODE_CBC, IV=decodedTapoKey["ivParameterSpec"])
    padJsonData = PKCS7.encode(jsonData).encode()
    encryptedJsonData = aes.encrypt(padJsonData)
    return base64.b64encode(encryptedJsonData).decode();
  except Exception as e:
    raise e


def decryptJsonData(decodedTapoKey, encryptedJsonData):
    encryptedJsonData = base64.b64decode(encryptedJsonData)
    aes = AES.new(decodedTapoKey["secretKeySpec"], AES.MODE_CBC, IV=decodedTapoKey["ivParameterSpec"])

    decryptedJsonData = aes.decrypt(encryptedJsonData)
    return decryptedJsonData.decode().strip()
