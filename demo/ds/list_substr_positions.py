# Print all positions of substring
st = "How do you do"
ss = "o"

pos = -1
while True:
    pos = st.find(ss, pos + 1)
    if pos == -1:
        break

    print(pos)

