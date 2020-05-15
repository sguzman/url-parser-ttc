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
        return f'https://tpr307389def-vh.akamaihd.net/i/The_Teaching_Company/{self.dir1}/{self.dir2}/4790_{self.index:02d},{self.arg1},,{self.arg2},.mp4.csmil/segment{{$ii}}_0_av.ts?set-akamai-hls-revision=5&hdntl=exp={self.exp}~acl=/i/The_Teaching_Company/564/895/4790_02*~data=hdntl~hmac={self.hmac} '

    def output_fish_script(self):
        return f"""
for ii in (seq {self.leng})
    http --continue --verbose --download --output "{self.index}_$ii.av.ts" '{self.build_url()}'
end

for ii in (seq {self.leng})
    cat "{self.index}_$ii.av.ts"
end > "{self.index}.ts"

ffmpeg -i {self.index}.ts -acodec copy -vcodec copy {self.index}.mp4
rm {self.index}*.ts
        """


def parse(url: str) -> Course:
    temp: urllib.parse.ParseResult = urllib.parse.urlparse(url)
    path: str = temp.path
    split_path: List[str] = path.split('/')
    split_args: List[str] = split_path[5].split(',')
    index_temp: str = split_args[0].split('_')[1]
    temp_length: str = split_path[-1]
    temp_length2: str = temp_length.split('_')[0].lstrip('segment')
    query: str = temp.query
    split_query: List[str] = query.split('&')
    split_query_eq: List[str] = split_query[1].split('=')
    exp_temp: str = split_query_eq[2].split('~')[0]

    dir1: str = split_path[3]
    dir2: str = split_path[4]
    index: int = int(index_temp)
    arg1: str = split_args[1]
    arg2: str = split_args[3]
    leng: int = int(temp_length2)
    exp: str = exp_temp
    hmac: str = split_query_eq[5]

    obj: Course = Course(dir1=dir1, dir2=dir2, index=index, arg1=arg1, arg2=arg2, leng=leng, exp=exp, hmac=hmac)
    return obj


def main() -> None:
    for arg in sys.argv[1:]:
        result = parse(arg)
        output_fish_script: str = result.output_fish_script()
        print(output_fish_script)


if __name__ == '__main__':
    main()

