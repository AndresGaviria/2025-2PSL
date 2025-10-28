import jwt;

try:
    key = "EstaEsLaContraseña";

    encode = jwt.encode({"Usuario": "Test.jhsgdfhgdjh"}, key, algorithm="HS256");
    print(encode);

    decode = jwt.decode(encode, key, algorithms="HS256");
    print(decode);
except Exception as ex:
    print(ex);

"""
py -m pip install PyJWT
"""