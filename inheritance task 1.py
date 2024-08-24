
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def __str__(self):
        return (f"Screen Type: {self.screen_type}\n"
                f"Network Type: {self.network_type}\n"
                f"Dual SIM: {self.dual_sim}\n"
                f"Front Camera: {self.front_camera}\n"
                f"Rear Camera: {self.rear_camera}\n"
                f"RAM: {self.ram}\n"
                f"Storage: {self.storage}")


class Apple(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", "4G/5G", True, front_camera, rear_camera, ram, storage)
        self.brand = "Apple"

    def __str__(self):
        return f"Brand: {self.brand}\n{super().__str__()}"


class Samsung(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", "4G/5G", True, front_camera, rear_camera, ram, storage)
        self.brand = "Samsung"

    def __str__(self):
        return f"Brand: {self.brand}\n{super().__str__()}"


if __name__ == "__main__":

    apple_phone = Apple("12MP", "48MP", "4GB", "64GB")
    samsung_phone = Samsung("16MP", "32MP", "3GB", "32GB")
    print("Samsung Phone Details:")
    print(samsung_phone)

    print("Apple Phone Details:")
    print(apple_phone)
    print()


 
