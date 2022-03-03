import os


def main():

    bg = open("bg.txt", "w")
    directory = os.listdir(os.path.abspath("img"))
    path = os.path.abspath("img") + "//"
    print(path)
    i = 1
    for file in directory:
        os.rename(path+file, path+f"img{i}.jpg")
        print(file)
        i = i+1
        bg.write(f"img/img{i}.jpg\n")

    bg.close()


if __name__ == '__main__':
    main()
