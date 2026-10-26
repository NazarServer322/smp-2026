"""Робота 6: розбір журналу сервера data/access.log іменованими групами.

    python praktyka/06-regex-log/log-parser.py
"""
import re
import sys
from collections import Counter, defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

# IP на початку рядка, час у [ ], метод і шлях — перші два слова в лапках,
# протокол пропускаємо [^"]*, далі після лапки — рівно три цифри коду.
SHABLON = re.compile(
    r'^(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) '
    r'.*?\[(?P<chas>[^\]]+)\] '
    r'"(?P<metod>[A-Z]+) (?P<shliakh>\S+)[^"]*" '
    r'(?P<kod>\d{3}) '
)

rozibrano = 0
propushcheno = 0
ip = Counter()
kody = Counter()
pomylky_5xx = []
shliakhy_5xx = Counter()
shliakhy_404 = Counter()
khto_404 = defaultdict(set)

with open("data/access.log", encoding="utf-8") as f:
    for ryadok in f:
        m = SHABLON.search(ryadok)
        if not m:
            propushcheno += 1
            continue
        rozibrano += 1
        ip[m["ip"]] += 1
        kody[m["kod"]] += 1
        if m["kod"].startswith("5"):
            pomylky_5xx.append((m["chas"], m["shliakh"], m["kod"]))
            shliakhy_5xx[m["shliakh"]] += 1
        if m["kod"] == "404":
            shliakhy_404[m["shliakh"]] += 1
            khto_404[m["shliakh"]].add(m["ip"])

print("== 1. Рядки")
print(f"Розібрано: {rozibrano}, пропущено: {propushcheno}")

print("\n== 2. Топ-5 IP-адрес")
for adresa, kilkist in ip.most_common(5):
    print(f"{kilkist:4}  {adresa}")

print(f"\n== 3. Коди відповіді (різних: {len(kody)})")
for kod, kilkist in sorted(kody.items()):
    print(f"{kod}: {kilkist}")

print(f"\n== 4. Запити з помилкою 5xx (усього: {len(pomylky_5xx)})")
for chas, shliakh, kod in pomylky_5xx:
    print(f"{chas}  {kod}  {shliakh}")

print("\n== 5xx за шляхами")
for shliakh, kilkist in shliakhy_5xx.most_common():
    print(f"{kilkist:4}  {shliakh}")

print("\n== 404 за шляхами")
for shliakh, kilkist in shliakhy_404.most_common():
    adresy = ", ".join(sorted(khto_404[shliakh]))
    print(f"{kilkist:4}  {shliakh}   ← {adresy}")
