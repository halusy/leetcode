class Solution:
    def reverse(self, x: int) -> int:
        x_reversed = ""
        neg = ""
        i = 0

        if len(str(x)) == 1:
            return x

        for each in reversed(str(x)):
            if i == 0 and each == "0":
                continue
            if each == "-":
                neg = "-"
                continue

            i += 1
            x_reversed += each
            
        if int(x_reversed) < -(2 ** 31) or int(x_reversed) > (2 ** 31) - 1:
            return 0
        x_reversed = neg + x_reversed
        return int(x_reversed)