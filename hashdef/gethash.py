import hashlib

def get_hash(path):
    with open(path, 'rb') as f:
        contents = f.read()
        md5 = hashlib.md5(contents).hexdigest()
        sha1 = hashlib.sha1(contents).hexdigest()
        sha256 = hashlib.sha256(contents).hexdigest()

    return md5, sha1, sha256


if __name__ == '__main__':

    print("Input path : ")
    path = input()

    md5, sha1, sha256 = get_hash(path)
    print("md5 : {}, sha1 : {}, sha256 : {}".format(md5, sha1, sha256))


# https://ingorae.tistory.com/505 - with / as

# formatted string literal
# print(f"md5 ...
# https://docs.python.org/ko/3/tutorial/inputoutput.html - python 2.7
# https://wikidocs.net/20562 - python 3.5
