
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        return f"Making a call to {number}."

    def receive_call(self, number):
        return f"Receiving a call from {number}."

    def take_a_picture(self):
        return f"Taking a picture with {self.rear_camera} camera."

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
    apple_phone1 = Apple("12MP", "48MP", "4GB", "64GB")
    apple_phone2 = Apple("8MP", "32MP", "3GB", "32GB")

    samsung_phone1 = Samsung("16MP", "64MP", "6GB", "128GB")
    samsung_phone2 = Samsung("10MP", "48MP", "4GB", "64GB")


    print("Samsung Phone 1 Details:")
    print(samsung_phone1)
    print(samsung_phone1.make_call("345-678-9012"))
    print(samsung_phone1.receive_call("765-432-1098"))
    print(samsung_phone1.take_a_picture())
    print()

    print("Samsung Phone 2 Details:")
    print(samsung_phone2)
    print(samsung_phone2.make_call("456-789-0123"))
    print(samsung_phone2.receive_call("654-321-0987"))
    print(samsung_phone2.take_a_picture())
    

    print("Apple Phone 1 Details:")
    print(apple_phone1)
    print(apple_phone1.make_call("123-456-7890"))
    print(apple_phone1.receive_call("098-765-4321"))
    print(apple_phone1.take_a_picture())
    print()

    print("Apple Phone 2 Details:")
    print(apple_phone2)
    print(apple_phone2.make_call("234-567-8901"))
    print(apple_phone2.receive_call("876-543-2109"))
    print(apple_phone2.take_a_picture())
    print()