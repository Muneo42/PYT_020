from pkg.p1.m1 import *
from pkg.p1.m2 import *
from pkg.p2.m1 import *

def main():
    v = cast_string_to_list("ABCD")
    print(v)
    v = cast_elements_to_integers(v)
    print(v)
    v = cast_elements_to_binaries(v)
    print(v)
    v = justify_elements(v)
    print(v)
    v = lst_to_str(v)
    print(v)
    v = split_into_six(v)
    print(v)
    v = justify_last_block(v)
    print(v)
    v = cast_binaries_to_decimals(v)
    print(v)
    v = create_base64_list(v)
    print(v)
    v = create_base64_string(v)
    print(v)
    v = justify_base64_string(v)
    print(v)

if __name__ == '__main__':
    main()

