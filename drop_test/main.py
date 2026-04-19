from pathlib import Path

def minimalis_dobasok(ksz, cel_m):
    if cel_m == 0: return 0
    if ksz == 1: return cel_m

    tabla = [[0] * (ksz + 1)]
    akt_p = 0
    
    while tabla[akt_p][ksz] < cel_m:
        akt_p += 1
        ujs = [0] * (ksz + 1)
        tabla.append(ujs)
        
        for k in range(1, ksz + 1):
            alatt = tabla[akt_p - 1][k - 1]
            felett = tabla[akt_p - 1][k]
            tabla[akt_p][k] = 1 + alatt + felett
            
    return akt_p

def main():
    fajl = Path("input.txt")
    if not fajl.exists(): return

    for sor in fajl.read_text(encoding="utf-8").splitlines():
        if "," in sor:
            r = sor.split(",")
            n_db = int(r[0].strip())
            h_m = int(r[1].strip())
            valasz = minimalis_dobasok(n_db, h_m)
            print(f"min_num_of_drops({n_db}, {h_m}) => {valasz}")

if __name__ == "__main__":
    main()