# Strips css of text/lines. Makes browsers happy.

with open('../assets/css/style.css', 'r') as f:
    text = f.read()
    text = text.replace(" ", "")
    text = text.replace("\n", "")

f = open('../assets/css/style.min.css', 'wb')
f.write(text)
f.close()
