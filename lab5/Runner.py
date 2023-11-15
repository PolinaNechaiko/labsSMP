from Lb5.Interface import ShapeInterface


class Runner:
    def __init__(self):
        self.interface = ShapeInterface()

    def run(self):
        while True:
            print("\n----- Menu -----")
            print("1. Create Cube")
            print("2. Create Pyramid")
            print("3. Exit")

            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                self.interface.create_cube()
            elif choice == '2':
                self.interface.create_pyramid()
            elif choice == '3':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 3.")

if __name__ == "__main__":
    runner = Runner()
    runner.run()
