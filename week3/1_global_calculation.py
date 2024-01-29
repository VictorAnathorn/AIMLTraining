global_number = 10


def perform_calculation():
    global global_number

    local_number = 5

    print("Before calculation:")
    print("Global variable:", global_number)
    print("Local variable:", local_number)

    result = global_number + local_number

    global_number = result

    print("\nAfter calculation:")
    print("Global variable:", global_number)
    print("Local variable:", local_number)
    print("Result of calculation:", result)


perform_calculation()
