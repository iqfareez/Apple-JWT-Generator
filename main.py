import jwt
import time
import os

# Team ID
team_id = os.environ['TEAM_ID']

# Key ID
key_id = os.environ['KEY_ID']

# Private Key
# private_key = bytes(os.environ['PRIVATE_KEY'].replace('\\n', '\n').encode('utf-8'))
private_key=b'-----BEGIN PRIVATE KEY-----\nMIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgFWp6A9RgVg+CHCar\nP9QD4JRNARm3HfzVxwN4lcPGxX2gCgYIKoZIzj0DAQehRANCAAQZEMpdS5SyjmOA\nkK4dLJSMwuAetrZeVwrQOUgrFJEv1GQNDQPdDkWxrVAUYXF2ZSqgOo67PGlGnh1P\nlzJO2EV1\n-----END PRIVATE KEY-----'

issued_timestamp = time.time()
expiration_timestamp = issued_timestamp + 1800

encoded = jwt.encode({'iss': team_id,'iat': issued_timestamp,'exp': expiration_timestamp, 'aud': "https://appleid.apple.com", 'sub' : os.environ['SUBJECT']}, private_key, algorithm='ES256', headers={'kid': key_id})

print(encoded)
