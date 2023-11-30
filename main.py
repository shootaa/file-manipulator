user_input = input("コマンドを入力してください: ")
parts = user_input.split()
command = parts[0]


if len(parts) == 3:
    if command == 'reverse':
        inputpath = parts[1]
        outputpath = parts[2]
        with open(inputpath) as f:
            contents = f.read()
        with open(outputpath, 'w') as f:
            f.write(contents[::-1])
    if command == 'copy':
        inputpath = parts[1]
        outputpath = parts[2]
        with open(inputpath) as f:
            contents = f.read()
        with open(outputpath, 'w') as f:
            f.write(contents)
    if command == 'duplicate-contents':
        inputpath = parts[1]
        n = int(parts[2])
        with open(inputpath) as f:
            contents = f.read()
        for x in range(n):
            with open(inputpath, 'a') as f:
                f.write(contents)
elif len(parts) == 4:
    if command == 'replace-string':
        inputpath = parts[1]
        needle = parts[2]
        newstring = parts[3]
        with open(inputpath) as f:
            contents = f.read()
        replaced_contents = contents.replace(needle, newstring)
        with open(inputpath, 'w') as f:
            f.write(replaced_contents)

else:    
    print('入力されたコマンドが正しくありません')
