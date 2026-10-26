"""Робота 6, крок 1: розминка — читання файлу й середнє без регулярних виразів."""

# 1.1. Кожен рядок words.txt — великими літерами
with open("data/words.txt", encoding="utf-8") as f:
    for ryadok in f:
        print(ryadok.rstrip().upper())

# 1.2. Середнє X-DSPAM-Confidence у mbox-short.txt — лише startswith і split
suma = 0.0
kilkist = 0
with open("data/mbox-short.txt", encoding="utf-8") as f:
    for ryadok in f:
        if ryadok.startswith("X-DSPAM-Confidence:"):
            suma += float(ryadok.split(":")[1])
            kilkist += 1

print(f"\nРядків X-DSPAM-Confidence: {kilkist}")
print(f"Середнє: {suma / kilkist}")
