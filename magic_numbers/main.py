from pathlib import Path

def is_magic_num(szam):

    string = str(szam)
    return string == string[::-1]

def next_magic_num(n):

    next_szam = n + 1
    string = str(next_szam)

    length = len(string)
    half_szam = string[:(length + 1) // 2]
    mirrored = int(half_szam + half_szam[:length // 2][::-1])

    if mirrored > n:

        return mirrored

    half = str(int(half_szam) + 1)

    if len(half) > len(half_szam):

        return int("1" + "0" * length + "1")

    return int(half + half[:length // 2][::-1])

def main():
    data = Path("input.txt").read_text(encoding="utf-8")

    for sor in data.splitlines():

        sor = sor.strip()
        szam = eval(sor.replace("^", "**"))

        print(f"next_magic_num({szam}) => {next_magic_num(szam)}")

if __name__ == "__main__":
    main()