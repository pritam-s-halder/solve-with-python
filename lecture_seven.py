with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print(data)
    else:
        print("not found")
