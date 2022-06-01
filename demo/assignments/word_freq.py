st = "how are you and how are you doing"

words = st.split(" ")

for w in sorted(set(words)):
    print(f"{w:10} {words.count(w)}")
