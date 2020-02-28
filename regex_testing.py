import re

x = [
    'well what is $5k to you or $5million or $500,000 or 5kk or $e or $500.32',
    '$5bill'
]

all_comments = []
for all in x:
    b = re.findall(r"\$(\d+\S+)", all)
    for all in b:
        all_comments.append(all)

#b = re.findall(r"\$(\d+\S+)", x)
print(all_comments)
#print(b)
