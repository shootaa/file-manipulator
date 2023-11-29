user_input = input("コマンドを入力してください: ")
parts = user_input.split()


if len(parts) == 3:
    command = user_input[0]
    if command == 'reverse':
        inputpath = user_input[1]
        outpath = user_input[2]
        with open(inputpath) as f:
            contents = f.read()
        with open(outpath, 'w') as f:
            f.write(contents[::-1])
    if command == 'copy':
        inputpath = user_input[1]
        outputpath = user_input[2]
        with open(inputpath) as f:
            contents = f.read()
        with open(outpath, 'w') as f:
            f.write(contents)
    if command == 'duplicate-contents':
        inputpath = user_input[1]
        n = user_input[2]
        with open(inputpath) as f:
            contents = f.read()
        for x in range(n):
            with open(inputpath, 'a') as f:
                f.write(contents)

    if command == 'replace-string':
        inputpath = user_input[1]
        needle = user_input[2]
        newstring = user_input[3]
        with open(inputpath) as f:
            contents = f.read()
        replaced_contents = contents.replace(needle, newstring)
        with open(inputpath, 'w') as f:
            f.write(replaced_contents)
else:
    print('入力されたコマンドが正しくありません')
