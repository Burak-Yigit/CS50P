file_extension_type = input("File name: ").lower().strip()

if file_extension_type.endswith(".gif"):
    print("image/gif")

elif file_extension_type.endswith(".jpg") or file_extension_type.endswith(".jpeg"):
    print("image/jpeg")

elif file_extension_type.endswith(".png"):
    print("image/png")

elif file_extension_type.endswith(".pdf"):
    print("application/pdf")

elif file_extension_type.endswith(".txt"):
    print("text/plain")

elif file_extension_type.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")