from pathlib import Path
from datetime import datetime
import math

def dij_szamolo(perc):

    if perc < 0: return "HIBA"
    
    if perc >= 1440:
        napok = math.ceil(perc / 1440)
        return napok * 10000

    if perc <= 30:
        return 0
    
    fennmarado_perc = perc - 30
    orak = math.ceil(fennmarado_perc / 60)
    
    osszeg = 0
    for i in range(1, orak + 1):
        if i <= 3:
            osszeg += 300
        else:
            osszeg += 500
            
    return osszeg

def main():
    be_fajl = Path("input.txt")
    ki_fajl = Path("output.txt")
    if not be_fajl.exists(): return

    sorok = be_fajl.read_text(encoding="utf-8").splitlines()
    eredmenyek = []

    for sor in sorok:
        s = sor.strip()
        if not s or "RENDSZAM" in s or "==" in s: continue
        
        r = s.split()
        if len(r) >= 5:
            rsz = r[0]
            be_s = f"{r[1]} {r[2]}"
            ki_s = f"{r[3]} {r[4]}"
            
            form = "%Y-%m-%d %H:%M:%S"
            be_d = datetime.strptime(be_s, form)
            ki_d = datetime.strptime(ki_s, form)
            
            p = (ki_d - be_d).total_seconds() / 60
            fizet = dij_szamolo(p)
            
            sor_ki = f"{rsz}: {fizet} forint"
            print(sor_ki)
            eredmenyek.append(sor_ki)

    ki_fajl.write_text("\n".join(eredmenyek), encoding="utf-8")

if __name__ == "__main__":
    main()