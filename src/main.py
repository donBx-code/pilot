import pilot.sample as s 
import pilot.class_example as cls

def main():
    print("running main() ")

    s.info()

    triangle:cls.Triangle = cls.Triangle(5,5)
    triangle.print()


if __name__ == "__main__":
    main()

