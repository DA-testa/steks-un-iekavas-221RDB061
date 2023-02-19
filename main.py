# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i))
            # print(opening_brackets_stack)
        
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack:
                if (are_matching(opening_brackets_stack[len(opening_brackets_stack)-1].char,next)):
                    opening_brackets_stack.pop(len(opening_brackets_stack)-1)
                    # print(opening_brackets_stack)
                else:
                    print(i+1)
                    break
            else:
                # print("net otkritoj")
                print()
                
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
