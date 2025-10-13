#!/usr/bin/python3

import sys
import getopt

name = ""


def usage():
    print("Simple Username Generator")
    print("Usage: python3 username_gen.py -n \"FULL NAME\"")
    print()
    print("Examples:")
    print("  python3 username_gen.py -n \"Mark Zuckerberg\"")
    sys.exit(0)


def generate_usernames(full_name):
    names = full_name.split()
    usernames = set()

    if len(names) >= 2:
        first = names[0].lower()
        last = names[-1].lower()

        usernames.add(first)
        usernames.add(last)

        usernames.add(first + last)
        usernames.add(first + "." + last)
        usernames.add(last + first)
        usernames.add(last + "." + first)

        usernames.add(first[0] + last)
        usernames.add(first[0] + "." + last)
        usernames.add(last[0] + first)
        usernames.add(last[0] + "." + first)

        usernames.add(last[:2] + first)
        usernames.add(last[:2] + "." + first)
        usernames.add(first[:2] + last)
        usernames.add(first[:2] + "." + last)

    else:
        single = names[0].lower()
        usernames.add(single)

    return list(usernames)


def main():
    global name

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:", ["help", "name="])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-n", "--name"):
            name = a
        else:
            print("flag provided but not defined: " + o)
            usage()

    if not name:
        print("[-] Name is required")
        usage()

    print("[*] Generating usernames for: " + name)
    print("=" * 50)

    usernames = generate_usernames(name)

    for username in usernames:
        print(username)

    print("=" * 50)
    print("[*] Generated completed.")


if __name__ == "__main__":
    main()
