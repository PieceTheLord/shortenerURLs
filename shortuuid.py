import hashlib

print(hashlib.sha512(b"http://localhost:8080/username/home/friend").hexdigest()[:8])