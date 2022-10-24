file_name = str.casefold(input("Filename: ")).strip()
file_ext = file_name.rsplit('.', maxsplit=1)[-1]


if file_ext == "jpg":
    file_ext = "jpeg"
    new_fname = "image/" + file_ext
    print(new_fname)
else:
    match file_ext: 
        case "gif" | "jpeg" | "png":
            new_fname = "image/" + file_ext
            print(new_fname)
        case "pdf" | "zip":
            new_fname = "application/" + file_ext
            print(new_fname)
        case "txt":
            new_fname = "text/plain"
            print(new_fname)
        case _:
            print("application/octet-stream")
