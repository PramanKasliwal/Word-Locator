import argparse
import os

def locate_word(word,filename,all_instances=None):
    if not os.path.isfile(filename):
        print(f'{filename} not found')
        return
    line_number = 1
    line_nums = []
    found = False
    with open(filename,'rb') as fobj:
        all_text = fobj.read().decode()
    all_text = all_text.split('\n')
    for line in all_text:
        if word in line:
            found = True
            if not all_instances:
                break
            else:
                line_nums.append(str(line_number))
        line_number+=1
    if not found:
        print(f'"{word}" does not exist in {filename}')
    else:
        if all_instances:
            print(f'"{word}" found in {filename} at lines {", ".join(line_nums)}.')
        else:
            print(f'"{word}" found at {line_number} in {filename}')
    return


def main():
    parser = argparse.ArgumentParser(description="Syntax: python3 %s --word <word> --file <filename>" % (os.path.basename(__file__)))
    parser.add_argument('--word', help="Word to be searched in the wordlist",required=True)
    parser.add_argument('--file', help='Wordlist',required=True)
    parser.add_argument('--all', help='Find all the instances of the word in the file',action='store_true')
    args = parser.parse_args()

    word = args.word
    filename = args.file
    all_instances = args.all

    locate_word(word,filename,all_instances)

if __name__ == '__main__':
    main()
