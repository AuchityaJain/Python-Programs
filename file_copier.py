# file_copier.py

with open('file_in.txt', 'r') as file_in:
    content = file_in.read()

with open('file_out.txt', 'w') as file_out:
    file_out.write(content)

with open('file_out.txt', 'r') as file_out:
    output_content = file_out.read()

print(output_content)
