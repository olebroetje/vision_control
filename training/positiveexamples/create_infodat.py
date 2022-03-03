import os


def main():

    info = open("info.dat", "w")
    directory = os.listdir(os.path.abspath("img"))
    path = os.path.abspath("img") + "//"
    print(path)
    i = 1
    for file in directory:
        os.rename(path + file, f"{path}img{i}.jpg")
        print(file)
        info.write(f"img/img{i}.jpg\n")
        i = i + 1

    info.close()


if __name__ == '__main__':
    main()
