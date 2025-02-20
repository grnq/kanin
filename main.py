global some_value

def main(val):
    some_value = val
    if (testing):
       print(f"Testing {some_value}")
    else:
       print(f"No testing {some_value}")

def testing():
    if some_value > 3:
      return True
    else:
      return False


if __name__ == "__main__":
    main(2)
    main(3)
    main(7)