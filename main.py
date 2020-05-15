import sys
import typing
from typing import List
import urllib
import urllib.parse


class Course:
    def __init__(self, dir1: str, dir2: str, index: int, arg1: str, arg2: str, leng: int, exp: str, hmac: str):
        self.dir1: str = dir1
        self.dir2: str = dir2
        self.index: int = index
        self.arg1: str = arg1
        self.arg2: str = arg2
        self.leng: int = leng
        self.exp: str = exp
        self.hmac: str = hmac

    def build_url(self):
        return f'https://tpr307389def-vh.akamaihd.net/i/The_Teaching_Company/{self.dir1}/{self.dir2}/4790_{self.index:01d},{self.arg1},,{self.arg2},.mp4.csmil/segment{self.leng}_0_av.ts?set-akamai-hls-revision=5&hdntl=exp={self.exp}~acl=/i/The_Teaching_Company/564/895/4790_02*~data=hdntl~hmac={self.hmac} '


def parse(url: str) -> Course:
    temp: urllib.parse.ParseResult = urllib.parse.urlparse(url)
    path: str = temp.path
    split_path: List[str] = path.split('/')

    dir1: str = ''
    dir2: str = ''
    index: int = 0
    arg1: str = ''
    arg2: str = ''
    leng: int = 0
    exp: str = ''
    hmac: str = ''

    obj: Course = Course(dir1=dir1, dir2=dir2, index=index, arg1=arg1, arg2=arg2, leng=leng, exp=exp, hmac=hmac)
    return obj


def main() -> None:
    for arg in sys.argv[1:]:
        result = parse(arg)
        print(result)


if __name__ == '__main__':
    main()

