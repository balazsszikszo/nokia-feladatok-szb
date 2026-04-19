from pathlib import Path

def kovetkezo_magikus(n):
    s = str(n + 1)
    hossz = len(s)
    
    bal = s[:(hossz + 1) // 2]
    
    def tukroz(feles):
        t = feles + feles[:hossz // 2][::-1]
        return int(t)

    m = tukroz(bal)
    
    if m >= n + 1:
        return m
    
    uj_bal = str(int(bal) + 1)
    
    if len(uj_bal) > len(bal):
        return int("1" + "0" * (hossz - 1) + "1")
        
    return tukroz(uj_bal)

def main():
    be_ut = Path("input.txt")
    if not be_ut.exists(): return

    for sor in be_ut.read_text(encoding="utf-8").splitlines():
        if not (s := sor.strip()): continue
        
        szam = eval(s.replace("^", "**"))
        print(f"next_magic_num({szam}) => {kovetkezo_magikus(szam)}")

if __name__ == "__main__":
    main()