def foo(ascii, a, b, c):

    for i in range(len(ascii)):
        if i % 3 == 0:
            ascii[i] = chr((ascii[i] + a) % 256)
        elif i % 3 == 1:
            ascii[i] = chr((ascii[i] + b) % 256)
        elif i % 3 == 2:
            ascii[i] = chr((ascii[i] + c) % 256)
    return "".join(ascii)


ascii = "104 88 157 140 98 93 64 54 160 142 90 163 129 103 166 140 84 165 137 98 159 147 19 151 143 101 81 147 98 157 150 92 159 135 19 165 136 88 81 103 84 158 130 92 165 64 86 153 129 95 157 133 97 152 133 33 81 112 95 150 129 102 150 64 102 150 142 87 81 153 98 166 146 19 164 143 95 166 148 92 160 142 19 146 142 87 81 99 73 81 148 98 81 137 86 146 142 86 160 132 88 113 135 84 158 130 92 165 146 88 164 133 84 163 131 91 95 131 98 158 64 100 166 143 103 154 142 90 81 146 88 151 133 101 150 142 86 150 90 19 149 83 42 99 89 44 101 134 89 106 78"
ascii = [int(x) for x in ascii.split(" ")]
print(len(ascii))
a = ord(".")-ascii[-1]
b = ord("e")-ascii[1]
c = ord("l")-ascii[2]
print(a,b,c)
print(foo(ascii, a, b, c))