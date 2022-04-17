from jisho_api.word import Word
from jisho_api.tokenize import Tokens
from jisho_api.kanji import Kanji

def main():
    with open("./jisho_dict/text.txt") as f:
        import pdb; pdb.set_trace()
        lines = f.readlines()
        for line in lines:
            if "-----" in line or line == "\n" or line.endswith('/'):
                continue
            # import pdb; pdb.set_trace()
            print(line.replace("\n", ""))

    # r = Tokens.request('私の山羊')
    return ''

if __name__ == '__main__':
    main()
