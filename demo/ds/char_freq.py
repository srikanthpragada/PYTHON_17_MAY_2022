st = "How are you doing today"

visited = ""
for c in st:
    if c not in visited:
        print(f"{c} {st.count(c)}")
        visited += c
